import os
import unidecode
import numpy
import cv2
import sys
from PIL import Image

cascade = cv2.CascadeClassifier('./Files/haarcascade_frontalface_alt.xml')

class CardCreate:
    def __init__(self):
        pass
    
    def resize(self, photo, width = None, height = None, inter = cv2.INTER_AREA):
        self.photo = cv2.imread(photo, cv2.IMREAD_COLOR)

        dimension = None
        (h, w) = self.photo.shape[:2]
        if width is None and height is None:
            return self.photo
        if width is None:
            r = height / float(h)
            dimension = (int(w * r), height)
        else:
            r = width / float(w)
            dimension = (width, int(h * r))        

        self.resized_photo = cv2.resize(self.photo, dimension, interpolation=inter)
        return self.resized_photo 

    def create(self, photo):
        self.photo = photo
        photo_grey = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)                
        face_data = cascade.detectMultiScale(photo_grey, 1.05, 8, minSize=(30, 30))
        try:
            if face_data.all():
                size = 80              
                for (x, y, w, h) in face_data:
                    face_detected = self.photo[y - size : y + h + size, x - size : x + w + size]
                    face_color = cv2.cvtColor(face_detected, cv2.COLOR_BGR2RGB)
                    face_ready = Image.fromarray(face_color)
                    self.face = face_ready                                           
                    return self.face                     
                else:
                    pass
        except AttributeError:
            print('Nie ma ryja')
            self.face = None
            return self.face

               

