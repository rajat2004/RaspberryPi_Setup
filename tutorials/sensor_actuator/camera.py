'''
Code if using Rpi Camera version 1.0+

Not applicable for external cameras (Logitech, etc).

See /camera.sh for more.
'''

import picamera
import time

start_cam=time.clock()
CAMERA = picamera.PiCamera()
cam_ini=time.clock()


for i in range(15):
    CAMERA.capture('./input/image'+str(i)+'.jpg')
cam_fin=time.clock()

print cam_ini-start_cam
print cam_fin-cam_ini
print (cam_fin-cam_ini)/15
