import os
import unidecode
import numpy
import cv2

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
        print('Robie Cos')
        try:
            if face.all():
                size = 500
                cord_x = cord_y = 10
                for (x, y, w, h) in face:
                    # cv2.rectangle(read_grayscale, (x - size, y + size), (x + w + size, y + h + size), (0, 0, 0))
                    photo_complete = read[y - size:y + h + size, x - size:x + w + size]
                    # test = cv2.resize(photo_complete, (800, 800))
                    cv2.imwrite('lalalal', photo_complete)
                    cv2.imshow('Test', photo_complete)
                else:
                    pass            
        except AttributeError:
            message = 'No face for '


        

