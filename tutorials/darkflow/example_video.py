from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/tiny-yolo-voc.cfg", "load": "tiny_yolo_voc.weights", "threshold": 0.1}

tfnet = TFNet(options)
cap = cv2.VideoCapture(0)

#colour_cat={'person':3,'tvmonitor':10}
#line_thick={}

while True:

    ret, image_np = cap.read()

    result = tfnet.return_predict(image_np)
    print(result)

    for i in result:
        topleft_coord=(i['topleft']['x'],i['topleft']['y'])
        bottomright_coord=(i['bottomright']['x'],i['bottomright']['y'])
        image_np=cv2.rectangle(image_np,topleft_coord,bottomright_coord, (0,0,255),3)#colour_cat[i['label']],line_thick[i['label']])

    cv2.imshow('object detection', cv2.resize(image_np, (800,600)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
