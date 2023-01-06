import sys
from PyQt5.QtWidgets import *
from CanvasDessin import *
from PyQt5.QtGui import *
from PyQt5.QtCore import* 
from CanvasDessin import *


class Dessin (QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvasdessin=CanvasDessin()
        self.setCentralWidget(self.canvasdessin)
        self.tlbar=QToolBar("dessin")
        self.slider=QSlider(self)
        self.button= QPushButton("Effacer",self)
        self.pix=QPixmap()
        self.pix.fill(QColor(0, 0, 0))
        self.icon=QIcon(self.pix)
      
        
        
        
    
    
    def setTlbar(self):
        self.setSlider()
        color=QAction(QIcon("./color.jpg"),"color",self)
        c=QAction(self.icon,"chose",self)
        color.setToolTip(self.tr("color"))
        self.tlbar.addWidget(self.slider)
        self.tlbar.addWidget(self.button)
        self.tlbar.addAction(color)
        self.tlbar.addAction(c)
        self.addToolBar(self.tlbar)
        color.triggered.connect(self.openColorDialog)
        self.slider.valueChanged.connect(self.setSize)
        self.button.clicked.connect(self.effacer)
        
        
        
    
    
    
    def setSlider(self):
        self.slider.setMinimum(2)
        self.slider.setMaximum(80)
        self.slider.setValue(5)
        self.slider.setTickInterval(5)
        self.slider.setTickPosition(QSlider.TicksBelow)
        
   
   
   
    def effacer(self):
       self.canvasdessin.paths=[]
       self.canvasdessin.repaint()
    
       
    
    def openColorDialog(self):
        c=QColorDialog.getColor()
        self.canvasdessin.setColor(c)
    
    def setSize(self):
        w=self.slider.value()
        self.canvasdessin.setWidth(w)
    
    


def main(args):
    app=QApplication(args)
    dessin=Dessin()
    dessin.setTlbar()
    dessin.show()
    app.exec_()
    














if __name__=="__main__":
    main(sys.argv)