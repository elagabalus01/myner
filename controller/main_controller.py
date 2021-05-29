from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QFileDialog,
    QTableWidgetItem
)
from PyQt5 import QtCore
from views import Ui_main_window
# from .analisis_exploratorio.preview_table import PreviewTableController
from .analisis_exploratorio import AnalisisExploratorioController
from .menu_controller import MenuController
from model import getDataFrame
class Window(QMainWindow, Ui_main_window,AnalisisExploratorioController,
    MenuController):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.file="data.csv"
        self.file=None
        if self.file:
            self.datos=getDataFrame(self.file)
        else:
            self.datos=None
        self.setupUi(self)
        self.set_file_menu()
        # self.set_preview_table()
        # self.set_struct_table()
        self.set_analisis_exploratorio()

    def openFile(self):
        print("Abriendo archivo")
        self.file = QFileDialog.getOpenFileName(self,
            "Abrir archivo", ".","Archivo de datos (*.csv)"
        )[0]
        self.datos=getDataFrame(self.file)
        # from test import print_detail
        # print_detail(self.file)
        self.set_analisis_exploratorio()
