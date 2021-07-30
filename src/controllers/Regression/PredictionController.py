from PyQt5 import QtWidgets
from math import sqrt,floor
import numpy as np
class PredictionController:

    def __init__(self,model,view,clasifier):
        self.model=model
        self.view=view
        self.clasifier=clasifier
        self.inputs={}
        self.bind_signals()

    def bind_signals(self):
        self.view.btn_prediction.pressed.connect(self.make_prediction)

    def make_prediction(self):
        vector_entrada=[]
        for entrada in self.inputs.values():
            vector_entrada.append(entrada.value())
        print(vector_entrada)
        np.array(vector_entrada)

        result = self.clasifier.predict([vector_entrada])
        self.view.lab_prediction.setText(str(result[0]))

    def set_model(self):
        self.inputs={}
        data=self.model.clean_numeric_data
        features=data.columns
        cols=len(features)
        root=sqrt(cols)
        cols=floor(root)
        i=0
        j=0
        for feature in features:
            label=QtWidgets.QLabel(str(feature),self.view)
            feature=self.inputs[str(feature)]=QtWidgets.QSpinBox(self.view)

            self.view.entradas_grid.addWidget(label,j*2,i)
            self.view.entradas_grid.addWidget(feature,(j*2)+1,i)
            i=i+1
            if i==cols+1:
                i=0
                j=j+1

        


