import os
import unidecode
import numpy
import cv2
from PIL import Image

cascade = cv2.CascadeClassifier('./Files/haarcascade_frontalface_alt.xml')


class CardCreate:
    def __init__(self):
        pass
    
    def create(self, photo):        
        self.photo = photo

        logopath = './Files/DOVISTA - User.jpg'        
        read = cv2.imread(self.photo, cv2.IMREAD_COLOR)
        logo = cv2.imread(logopath, cv2.IMREAD_COLOR)
        read_grayscale = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
        face = cascade.detectMultiScale(read_grayscale, 1.05, 8, minSize=(300, 350))
        try:
            if face.all():
                size = 500
                cord_x = cord_y = 10
                for (x, y, w, h) in face:
                    photo_complete = read[y - size:y + h + size, x - size:x + w + size]                  
                    self.face = photo_complete
                    return self.face 
                else:
                    pass
        except AttributeError:
            message = 'No face for '
            print(message)        

