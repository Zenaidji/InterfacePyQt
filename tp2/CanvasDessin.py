import sys
from PyQt5.QtWidgets import *
from ButtonModel import *
from PyQt5.QtGui import *
from PyQt5.QtCore import* 
from Trace import *




class CanvasDessin(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700,700)
        self.traces =[]
        self.mycolor=QColor(0,0,0)
        self.mywidth=5
        self.tr=Trace(self.mywidth,self.mycolor)  
        self.path = QPainterPath()
        self.paths=[]
       
     
   
     
        
    
    
    
    
    def setColor(self,c):
        self.mycolor=c
   
        
            
          
    def setWidth(self,w):
        self.mywidth=w
    
        
        
    
    def mousePressEvent(self, event):
        point=event.pos()
        self.tr=Trace(self.mywidth,self.mycolor)
        self. tr.points.append(point) 
        self.path=QPainterPath()
        self.path.moveTo(point) 
        self.paths.append([self.path,self.tr])
        self.update()
    
    
    
    
    def mouseMoveEvent(self, event):
         point=event.pos()
         self.tr.points.append(point)
         self.path.lineTo(point) 
         self.update()
         
    
    
         
    def mouseReleaseEvent(self,event):
        self.traces.append(self.tr)
        self.update()
    
    
 
             
        
        
        
        
    def  paintEvent(self,event):   
        pen=QPen()
        painter = QPainter(self)
        for p in self.paths:
            pen.setColor(p[1].color)
            pen.setWidth(p[1].width)
            painter.setPen(pen)
            painter.drawPath(p[0]) 
    
       
            
            
   
        
      
        

                
        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  
        
        