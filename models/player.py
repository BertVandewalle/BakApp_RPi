from qt_core import *
from PyQt5.QtGui import QPixmap

class Player:
    name =""
    id = ""
    pixMap = QPixmap

    def __init__(self,id,name):
        self.name = name
        self.id = id
    
   
    @property
    def image(self):
        try:
            return self._image
        except AttributeError:
            print("Player has no image")

    @image.setter
    def image(self,image):
        self._image = image




