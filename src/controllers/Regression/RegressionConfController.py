from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QMessageBox
from .ClassifierWorker import ClassifierWorker
class RegressionConfController:
    def __init__(self,model,view,classifier):
        self.model=model
        self.view=view
        self.classifier=classifier
        self.model_thread=None
        self.classifier_worker=None
        self.bind_signals()

    def disable_user_input(self):
        self.view.btn_calcular.setDisabled(True)

    def enable_user_input(self):
        self.view.btn_calcular.setDisabled(False)

    def bind_signals(self):
        self.view.btn_calcular.pressed.connect(self.generar_modelo)
        self.view.btn_calcular.pressed.connect(self.disable_user_input)

    def generar_modelo(self):
        self.classifier.test_percentage=self.view.test_percentage.value()/100
        self.classifier.dependiente=self.view.features_box.currentText()

        self.model_thread=QThread()
        self.classifier_worker=ClassifierWorker(self.classifier)
        self.classifier_worker.moveToThread(self.model_thread)

        self.model_thread.started.connect(self.classifier_worker.generar_modelo)
        self.classifier_worker.model_created.connect(self.mostrar_mensaje)
        self.classifier_worker.model_created.connect(self.enable_user_input)

        self.classifier_worker.model_created.connect(self.model_thread.quit)
        self.classifier_worker.model_created.connect(self.classifier_worker.deleteLater)
        self.model_thread.finished.connect(self.model_thread.deleteLater)

        self.model_thread.start()

    def mostrar_mensaje(self):
        error_message=QMessageBox()
        error_message.critical(self.view,"Completado","Se terminó de calcular el modelo")
        error_message.setFixedSize(500,200)

    def set_model(self):
        self.view.features_box.clear()
        for feature in self.model.objects:
            self.view.features_box.addItem(feature)
