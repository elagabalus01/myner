from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
class Canvas(FigureCanvasQTAgg):
    def __init__(self,fig,parent=None, width=5, height=4, dpi=100):
        super().__init__(fig)


