from PyQt5.QtWidgets import QFileDialog
from model import getDataFrame
class MenuController:
    def set_file_menu(self):
        self.actionAbrir.triggered.connect(self.openFile)
    
