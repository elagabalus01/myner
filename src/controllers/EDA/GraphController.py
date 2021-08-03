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
        ''' Muestra graficas '''
        view=self.view
        feature=self.view.features_box.currentText()
        #Graficando histograma
        view.hist.clear_axis(view.hist_ax)
        view.hist_ax.set_title(f"Histograma - {feature}")
        self.model.data[feature].hist(ax=view.hist_ax,figure=view.hist.figure
            ,xrot=45)
        view.hist.update_axis(view.hist_ax)
        #Box plot
        view.box.clear_axis(view.box_ax)
        view.box_ax.set_title(f"Diagrama de caja - {feature}")
        sns.boxplot(ax=view.box_ax,x=self.model.data[feature])
        view.box.update_axis(view.box_ax)

    def plot_objects(self):
        #Object plot
        view=self.view
        data=self.model.data
        feature=self.view.object_feature_box.currentText()
        view.obj.clear_axis(view.obj_ax)
        view.obj_ax.set_title(f"Diagrama de frecuencia {feature}")
        sns.countplot(ax=view.obj_ax,y=feature, data=data)
        view.obj.figure.tight_layout()
        view.obj.update_axis(view.obj_ax)

    def set_model(self):
        if len(self.model.num_cols)>0:
            self.view.features_box.clear()
            for feature in self.model.numeric_columns():
                self.view.features_box.addItem(feature)
            self.plot_hist_box()
            self.view.graficas.show()
        else:
            print("No tiene datos númericos")
            self.view.graficas.hide()
        if len(self.model.objects)>0:
            self.view.object_feature_box.clear()
            for feature in self.model.objects:
                self.view.object_feature_box.addItem(feature)
            self.view.object_plot.show()
            self.plot_objects()
        else:
            print("No tiene objetos")
            self.view.object_plot.hide()
