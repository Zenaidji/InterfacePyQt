import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import* 

class MainWindow(QMainWindow):
    
    
	def __init__(self):
		self.textEdit=QTextEdit()
		super().__init__()
		
	
		
	def closeEvent(self,event):
		event.ignore()	
		self.quitApp()
		
		
  
  
  
	def menu(self):
		menu=self.menuBar()
		menu2=menu.addMenu("Fichier")
  
		save=QAction(QIcon("./save.png"),"save",self)
		save.setShortcut( "Ctrl+S")
		save.setToolTip(self.tr("Save"))
		save.setStatusTip(self.tr("Save"))
  
		open=QAction(QIcon("./open.png"),"open",self)
		open.setShortcut( "Ctrl+O")
		open.setStatusTip(self.tr("Open"))
		open.setToolTip(self.tr("Open"))
  
		quite=QAction(QIcon("./quit.png"),"quite",self)
		quite.setShortcut( "Ctrl+Q")
		quite.setToolTip(self.tr("Quite"))
		quite.setStatusTip(self.tr("Quite"))
  
		menu2.addAction(save)
		menu2.addAction(open)
		menu2.addAction(quite)
  
		fileToolBar = QToolBar("File")
		fileToolBar.addAction(save)
		fileToolBar.addAction(quite)
		fileToolBar.addAction(open)
		self.addToolBar(fileToolBar)
	
		quite.triggered.connect(self.quitApp)
		open.triggered.connect(self.openFile)
		save.triggered.connect(self.saveFile)
		self.resize(400,400)
		self.show()
	

  
  
	def openFile(self):
		FdOpen=QFileDialog(self)
		Fname=FdOpen.getOpenFileName(self,"open file",".","*.html *.txt *.md")
		Qfile=QFile(Fname[0])
		Qfile.open(QIODevice.ReadWrite)
		Qtxt=QTextStream(Qfile)
		str=Qtxt.readAll()
		self.textEdit.setHtml(str)

		print(Fname[0])

     
     
     
     
	def saveFile(self):
		FdSave=QFileDialog(self)
		Fsave=FdSave.getSaveFileName(self,"save file",".","*.html *.txt ")
		Qfile=QFile(Fsave[0])
		str=self.textEdit.toHtml()
		Qtxt=QTextStream (Qfile)
		Qtxt<<str 
		print(Fsave[0])


        
	def quitApp(self):
		
		Qdialog=QMessageBox (self)
		Qdialog.setText ("êtes vous sure de fermer le fichier")
		b1=Qdialog.addButton("yes",QMessageBox.YesRole)
		b2=Qdialog.addButton("no",QMessageBox.NoRole)
		res=Qdialog.exec()
		if (Qdialog.clickedButton()==b1):
			print("quiteApp")
			quit()
		
			
  
  
  
  
  
         
         
 
	


def main(args):
    app=QApplication(args)
    win=MainWindow()
    
    win.menu()
    win.setCentralWidget(win.textEdit)
    barStatus=QStatusBar(win)
    win.statusBar()
    win.show()
    app.exec_()
	
 	


	

if __name__ == "__main__":
    
	main(sys.argv)
	print("execution du programme")
