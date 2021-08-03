import pandas as pd
from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView
from .AprioriWorker import AprioriWorker
from PyQt5.QtCore import QThread
safe_input=lambda x: round(x,4)
class AprioriController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.apriori_thread=None
        self.apriori_worker=None
        self.bind_signals()

    def bind_signals(self):
        self.view.btn_gen_reglas.clicked.connect(self.calcular)

    def set_model(self):
        self.view.rule_table.clear()
        self.view.set_table()
        self.view.rule_table.setRowCount(0)
        self.view.rule_table.resizeColumnsToContents()

    def calcular(self):
        self.view.rule_table.clear()
        self.view.btn_gen_reglas.setDisabled(True)
        self.view.set_table()
        args={
            'min_support':safe_input(self.view.soporte_in.value()),
            'min_confidence':safe_input(self.view.confianza_in.value()),
            'min_lift':safe_input(self.view.lift_in.value())
        }

        self.apriori_thread=QThread()
        self.apriori_worker=AprioriWorker(self.model)
        self.apriori_worker.set_config(args)
        self.apriori_worker.moveToThread(self.apriori_thread)

        self.apriori_worker.complete.connect(self.apriori_thread.quit)
        self.apriori_worker.complete.connect(self.apriori_worker.deleteLater)
        self.apriori_thread.finished.connect(self.apriori_thread.deleteLater)

        self.apriori_thread.started.connect(self.apriori_worker.calcular_apriori)
        self.apriori_worker.complete.connect(self.mostrar_tabla)

        self.apriori_thread.start()

    def mostrar_tabla(self,result):
        clean_rules=result['rules']
        n=result['length']
        self.view.rule_table.setRowCount(n)
        j=0
        for regla in clean_rules:
            items=[item for item in regla.items]
            stats=regla.ordered_statistics[0]
            item=QTableWidgetItem()
            item.setData(Qt.DisplayRole,"|".join(items))
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
            j=j+1
        self.view.rule_table.resizeColumnsToContents()
        self.view.rule_table.resizeRowsToContents()
        self.view.btn_gen_reglas.setDisabled(False)
