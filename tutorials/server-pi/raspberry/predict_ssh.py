'''
Distributed computing based model for low power RISC device.
'''

# SSH for prediction
# In built libraries
import resize
import subprocess
import time
import os
import shutil
import pickle
import cv2

# Custom modules
import constants

# Select USB Camera
cap = cv2.VideoCapture(0)

RPI_IP,MAC_IP=constants.read_IP()

PORT='Ankivarun@'+MAC_IP+':~/Documents/Academics/IIT\ M/Projects/Smart\ DB/mac_interface/ssh_input/'
PASSWORD='1207'
PORT_OP='~/Documents/Academics/IIT\ M/Projects/Smart\ DB/mac_interface/ssh_output/'

def send_and_receive(image_path=None):
    # outputs [glass,metal,plastic,organic] confidence

    #image must be of form ./input/foo.jpg

    #Send over image
    subprocess.call(['sshpass','-p','1207','rsync',image_path,PORT])


    while True:
        if os.path.isfile('./ssh_output/ssh_output.txt'):
            time.sleep(0.1)
            break
        else:
            time.sleep(0.01)
            continue

    with open('./ssh_output/ssh_output.rb') as file:
        distance_dictionary=pickle.load(file)

    return distance_dictionary

def stream_video():

    while True:

        ret, image_np = cap.read()
        image_np=cv2.resize(image, (300, 300))
        cv2.imwrite("input/image.jpg",image_np)
        send_and_receive("input/image.jpg")


if __name__=='__main__':
    s1=time.clock()
    stream_video()
    s2=time.clock()
    print s2-s1
