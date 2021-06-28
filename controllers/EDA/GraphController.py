import matplotlib
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy
from controllers.infrastructure.Canvas import Canvas
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
import seaborn as sns
matplotlib.use('Qt5Agg')

class GraphController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        #Widget de histograma
        self.hist=Canvas(Figure(figsize=(5,5)),self.view,
            width=5, height=4, dpi=100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.hist.setSizePolicy(sizePolicy)
        self.view.graph_layout.addWidget(self.hist,1,0,1,1,Qt.AlignHCenter)
        self.hist_ax=self.hist.figure.add_subplot(1, 1, 1)
        #Widget de caja de bigotes
        self.box=Canvas(Figure(figsize=(5,5)),self.view,
            width=5, height=4, dpi=100)
        self.box.setSizePolicy(sizePolicy)
        self.view.graph_layout.addWidget(self.box,1,1,1,1,Qt.AlignHCenter)
        self.box_ax=self.box.figure.add_subplot(1, 1, 1)
        #Widget de caja de objectos
        self.obj=Canvas(Figure(figsize=(7,5)),self.view,dpi=100)
        self.obj.setSizePolicy(sizePolicy)
        self.view.object_plot_grid.addWidget(self.obj,1,0,1,2,Qt.AlignHCenter)
        self.obj_ax=self.obj.figure.add_subplot(1, 1, 1)

        self.bind_signals()

    def bind_signals(self):
        self.view.features_box.activated.connect(self.plot)
        self.view.object_feature_box.activated.connect(self.plot_objects)

    def plot(self):
        ''' Muestra graficas '''
        feature=self.view.features_box.currentText()
        #Graficando histograma
        self.hist_ax.clear()
        self.hist_ax.set_title(f"Histograma - {feature}")
        self.model.data[feature].hist(ax=self.hist_ax,figure=self.hist.figure
            ,xrot=45)
        self.hist.figure.canvas.draw()
        try:
            self.hist_ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")
        #Box plot
        self.box_ax.clear()
        self.box_ax.set_title(f"Diagrama de caja - {feature}")
        sns.boxplot(x=self.model.data[feature],ax=self.box_ax)
        self.box.figure.canvas.draw()
        try:
            self.box_ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")

    def plot_objects(self):
        #Object plot
        data=self.model.data
        feature=self.view.object_feature_box.currentText()
        self.obj_ax.clear()
        self.obj_ax.set_title(f"Diagrama de frecuencia {feature}")
        sns.countplot(ax=self.obj_ax,y=feature, data=data)
        self.obj.figure.canvas.draw()
        try:
            self.obj_ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")


    def set_model(self):
        self.view.features_box.clear()
        for feature in self.model.numeric_columns():
            self.view.features_box.addItem(feature)
        self.plot()

        self.view.object_feature_box.clear()
        for feature in self.model.objects:
            self.view.object_feature_box.addItem(feature)
        if len(self.model.objects)>0:
            self.view.object_plot.show()
            self.plot_objects()
        else:
            print("No tiene objectos")
            self.view.object_plot.hide()
