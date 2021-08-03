from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from math import sqrt,floor
from PyQt5.QtCore import QThread
from .ClassifierWorker import ClassifierWorker

class PredictionController:

    def __init__(self,model,view,classifier):
        self.model=model
        self.view=view
        self.classifier=classifier
        self.inputs={}
        self.labels={}
        self.prediction_thread=None
        classifier_worker=None
        self.bind_signals()

    def set_dependiente(self):
        self.set_model()
        self.view.lab_variable.setText(self.classifier.dependiente)

    def disable_user_input(self):
        self.view.btn_prediction.setDisabled(True)

    def enable_user_input(self):
        self.view.btn_prediction.setDisabled(False)

    def bind_signals(self):
        self.view.btn_prediction.pressed.connect(self.make_prediction)
        # self.view.btn_prediction.pressed.connect(self.clear_layout) #TEst clear layout

    def show_prediction(self,label):
        self.view.lab_resultado.setText(label)

    def make_prediction(self):
        vector_entrada=[]
        for entrada in self.inputs.values():
            vector_entrada.append(entrada.value())

        self.classifier.vector_entrada=vector_entrada


        self.prediction_thread=QThread()
        self.classifier_worker=ClassifierWorker(self.classifier)
        self.classifier_worker.moveToThread(self.prediction_thread)

        self.prediction_thread.started.connect(self.classifier_worker.calcular_prediccion)
        self.classifier_worker.prediction_calculated.connect(self.disable_user_input)
        self.classifier_worker.prediction_calculated.connect(self.show_prediction)
        self.classifier_worker.prediction_calculated.connect(self.enable_user_input)

        self.classifier_worker.prediction_calculated.connect(self.prediction_thread.quit)
        self.classifier_worker.prediction_calculated.connect(self.classifier_worker.deleteLater)
        self.prediction_thread.finished.connect(self.prediction_thread.deleteLater)

        self.prediction_thread.start()

    def clear_layout(self):
        print("Borrando widgets")
        for widget in self.inputs.values():
            self.view.entradas_grid.removeWidget(widget)
            widget.setParent(None)
        for widget in self.labels.values():
            self.view.entradas_grid.removeWidget(widget)
            widget.setParent(None)
        self.inputs={}
        self.labels={}


    def set_model(self):
        self.clear_layout()
        self.view.lab_resultado.setText("RESULTADO")
        data=self.model.clean_numeric_data
        features=data.columns
        cols=len(features)
        root=sqrt(cols)
        cols=floor(root)
        i=0
        j=0
        features=[feature for feature in features if feature!=self.classifier.dependiente]
        for feature in features:
            label=self.labels[str(feature)]=QtWidgets.QLabel(str(feature),self.view)
            feature=self.inputs[str(feature)]=QtWidgets.QDoubleSpinBox(self.view)
            feature.setDecimals(6)
            feature.setRange(-10000000.000000,10000000.000000)
            feature.setSingleStep(0.01)
            self.view.entradas_grid.addWidget(label,j*2,i,Qt.AlignLeft)
            self.view.entradas_grid.addWidget(feature,(j*2)+1,i,Qt.AlignLeft)
            i=i+1
            if i==cols+1:
                i=0
                j=j+1
