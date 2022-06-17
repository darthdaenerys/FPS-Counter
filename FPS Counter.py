import cv2
import time

width=1280
height=720

camera=cv2.VideoCapture(0,cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
camera.set(cv2.CAP_PROP_FPS,60)

t1=time.time()
fpsfilter=30

time.sleep(.1)

while True:
    dt=time.time()-t1
    t1=time.time()  #reciprocal of dt is fps
    fpsfilter=fpsfilter*.9+(1/dt)*.1    #trust value in order to stabilize fps display
    _,frame=camera.read()
    frame[30:70,1100:1220]=(233,12,23)
    cv2.rectangle(frame,(1100,30),(1220,70),(0,255,255),2)
    cv2.putText(frame,str(int(fpsfilter))+' fps',(1105,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
    cv2.imshow('fps counter',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()