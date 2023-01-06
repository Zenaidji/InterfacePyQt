import sys
from PyQt5.QtWidgets import *
from ButtonModel import *
from PyQt5.QtGui import *
from PyQt5.QtCore import* 
class CanvasButton(QWidget):
    cursorOve=False
    DefaultCol=QColor(255, 153, 128)
    ButtonModel=ButtonModel()
    hoverCol=QColor(128, 255, 223)
    pressCol=QColor(0, 0, 255)
    
    
    def __init__(self):
      
        super().__init__()
        self. bbox=QRect(250,250,200,100)
        self.setMouseTracking(True)
          
        
    def mouseMoveEvent(self,event):
       # print("move")
        pos=event.pos()
        self.cursorOve=self.cursorOnEllipse(pos)
        if (self.cursorOve):
            self.ButtonModel.enter()
            
            
        else:
            self.ButtonModel.leave()
        self.update()
    
        
    def mousePressEvent(self,event):
        self.ButtonModel.press()
        self.update()
        
        
    def cursorOnEllipse(self, point):
        x=point.x()
        y=point.y()
        cx=self.bbox.center().x()
        cy=self.bbox.center().y()  
        px=(x-cx)**2
        py= (y-cy)**2   
  
        r=(px/10000)+(py/(2500))
        print(r)
        
        if r>1:
            return False
        else:
            return True
        
        
        
       #return self.bbox.contains(point)
        
        
    
    
    def mouseReleaseEvent(self,event):
        self.ButtonModel.release()
        self.update()
        
    def  paintEvent(self,event):
        painter=QPainter(self)
        pen=QPen(QColor(0, 0, 0))
        pen.setWidth(5)
        painter.setPen(pen)
        painter.setBrush(self.DefaultCol)
        if (self.ButtonModel.stat==self.ButtonModel.hover):     
            painter.setBrush(self.hoverCol)
        elif (self.ButtonModel.stat==self.ButtonModel.pressIn):
            painter.setBrush(self.pressCol)
 
            
        painter.drawEllipse(self.bbox)   
             





def main(args):
    app=QApplication(args)
    canvasButton=CanvasButton()
    win=QMainWindow()
    win.setCentralWidget(canvasButton)
    win.show()
    win.resize(800,600)
    app.exec_()
if __name__=="__main__":
    main(sys.argv)


