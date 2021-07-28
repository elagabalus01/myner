from .Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
class MainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)
		self.setupUi(self)
	