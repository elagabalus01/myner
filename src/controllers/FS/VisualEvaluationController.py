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
        view.graph.clear_axis(view.axe)
        view.axe.set_title('Gráfico de dispersión')
        view.axe.set_xlabel(x_label)
        view.axe.set_ylabel(y_label)
        sns.scatterplot(ax=view.axe,x=x_label,y=y_label,
            data=self.model.data, hue=var_dep)
        view.graph.update_axis(view.axe)

    def set_model(self):
        self.view.eje_x_box.clear()
        self.view.eje_y_box.clear()
        self.view.dependiente_box.clear()
        dependiente=set()
        merge_no_repit=lambda x,y:set(x).union(y)

        for feature in merge_no_repit(self.model.objects,self.model.numeric_columns()):
            self.view.dependiente_box.addItem(feature)

        for feature in self.model.numeric_columns():
            self.view.eje_x_box.addItem(feature)
            self.view.eje_y_box.addItem(feature)

        self.plot()
