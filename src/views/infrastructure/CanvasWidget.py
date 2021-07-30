import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
class CanvasWidget(FigureCanvasQTAgg):
    def __init__(self,fig,parent=None, width=5, height=4, dpi=100):
        super().__init__(fig)

    def clear_axis(self,axis):
        axis.cla()
        axis.clear()

    def update_axis(self,axis):
        self.figure.canvas.draw()
        axis.figure.canvas.draw()
        axis.figure.canvas.flush_events()
        try:
            axis.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")
