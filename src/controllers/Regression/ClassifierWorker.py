from PyQt5.QtCore import pyqtSignal,QObject

class ClassifierWorker(QObject):
    model_created = pyqtSignal()
    prediction_calculated = pyqtSignal(str)
    def __init__(self,classifier):
        super().__init__(parent=None)
        self.classifier = classifier

    def generar_modelo(self):
        self.classifier.generar_modelo()
        self.model_created.emit()

    def calcular_prediccion(self):
        result=self.classifier.calcular_prediccion()
        self.prediction_calculated.emit(result)
