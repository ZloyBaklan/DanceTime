# coding:utf-8
# Copyright@hitzym
# video2img
# Dec,7,2017
import cv2
vc=cv2.VideoCapture("~/video.mp4")
c=1  
if vc.isOpened():  
    rval,frame=vc.read()  
else:  
    rval=False  
while rval:  
    rval,frame=vc.read()
    rows, cols, channel = frame.shape
    # frame2=cv2.resize(frame,(cols/3,rows/3),fx=0,fy=0,interpolation=cv2.INTER_AREA)
    if ( c%5 == 0):                            #every 5 fps write frame to img
        cv2.imwrite(('./yourImgPath/'+str(c)+'.jpg'),frame)
        # cropped001 = frame2[0:300,300:600]   #y change from 0 to 300 x change from 300 to 600
        # cv2.imwrite('./cropped/'+str(c)+'_001.jpg',cropped001)
    c=c+1  
    cv2.waitKey(1)  
vc.release() 
