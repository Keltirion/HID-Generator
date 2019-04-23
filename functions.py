import os
import unidecode
import numpy
import cv2


class CardCreate():
    def __init__(self):
        pass        

    def create(self, photo):
        self.photo = photo

        logopath = './Files/DOVISTA - User.jpg'

        read = cv2.imread(self.photo, cv2.IMREAD_COLOR)
        logo = cv2.imread(logopath, cv2.IMREAD_COLOR)
        read_grayscale = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)

        
        cv2.imshow('test', logo)
        cv2.waitKey(0)
        cv2.imshow('test', read_grayscale)
        
