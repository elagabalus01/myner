# import seaborn as sns
from controllers.infrastructure.Canvas import Canvas
from matplotlib.figure import Figure
class VisualEvaluationController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=None
        self.graph=Canvas(Figure())
        # create an axes object in the figure
        self.axe=self.graph.figure.add_subplot(1, 1, 1)
        #ROW-COLUM
        self.view.scroll_grid.addWidget(self.graph,1,0,1,4)
        self.bind_signals()

    def bind_signals(self):
        self.view.eje_x_box.activated.connect(self.set_graph)
        self.view.eje_y_box.activated.connect(self.set_graph)

    def set_graph(self,event):
        if self.model.file:
            self.plot()
    
    def plot(self):
        x_label=self.view.eje_x_box.currentText()
        y_label=self.view.eje_y_box.currentText()
        self.axe.remove()
        self.axe=self.graph.figure.add_subplot(1, 1, 1)
        self.axe.set_title('Gráfico de dispersión')
        self.axe.plot(self.model.data[x_label],self.model.data[y_label],'b+')
        self.axe.set_xlabel(x_label)
        self.axe.set_ylabel(y_label)
        try:
            self.axe.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")

    def set_model(self):
        self.view.eje_x_box.clear()
        self.view.eje_y_box.clear()
        for feature in self.model.data.columns:
            if self.model.data[feature].dtype!='object':
                self.view.eje_x_box.addItem(feature)
                self.view.eje_y_box.addItem(feature)
        print("Agregadas las etiquedas")
        self.plot()