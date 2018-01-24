
from picamera import PiCamera
from time import sleep

#set camera linkage
camera = PiCamera()
camera.rotation = 190

camera.start_preview()
sleep(500)
camera.stop_preview()
