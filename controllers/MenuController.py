from PyQt5.QtWidgets import QFileDialog,QMessageBox,QMessageBox
from PyQt5.QtGui import QKeySequence
from model import DataAdapter
from pandas.errors import ParserError
from .MyWorker import MyWorker
from PyQt5.QtCore import QThread
from views import LoadingScreen
class MenuController:
    def __init__(self,view,model):
        self.view=view
        self.model=model
        self.carga=0
        self.read_thread=None
        self.read_worker=None
        self.loading_screen=LoadingScreen(self.view)
        self.bind_signals()

    def bind_signals(self):
        self.view.actionAbrir.triggered.connect(self.openFile)
        self.view.actionAbrir.setShortcut(QKeySequence("Ctrl+o"))

        self.view.actionCerrar.triggered.connect(self.closeFile)
        self.view.actionCerrar.setShortcut(QKeySequence("Ctrl+w"))

        self.view.actionSalir.triggered.connect(self.exit)
        self.view.actionSalir.setShortcut(QKeySequence("Ctrl+q"))

    def aumentar_carga(self,valor):
        self.carga=self.carga+valor
        self.view.progress_bar.setProperty("value",self.carga)
        self.loading_screen.loading_bar.setProperty("value",self.carga)
        if self.carga==100:
            self.view.load_screen.hide()
            self.view.tabWidget.show()
            self.loading_screen.close()
            self.carga=0
            self.view.progress_bar.setProperty("value",self.carga)
            self.loading_screen.loading_bar.setProperty("value",self.carga)


    def openFile(self):
        file = QFileDialog.getOpenFileName(self.view,
            "Abrir archivo", "../datasets","Archivo de datos (*.csv)"
        )[0]
        has_header=QMessageBox.question(self.view,"Abrir","¿Tiene cabecera?")
        if has_header==QMessageBox.Yes:
            print("Tiene cabecera")
            has_header=True
        elif has_header==QMessageBox.No:
            print("No Tiene cabecera")
            has_header=False
        if len(file)>0:
            self.view.tabWidget.hide()
            self.view.load_screen.show()
            self.loading_screen.open()
            # Cambiando el titulo de la ventana
            file_name=file.split('/')[-1]
            try:
                print("Comenzando carga de archivo")
                self.read_thread=QThread()
                self.read_worker=MyWorker(self.model)
                self.read_worker.moveToThread(self.read_thread)
                self.read_worker.set_file(file,has_header=has_header)
                self.read_worker.complete.connect(self.read_thread.quit)
                self.read_worker.complete.connect(self.read_worker.deleteLater)
                self.read_thread.finished.connect(self.read_thread.deleteLater)

                self.read_thread.started.connect(self.read_worker.read_file)
                self.read_worker.complete.connect(self.model.notify_observers)
                self.read_thread.start()


            except FileNotFoundError:
                self.show_error_popup("No se ha encontrado el archivo")
                return
            except (ParserError,IndexError):
                self.show_error_popup("No se pudieron extraer los datos del archivo")
                return
            except PermissionError:
                self.show_error_popup("No se tienen permisos para abrir el archivo")
                return
        else:
            pass
        # PROVICIONAL EN LO QUE DECIDO POR OBSERVER O SEÑALES

            # self.view.progress_bar.setProperty("value", 20)

            # self.view.set_analisis_exploratorio()
            # self.view.progress_bar.setProperty("value", 60)

            # self.view.set_graphics()
            # self.view.progress_bar.setProperty("value", 100)

            # self.view.progress_bar.hide()
            # self.view.scroll_analisis.show()

    def closeFile(self):
        self.file=None
        self.datos=None
        # self.set_analisis_exploratorio()
        # self.set_graphics()

    def exit(self):
        self.view.close()

    # ERRORS
    def show_error_popup(self,message):
        self.model.file=None
        # self.view.progress_bar.hide()
        # self.view.scroll_analisis.hide()
        self.view.setWindowTitle("Minería de datos")
        error_message=QMessageBox()
        error_message.critical(self.view,"Error",message)
        error_message.setFixedSize(500,200)
