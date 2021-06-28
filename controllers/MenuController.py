from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QKeySequence
from model import DataAdapter
from pandas.errors import ParserError
class MenuController:
    def __init__(self,view,model):
        self.view=view
        self.bind_signals()
        self.model=model
        self.carga=0

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
        if self.carga==100:
            self.view.load_screen.hide()
            self.view.tabWidget.show()

    def openFile(self):
        print("Abriendo archivo")
        file = QFileDialog.getOpenFileName(self.view,
            "Abrir archivo", ".","Archivo de datos (*.csv)"
        )[0]
        if len(file)>0:
            self.carga=0
            self.view.tabWidget.hide()
            self.view.load_screen.show()
            # Cambiando el titulo de la ventana
            file_name=file.split('/')[-1]

            # self.setWindowTitle(file_name)

            # self.view.scroll_analisis.hide()
            # self.view.progress_bar.show()
            # self.view.progress_bar.setProperty("value", 0)
            try:
                # self.model=self.mo(file)
                self.model.loadFile(file)
                self.model.notify_observers()
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
