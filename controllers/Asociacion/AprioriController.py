# from custom_apyori import apriori
import pandas as pd
from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView
from apyori import apriori
class AprioriController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.bind_signals()

    def bind_signals(self):
        self.view.btn_gen_reglas.clicked.connect(self.calcular)

    def set_model(self):
        # self.calcular()
        pass
        # self.view.feature1_box.clear()
        # self.view.feature2_box.clear()
        # for feature in self.model.numeric_columns():
        #     self.view.feature1_box.addItem(feature)
        #     self.view.feature2_box.addItem(feature)

    def calcular(self):
        self.view.rule_table.clear()
        safe_input=lambda x: round(x,4)
        self.view.btn_gen_reglas.setDisabled(True)
        # soporte=safe_input(self.view.soporte_in.value())
        # confianza=safe_input(self.view.confianza_in.value())
        # lift=safe_input(self.view.lift_in.value())
        # self.view.reglas.clear()

        self.view.set_table()
        lista_datos = []
        data=self.model.data
        lista_datos = []
        print(f"Número de datos {data.shape}")
        for i in range(data.shape[0]): #Para cada transacción
            lista_datos.append([
                str(data.values[i,j])  for j in range(data.shape[1])
            ])
        # lista_datos=data.values.tolist()

        reglas = apriori(lista_datos, min_support=0.028,
        min_confidences=0.3, min_lift=1.01)
        reglas_asociacion = list(reglas)
        # clean_rules=[]
        j=0
        for i in range(len(reglas_asociacion)):
            regla=reglas_asociacion[i]
            items=[item for item in regla.items]
            if 'nan' not in regla.items and len(regla.items)>1:
                stats=regla.ordered_statistics[0]
                item=QTableWidgetItem()
                item.setData(Qt.DisplayRole,",".join(items))
                self.view.rule_table.setItem(j,0,item)
                item=QTableWidgetItem()
                item.setData(Qt.DisplayRole,safe_input(regla.support))
                self.view.rule_table.setItem(j,1,item)
                item=QTableWidgetItem()
                item.setData(Qt.DisplayRole,safe_input(stats.confidence))
                self.view.rule_table.setItem(j,2,item)
                item=QTableWidgetItem()
                item.setData(Qt.DisplayRole,safe_input(stats.lift))
                self.view.rule_table.setItem(j,3,item)
                # rule=f"{items}, Support {regla.support} confidence {stats.confidence},lift {stats.lift}"
                # clean_rules.append(rule)
                # self.view.reglas.addItem(rule)

                print(regla)
                j=j+1
        print(f"Número de reglas {j}")
        self.view.rule_table.setRowCount(j)
        self.view.rule_table.resizeColumnsToContents()
        self.view.rule_table.resizeRowsToContents()
        self.view.btn_gen_reglas.setDisabled(False)
