from time import time
import cv2

class Camera(object):

    def __init__(self, scr = 0):
    	self.stream = cv2.VideoCapture(scr)
    	_ , self.frame = self.stream.read()


    def get_frame(self):
    	_ , self.frame = self.stream.read()
    	return self.frame