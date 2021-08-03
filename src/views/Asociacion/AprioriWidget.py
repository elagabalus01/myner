from .Ui_AprioriWidget import Ui_AprioriWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget,QTableWidgetItem,QAbstractItemView
class AprioriWidget(QWidget,Ui_AprioriWidget):
    loaded = pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.set_table()

    def set_table(self):
        ##CONFIGURANDO TABLA
        table_headers=['Regla','Soporte','Confianza','Lift']
        for i in range(len(table_headers)):
            column_name=table_headers[i]
            item=QTableWidgetItem(column_name)
            self.rule_table.setHorizontalHeaderItem(i,item)
