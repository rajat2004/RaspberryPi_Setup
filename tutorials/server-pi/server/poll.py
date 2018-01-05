import os
import time
import tensorflow as tf
import shutil
import subprocess
from darkflow.net.build import TFNet
import cv2
from multiprocessing import Process

# Monodepth Imports
import numpy as np
import argparse
import re
import time
import tensorflow as tf
import tensorflow.contrib.slim as slim
import scipy.misc
import matplotlib.pyplot as plt


# Custom modules
import constants

# IP Initialisation
RPI_IP,MAC_IP=constants.read_IP()

PORT_OP='~/Documents/Academics/IIT\ M/Projects/Smart\ DB/mac_interface/ssh_output/'
PORT_RPI='pi@'+RPI_IP+':~/Desktop/raspberry/ssh_output/'

image_path='./ssh_input/image.jpg'

# Darkflow configuration
options = {"model": "cfg/tiny-yolo-voc.cfg", "load": "tiny_yolo_voc.weights", "threshold": 0.1}
tfnet = TFNet(options)

##########

# Monodepth Initialisation
parser = argparse.ArgumentParser(description='Monodepth TensorFlow implementation.')

parser.add_argument('--encoder',          type=str,   help='type of encoder, vgg or resnet50', default='vgg')
parser.add_argument('--image_path',       type=str,   help='path to the image', required=False)
parser.add_argument('--checkpoint_path',  type=str,   help='path to a specific checkpoint to load',default="checkpoints/model_city2kitti",required=False)
parser.add_argument('--input_height',     type=int,   help='input height', default=256)
parser.add_argument('--input_width',      type=int,   help='input width', default=512)

args = parser.parse_args()

params = monodepth_parameters(
    encoder=args.encoder,
    height=args.input_height,
    width=args.input_width,
    batch_size=2,
    num_threads=1,
    num_epochs=1,
    do_stereo=False,
    wrap_mode="border",
    use_deconv=False,
    alpha_image_loss=0,
    disp_gradient_loss_weight=0,
    lr_loss_weight=0,
    full_summary=False)

# SESSION
config = tf.ConfigProto(allow_soft_placement=True)
sess = tf.Session(config=config)

# SAVER
# INIT
sess.run(tf.global_variables_initializer())
sess.run(tf.local_variables_initializer())
#train_saver = tf.train.Saver()
coordinator = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coordinator)
left  = tf.placeholder(tf.float32, [2, args.input_height, args.input_width, 3])
model = MonodepthModel(params, "test", left, None)
# RESTORE
restore_path = args.checkpoint_path.split(".")[0]
#train_saver.restore(sess, restore_path)
tf.train.Saver().restore(sess, restore_path)

############

# Distance Calibration
Pixel=(150,150)
Pixel_to_metres_per_depth=1
camera_matrix=None

def calibrate():
    '''
    Define Pixel_to_metres, Pixel
    '''
    input_image="calibrate/*.jpg"


def YOLO_infer():
    ''' Will be a dictionary of objects found'''
    global image_data
    global YOLO_result
    YOLO_result=tfnet.return_predict(image_data)

    # Need to modify
    label_colour={"Sink":(255, 0, 0),\
    "Bidet":(0, 255, 0),\
    "Shower":(0, 0, 255),\
    "Tap":(0, 255, 255),\
    "Bathtub":(255, 255, 0),\
    "Toilet":(255,0, 255),\
    "Toilet_paper":(120, 120, 255)}

    font = cv.FONT_HERSHEY_SIMPLEX
    for i in result:
        topleft_coord=(i['topleft']['x'],i['topleft']['y'])
        bottomright_coord=(i['bottomright']['x'],i['bottomright']['y'])
        imgcv=cv2.rectangle(imgcv,topleft_coord,bottomright_coord,(0,255,0),3)
        cv.putText(imgcv,i['label'],topleft_coord, font, 0.8, (0, 255, 0), 2, cv.LINE_AA)
    cv2.imsave("YOLO_output/YOLO.jpg",imgcv)

def monovision_infer():
    global image_data
    global monovision_result
    global sess
    global train_saver
    global params

    # BGR to RGB
    image_data = image_data[:,:,::-1]

    def post_process_disparity(disp):
        _, h, w = disp.shape
        l_disp = disp[0,:,:]
        r_disp = np.fliplr(disp[1,:,:])
        m_disp = 0.5 * (l_disp + r_disp)
        l, _ = np.meshgrid(np.linspace(0, 1, w), np.linspace(0, 1, h))
        l_mask = 1.0 - np.clip(20 * (l - 0.05), 0, 1)
        r_mask = np.fliplr(l_mask)
        return r_mask * l_disp + l_mask * r_disp + (1.0 - l_mask - r_mask) * m_disp

    left  = tf.placeholder(tf.float32, [2, args.input_height, args.input_width, 3])
    model = MonodepthModel(params, "test", left, None)

    input_image = image_data
    original_height, original_width, num_channels = input_image.shape
    input_image = scipy.misc.imresize(input_image, [args.input_height, args.input_width], interp='lanczos')
    input_image = input_image.astype(np.float32) / 255
    input_images = np.stack((input_image, np.fliplr(input_image)), 0)

    disp = sess.run(model.disp_left_est[0], feed_dict={left: input_images})
    disp_pp = post_process_disparity(disp.squeeze()).astype(np.float32)

    output_directory = os.path.dirname(args.image_path)
    output_name = os.path.splitext(os.path.basename(args.image_path))[0]

    disp_to_img = scipy.misc.imresize(disp_pp.squeeze(), [original_height, original_width])
    monovision_result=disp_to_img
    scipy.misc.imsave("monovision_output/monovision.jpg",monovision_result)
    print('done!')

def extract_points(YOLO_result,monovision_result):
    extracted_points=[]
    for result in YOLO_result:
        '''
        format:
        {'label': 'person', 'confidence': 0.51818663, 'topleft': {'x': 686, 'y': 195}, 'bottomright': {'x': 1164, 'y': 719}}
        '''
        point_map={'label':result['label'],'confidence':result['confidence']}
        centroid=(int(sum(result['topleft']['x'],result['bottomright']['x'])/2),\
                int(sum(result['topleft']['y'],result['bottomright']['y'])/2))

        centroid_depth_heat=monovision_result[centroid]
        point_map_depth=float(monovision_result[centroid]*Depth_of_Ultrasound)/(monovision_result[Pixel])
        point_map_width=Pixel_to_metres_per_depth*point_map_depth*(abs(150-centroid[0]))
        point_map['coordinates_relative']=(point_map_depth,point_map_width)

while (True):
    if os.path.isfile(image_path):
        # If image transferred
        time.sleep(0.1)
        image_data = cv2.imread(image_path)

        # Now apply YOLO and monovision
        YOLO_result=None

        monovision_result=None

        p1=Process(target=YOLO_infer)
        p2=Process(target=monovision_infer)
        p1.start()
        p2.start()

        # Now start finiding the distances
        with open('./ssh_output/ssh_output.rb','wb') as file:
            pickle.dump(distance_dictionary,file)

        shutil.rmtree('./ssh_input')
        os.mkdir('./ssh_input')

        print PORT_RPI
        print RPI_IP

        subprocess.call(['sshpass','-p','raspberry','rsync','./ssh_output/ssh_output.rb',PORT_RPI])
    else:
        time.sleep(0.01)
        continue
