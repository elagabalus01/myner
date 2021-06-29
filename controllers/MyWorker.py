from PyQt5.QtCore import pyqtSignal,QObject

class MyWorker(QObject):
    complete = pyqtSignal()
    
    def __init__(self,model):
        super().__init__(parent=None)
        self.file=None
        self.model=model
    
    def set_file(self,file):
        self.file=file

    def read_file(self):
        self.model.loadFile(self.file)
        print("Terminado de leer el archivo")
        self.complete.emit()
        # self.model.notify_observers()

    