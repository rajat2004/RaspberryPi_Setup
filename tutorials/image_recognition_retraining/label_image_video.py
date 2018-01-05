# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Simple image classification with Inception.

Run image classification with your model.

This script is usually used with retrain.py found in this same
directory.

This program creates a graph from a saved GraphDef protocol buffer,
and runs inference on an input JPEG image. You are required
to pass in the graph file and the txt file.

It outputs human readable strings of the top 5 predictions along with
their probabilities.

Change the --image_file argument to any jpg image to compute a
classification of that image.

Example usage:
python label_image.py --graph=retrained_graph.pb
  --labels=retrained_labels.txt
  --image=flower_photos/daisy/54377391_15648e8d18.jpg

NOTE: To learn to use this file and retrain.py, please see:

https://codelabs.developers.google.com/codelabs/tensorflow-for-poets
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import numpy as np

import tensorflow as tf
import cv2

cap = cv2.VideoCapture(0)


def main(model_file,label_file):

    with tf.gfile.FastGFile(model_file, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    label_lines = [line.rstrip() for line in tf.gfile.GFile(label_file)]

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        while True:

            ret, frame_original = cap.read()

            frame = cv2.resize(frame_original, (299, 299), interpolation=cv2.INTER_CUBIC)

            #cv2.imshow('Main', frame)

            # adhere to TS graph input structure
            numpy_frame = np.asarray(frame)
            numpy_frame = cv2.normalize(numpy_frame.astype('float'), None, -0.5, .5, cv2.NORM_MINMAX)
            numpy_final = np.expand_dims(numpy_frame, axis=0)

            # Feed the image_data as input to the graph and get first prediction

            predictions = sess.run(softmax_tensor, \
                     {'Mul:0': numpy_final})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            label_top=None
            score_top=None

            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                if not label_top:
                    label_top=human_string
                    score_top=score
                    print('%s (score = %.5f)' % (human_string, score))

            label = "{}: {:.2f}%".format(label_top,score_top)

            image_data= cv2.putText(frame_original, label, (10, 25), \
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        	# show the output frame
            cv2.imshow("Frame", image_data)
            key = cv2.waitKey(1) & 0xFF
        	# if the `q` key was pressed, break from the loop
            if key == ord("q"):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    model_file="inceptionv3__retrained_graph.pb"
    #model_file="mobilenet_1.0_224_retrained_graph.pb"
    label_file="inceptionv3_retrained_labels.txt"
    #label_file="mobilenet_1.0_224_retrained_labels.txt"
    main(model_file,label_file)
