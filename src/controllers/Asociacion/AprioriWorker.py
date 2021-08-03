from PyQt5.QtCore import pyqtSignal,QObject
from custom_apyori import apriori
class AprioriWorker(QObject):
    complete = pyqtSignal(dict)

    def __init__(self,model):
        super().__init__(parent=None)
        self.config={}
        self.model=model

    def set_config(self,config):
        self.config=config

    def calcular_apriori(self):
        data=self.model.data
        lista_datos = data.values.tolist()
        reglas = apriori(lista_datos,**self.config)
        reglas_asociacion = list(reglas)
        clean_rules=[]
        j=0
        for regla in reglas_asociacion:
            if 'nan' not in regla.items and len(regla.items)>1:
                clean_rules.append(regla)
                j=j+1
        result={
            'rules':clean_rules,
            'length':j
        }
        self.complete.emit(result)

    def calcular_clusters(self):
        self.model.calcular_clusters()
        self.model.calcular_centroides()
        self.model.set_colors()
        self.complete.emit()
