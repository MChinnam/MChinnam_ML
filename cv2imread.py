import cv2
import math
import numpy as np
from PIL import Image
from PIL import ImageDraw,ImageFont

from im2tex import imtext

font = ImageFont.truetype("/Users/fission/Downloads/Roboto/Roboto-BlackItalic.ttf", 100)
videoFile = "/Users/fission/Downloads/pexels-thirdman-5538137 (1080p).mp4"
imagesFolder = "/Users/fission/Documents/classs/"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".png"
        #cv2.imwrite(filename, frame)
        
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(frame)
        text=(imtext(im_pil))
        I1 = ImageDraw.Draw(im_pil)
        I1.text((100, 100), f"{text}", fill=(255, 0, 0),font=font)
        
        im_pil.save(filename)
        
        

# For reversing the operation:

cap.release()
