import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton
from views.infrastructure.CanvasWidget import CanvasWidget
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

class CanvasWidgetTester(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__(None)
        self.setupUi()
        self.toggle=False
        self.bind_signals()

    def setupUi(self):
        self.resize(820, 464)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.central_widget=QWidget()
        self.central_widget.setLayout(self.gridLayout)
        self.graph=CanvasWidget(Figure())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.ax=self.graph.figure.add_subplot(1, 1, 1)
        self.toggle_btn=QPushButton('Toggle graph',self)
        self.gridLayout.addWidget(self.toggle_btn,1,0,Qt.AlignHCenter)
        self.gridLayout.addWidget(self.graph,0,0,Qt.AlignHCenter)
        self.setCentralWidget(self.central_widget)

    def bind_signals(self):
        self.toggle_btn.clicked.connect(self.toggle_graph)

    def toggle_graph(self):
        if self.toggle==False:
            self.graph.clear_axis(self.ax)
            self.ax.plot(range(0, 10),range(10,20))
            self.ax.set_xlabel("Prueba 1")
            self.graph.update_axis(self.ax)
            self.toggle=True
        else:
            countdown=list(range(-10,0))
            countdown.reverse()
            self.ax.plot(range(0, 10),countdown)
            self.ax.set_xlabel("Prueba 2")
            self.graph.clear_axis(self.ax)
            self.graph.update_axis(self.ax)
            self.toggle=False

    def run(self):
        self.show()
        sys.exit(self.app.exec())