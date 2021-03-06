#!/usr/bin/python

from picamera import PiCamera
from time import sleep
import os

#set camera linkage
camera = PiCamera()
camera.rotation = 0

#time parameters
on_for = 10 # seconds
pictures_every = 2 #seconds
folder_name = "Final_Test"
label = "dayx_midnight"
secs = 0
loops = 1

#Make new directory
if not os.path.exists("./Desktop/nantucket_timelapse/" + folder_name):
    os.makedirs("./Desktop/nantucket_timelapse/" + folder_name)

#Run camera, take stills according to above
while (secs <= on_for):

    #Take Picture
    print("Taking picture number " + str(loops))
    camera.capture("./Desktop/nantucket_timelapse/" + folder_name + "/image_" + str(loops) + "_interval_" + str(pictures_every) + "_seconds_" + label + ".jpg")
  
    
    #Sleep until next picture
    sleep(pictures_every)

    #Increment variables
    loops = loops +1
    secs = secs + pictures_every

#End
print("Finished taking pictures")
