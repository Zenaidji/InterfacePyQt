import sys
from PyQt5.QtWidgets import *
from CanvasDessin import *
from PyQt5.QtGui import *
from PyQt5.QtCore import* 

class Trace():
    def __init__(self,width,color):
        self.points = []
        self.width=width
        self.color=color
        
    
    
    
