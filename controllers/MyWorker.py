from PyQt5.QtCore import pyqtSignal,QObject

class MyWorker(QObject):
    complete = pyqtSignal()

    def __init__(self,model):
        super().__init__(parent=None)
        self.file=None
        self.has_header=True
        self.model=model

    def set_file(self,file,has_header):
        self.file=file
        self.has_header=has_header

    def read_file(self):
        self.model.loadFile(self.file,has_header=self.has_header)
        print("Terminado de leer el archivo")
        self.complete.emit()
        # self.model.notify_observers()
