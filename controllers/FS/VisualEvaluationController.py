# import seaborn as sns
from controllers.infrastructure.Canvas import Canvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
import seaborn as sns
class VisualEvaluationController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=None
        self.graph=Canvas(Figure(),self.view)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        # create an axes object in the figure
        self.axe=self.graph.figure.add_subplot(1, 1, 1)
        #ROW-COLUM
        self.view.scroll_grid.addWidget(self.graph,1,0,1,6,Qt.AlignHCenter)
        self.bind_signals()

    def bind_signals(self):
        self.view.eje_x_box.activated.connect(self.set_graph)
        self.view.eje_y_box.activated.connect(self.set_graph)
        self.view.dependiente_box.activated.connect(self.set_graph)

    def set_graph(self,event):
        if self.model.file:
            self.plot()
    
    def plot(self):
        x_label=self.view.eje_x_box.currentText()
        y_label=self.view.eje_y_box.currentText()
        var_dep=self.view.dependiente_box.currentText()
        self.axe.clear()
        # self.axe=self.graph.figure.add_subplot(1, 1, 1)
        self.axe.set_title('Gráfico de dispersión')
        # self.axe.scatter(self.model.data[x_label],self.model.data[y_label])
        sns.scatterplot(ax=self.axe,x=x_label,y=y_label,
            data=self.model.data, hue=var_dep)
        self.axe.set_xlabel(x_label)
        self.axe.set_ylabel(y_label)
        self.graph.figure.canvas.draw()
        try:
            self.axe.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")

    def set_model(self):
        self.view.eje_x_box.clear()
        self.view.eje_y_box.clear()
        for feature in self.model.numeric_columns():
            self.view.eje_x_box.addItem(feature)
            self.view.eje_y_box.addItem(feature)
        for feature in self.model.data.columns:
            self.view.dependiente_box.addItem(feature)
        self.plot()