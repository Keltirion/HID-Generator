import os
import unidecode
import numpy
import cv2
import sys
from PIL import Image

# TO DO
# 1. Failed detections and errors saved to folder "Failed"
# 2. Code Refactorisation

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


class CardCreate:
    def __init__(self):
        pass

    def resize(self, photo=None, width=None, height=None, inter=cv2.INTER_AREA):
        self.photo = photo

        while True:
            with open(self.photo, 'rb') as binary_image:
                string_image = binary_image.read()
                temporary_image = numpy.fromstring(string_image, numpy.uint8)
                self.photo = cv2.imdecode(temporary_image, cv2.IMREAD_COLOR)
            if self.photo is not None:
                break

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

        face_data = cascade.detectMultiScale(photo, 1.05, 8, minSize=(30, 30))
        try:
            if face_data.all():
                size = 60
                for (x, y, w, h) in face_data:
                    face_detected = self.photo[y - size : y + h + size, x - size : x + w + size]
                    face_color = cv2.cvtColor(face_detected, cv2.COLOR_BGR2RGB)
                    face_ready = Image.fromarray(face_color)
                    self.face = face_ready
                    return self.face
                else:
                    pass
        except AttributeError:
            print('Brak twarzy!')
            self.face = None
            return self.face
