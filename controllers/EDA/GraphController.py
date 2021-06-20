import matplotlib
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy
from controllers.infrastructure.Canvas import Canvas
matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self,fig=Figure(),parent=None, width=5, height=4, dpi=100):
        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)
        # self.axes = self.datos.plot()
        super(MplCanvas, self).__init__(fig)

class GraphController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.histogram=None

    def set_graphics(self):
        if self.model.file:
            # axes=self.datos.plot()
            # fig=axes.figure
            self.view.graphics_vertical_layout.removeWidget(self.histogram)
            self.histogram=None
            axes=self.model.data.hist(figsize=(14,14),xrot=45)
            fig=axes[0][0].figure
            self.histogram=Canvas(fig,self.view.graficas,width=5, height=4, dpi=100)
            print("Graficando")
            self.view.graphics_vertical_layout.addWidget(self.histogram)
            # graphics.axes=self.datos.hist(figsize=(14,14),xrot=45)
        else:
            if self.histogram:
                self.view.graphics_vertical_layout.removeWidget(self.histogram)
                self.histogram.deleteLater()
                print("Ejecutando not none")
                self.histogram=None

            print("Limpiando gráfica")
            # graphics=MplCanvas(None,self.graficas,width=5, height=4, dpi=100)
