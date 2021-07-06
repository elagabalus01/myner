import numpy
import seaborn as sns

class GraphController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.bind_signals()

    def bind_signals(self):
        self.view.features_box.activated.connect(self.plot_hist_box)
        self.view.object_feature_box.activated.connect(self.plot_objects)

    def plot_hist_box(self):
        view=self.view
        ''' Muestra graficas '''
        feature=self.view.features_box.currentText()
        #Graficando histograma
        view.hist_ax.clear()
        view.hist_ax.set_title(f"Histograma - {feature}")
        self.model.data[feature].hist(ax=view.hist_ax,figure=view.hist.figure
            ,xrot=45)
        view.hist.figure.canvas.draw()
        try:
            view.hist_ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")
        #Box plot
        view.box_ax.clear()
        view.box_ax.set_title(f"Diagrama de caja - {feature}")
        sns.boxplot(ax=view.box_ax,x=self.model.data[feature])
        view.box.figure.canvas.draw()
        try:
            view.box_ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")

    def plot_objects(self):
        #Object plot
        view=self.view
        data=self.model.data
        feature=self.view.object_feature_box.currentText()
        view.obj_ax.clear()
        view.obj_ax.set_title(f"Diagrama de frecuencia {feature}")
        sns.countplot(ax=view.obj_ax,y=feature, data=data)
        view.obj.figure.canvas.draw()
        try:
            view.obj_ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")


    def set_model(self):
        self.view.features_box.clear()
        for feature in self.model.numeric_columns():
            self.view.features_box.addItem(feature)
        self.plot_hist_box()

        self.view.object_feature_box.clear()
        for feature in self.model.objects:
            self.view.object_feature_box.addItem(feature)
        if len(self.model.objects)>0:
            self.view.object_plot.show()
            self.plot_objects()
        else:
            print("No tiene objectos")
            self.view.object_plot.hide()
