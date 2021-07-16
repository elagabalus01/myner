from .Ui_AprioriCadenasWidget import Ui_AprioriCadenasWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget,QTableWidgetItem,QAbstractItemView
class AprioriCadenasWidget(QWidget,Ui_AprioriCadenasWidget):
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
