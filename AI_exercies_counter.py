import cv2 
import numpy as np 
import mediapipe as mp
import math
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

def getAngle(a, b, c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

cap=cv2.VideoCapture('trainvd/8.mp4')
cap.set(3,480)
cap.set(4,640)
color =(255,0,0)
counter = 0 
stage = None


while True :
   isopen ,frame = cap.read()
   frame=cv2.resize(frame,(640,480))
   imgRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
   results = pose.process(imgRGB)
   lanmark=[]
   if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lanmark.append([id, cx, cy])
        '''mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS,
                             mpDraw.DrawingSpec((255,0,255),2,2),
                              mpDraw.DrawingSpec((0,0,255),2,2))'''
        if lanmark!=0:
            try:
                x1,y1=lanmark[15][1],lanmark[15][2]
                x2,y2=lanmark[11][1],lanmark[11][2]
                x3,y3=lanmark[13][1],lanmark[13][2]
                
                cv2.circle(frame,(x1,y1),8,(255,0,0),cv2.FILLED)
                cv2.circle(frame,(x1,y1),14,(255,0,0),3)
                cv2.circle(frame,(x2,y2),8,(255,0,0),cv2.FILLED)
                cv2.circle(frame,(x2,y2),14,(255,0,0),3)
                cv2.circle(frame,(x3,y3),8,(255,0,0),cv2.FILLED)
                cv2.circle(frame,(x3,y3),14,(255,0,0),3)
                
                angle=getAngle((x2,y2),(x3,y3),(x1,y1))
            
                cv2.putText(frame,f'{int(angle)}',(x3+8,y3),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
              
                per=np.interp(angle,(40,160),(100,0))
                bar = np.interp(angle, (40,160), (100, 400))
                print(bar)
                if int(per)<80:
                    cv2.rectangle(frame, (0,0), (200, 80),color, cv2.FILLED)
                    cv2.putText(frame, 'Keep Up ', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255,0,0), 2)
                   
                    color=(0,255,0)
                else :
                    cv2.rectangle(frame, (0,0), (200, 80),color, cv2.FILLED)
                    cv2.putText(frame, 'Good Job !!', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0,0,255), 2)
                    color=(255,0,0)
                cv2.rectangle(frame, (600, 100), (620, 400),(255,255,0) , 3)
                cv2.rectangle(frame, (600, int(bar)), (620, 400),color, cv2.FILLED)
                cv2.putText(frame, f'{int(per)}%', (500, 50), cv2.FONT_HERSHEY_PLAIN, 4,
                    (255,0,0), 4)
        
                 # Curl counter logic
                if angle >160:
                   stage = "down"
                if angle < 30 and stage =='down':
                   stage="up"
                   counter +=1
                   print(counter)
                cv2.putText(frame,f'{int(counter)}',(25,440),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0),5)
                
            except:
                pass
   
   
  
   cv2.imshow('cam', frame )
   if cv2.waitKey(10)& 0xff==ord('q'):
       break
   
