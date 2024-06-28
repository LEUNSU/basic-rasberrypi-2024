import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./test01.ui") [0]

# WindowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self): # 생성자, 첫번째 인자는 self
		super().__init__() # 부모 클래스 생성자 (QWidget) 
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
