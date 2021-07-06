# import seaborn as sns
import seaborn as sns
class VisualEvaluationController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.bind_signals()

    def bind_signals(self):
        self.view.eje_x_box.activated.connect(self.set_graph)
        self.view.eje_y_box.activated.connect(self.set_graph)
        self.view.dependiente_box.activated.connect(self.set_graph)

    def set_graph(self,event):
        if self.model.file:
            self.plot()

    def plot(self):
        view=self.view
        x_label=view.eje_x_box.currentText()
        y_label=view.eje_y_box.currentText()
        var_dep=view.dependiente_box.currentText()
        view.axe.clear()
        # self.axe=self.graph.figure.add_subplot(1, 1, 1)
        view.axe.set_title('Gráfico de dispersión')
        # self.axe.scatter(self.model.data[x_label],self.model.data[y_label])
        sns.scatterplot(ax=view.axe,x=x_label,y=y_label,
            data=self.model.data, hue=var_dep)
        view.axe.set_xlabel(x_label)
        view.axe.set_ylabel(y_label)
        view.graph.figure.canvas.draw()
        try:
            view.axe.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")

    def set_model(self):
        self.view.eje_x_box.clear()
        self.view.eje_y_box.clear()
        self.view.dependiente_box.clear()

        for feature in self.model.objects:
            self.view.dependiente_box.addItem(feature)

        for feature in self.model.numeric_columns():
            self.view.eje_x_box.addItem(feature)
            self.view.eje_y_box.addItem(feature)
            self.view.dependiente_box.addItem(feature)

        self.plot()
