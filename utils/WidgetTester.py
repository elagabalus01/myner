import sys
from controllers.kmeans import KmeansController
from controllers.EDA import EDA_Controller
from views import KmeansWidget
from views import EDA_Widget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from model import DataAdapter
class RunWidget:
    def __init__(self,widget:str):
        self.widget=widget
    def run(self):
        app = QApplication(sys.argv)
        # win=Window()
        # win.show()
        win=WidgetTester(f"{self.widget}Widget",f"{self.widget}Controller")
        win.show()
        sys.exit(app.exec())

#AGREGANDO MODULO DE K-MEANS
class WidgetTester(QMainWindow):
    def __init__(self,widget,witget_ctl):
        super().__init__(None)
        self.setupUi()
        self.model=DataAdapter('Hipoteca.csv')
        w_view=eval(widget)()
        self.w_ctl=eval(witget_ctl)(self.model,w_view)
        self.gridLayout.addWidget(w_view, 0, 0)
        self.w_ctl.notify(self.model)


    def setupUi(self):
        self.resize(820, 464)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.central_widget=QWidget()
        self.central_widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.central_widget)
        

