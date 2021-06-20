from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QFileDialog,
    QTableWidgetItem
)
from PyQt5 import QtCore
from views import Ui_main_window
# from .analisis_exploratorio.preview_table import PreviewTableController
from .analisis_exploratorio import AnalisisExploratorioController,GraphicsController
from .menu_controller import MenuController
# from .Worker import Worker
from .worker_obj import OWorker
from model import getDataFrame
import time
from pandas.errors import ParserError

class Window(QMainWindow, Ui_main_window,AnalisisExploratorioController,
    MenuController,GraphicsController):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.file="data.csv"

        self.file=None
        if self.file:
            self.datos=getDataFrame(self.file)
        else:
            self.datos=None
        self.histogram=None
        self.set_file_menu()
        # self.set_preview_table()
        # self.set_struct_table()
        self.set_analisis_exploratorio()
        # self.graficas.hide()
        self.set_graphics()
        self.progress_bar.hide()

    def show_error_popup(self,message):
        self.progress_bar.hide()
        self.scroll_analisis.hide()
        self.setWindowTitle("Minería de datos")
        error_message=QMessageBox()
        error_message.critical(self,"Error",message)
        error_message.setFixedSize(500,200)

    def openFile(self):
        print("Abriendo archivo")
        self.file = QFileDialog.getOpenFileName(self,
            "Abrir archivo", ".","Archivo de datos (*.csv)"
        )[0]
        if len(self.file)>0:
            # Cambiando el titulo de la ventana
            file_name=self.file.split('/')[-1]
            self.setWindowTitle(file_name)

            self.scroll_analisis.hide()
            self.progress_bar.show()
            self.progress_bar.setProperty("value", 0)
            try:
                self.datos=getDataFrame(self.file)
            except FileNotFoundError:
                self.show_error_popup("No se ha encontrado el archivo")
                return
            except ParserError:
                self.show_error_popup("No se pudieron extraer los datos del archivo")
                return
            except PermissionError:
                self.show_error_popup("No se tienen permisos para abrir el archivo")
                return

            self.progress_bar.setProperty("value", 20)

            self.set_analisis_exploratorio()
            self.progress_bar.setProperty("value", 60)

            self.set_graphics()
            self.progress_bar.setProperty("value", 100)

            self.progress_bar.hide()
            self.scroll_analisis.show()

    def closeFile(self):
        self.file=None
        self.datos=None
        self.set_analisis_exploratorio()
        self.set_graphics()

    def exit(self):
        self.close()
