import os
import unidecode
import numpy
import cv2

cascade = cv2.CascadeClassifier('./Files/haarcascade_frontalface_alt.xml')

class CardCreate():
    def __init__(self, photo):
        self.photo = photo
    
    @classmethod
    def create(self, photo):
        logopath = './Files/DOVISTA - User.jpg'        
        read = cv2.imread(self.photo, cv2.IMREAD_COLOR)
        logo = cv2.imread(logopath, cv2.IMREAD_COLOR)
        read_grayscale = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
        face = cascade.detectMultiScale(read_grayscale, 1.05, 8, minSize=(300, 350))
        try:
            if face.all():
                size = 50
                cord_x = cord_y = 10
                for (x, y, w, h) in face:
                    cv2.rectangle(read_grayscale, (x - size, y - 120), (x + w + size, y + h + size), (0, 0, 0))
                    photo_complete = read[y - 140:y + h + size, x - size:x + w + size]
                    test = cv2.resize(photo_complete, (800, 800))
                    cv2.imshow('Test', test)
                else:
                    pass            
        except AttributeError:
            message = 'No face for '


        

