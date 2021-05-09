import cv2
import math
import argparse

## To get image argument from command prompt
parser= argparse.ArgumentParser()
parser.add_argument('--image')
args= parser.parse_args()


## initializing protocol buffer and model for face, age and gender
facePrototxt="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"
agePrototxt="age_deploy.prototxt"
ageModel="age_net.caffemodel"
genderPrototxt="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"

## initialize mean values, age ranges and gender classification
MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['Male','Female']

## use readNet() to load the models
faceNet=cv2.dnn.readNet(faceModel,facePrototxt)
ageNet=cv2.dnn.readNet(ageModel,agePrototxt)
genderNet=cv2.dnn.readNet(genderModel,genderPrototxt)

## preprocessing images 
## function to detect and highlight the faces
def detectFace(net, frame, conf_threshold=0.7):
    image=frame.copy()
    frameHeight=image.shape[0]
    frameWidth=image.shape[1]
    blob=cv2.dnn.blobFromImage(image, 1.0, (227, 227), [104, 117, 123], True)

    net.setInput(blob)
    detections=net.forward()
    faceCoordinates=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceCoordinates.append([x1,y1,x2,y2])
            cv2.rectangle(image, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return image,faceCoordinates

##capturing video using webcam
video=cv2.VideoCapture(args.image if args.image else 0)
padding=20
while cv2.waitKey(1)<0:
    hasFrame,frame=video.read() ## store read content
    if not hasFrame:
        cv2.waitKey()
        break

    image,faceCoordinates=detectFace(faceNet,frame)
    if not faceCoordinates:
        print("No face detected")
    
    for faceCoordinate in faceCoordinates:
        face=frame[max(0,faceCoordinate[1]-padding):
                   min(faceCoordinate[3]+padding,frame.shape[0]-1),max(0,faceCoordinate[0]-padding)
                   :min(faceCoordinate[2]+padding, frame.shape[1]-1)]
        
        blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
        
        ## predict gender
        genderNet.setInput(blob)
        genderPreds=genderNet.forward()
        gender=genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender}')
        
        ## predict age
        ageNet.setInput(blob)
        agePreds=ageNet.forward()
        age=ageList[agePreds[0].argmax()]
        print(f'Age: {age[1:-1]} years')
        
        ## put text on the display frame
        cv2.putText(image, f'{gender}, {age}', (faceCoordinate[0], faceCoordinate[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow("Detecting age and gender", image)