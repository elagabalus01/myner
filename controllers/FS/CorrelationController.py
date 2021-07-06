import seaborn as sns
import numpy as np
class CorrelationController:
    def __init__(self,model,view):
        self.model=model
        self.view=view

    def show_heatmap(self):
        # self.ax.set_xticklabels(self.ax.get_xticklabels(), rotation = -45)
        corr=self.model.data.corr()
        #Mask oculta los valores diferente de 0 mask=matriz_inferior
        matriz_inferior=np.triu(corr) #np.tri[u|l] u=upper l=lower
        view=self.view
        view.ax.cla()
        view.ax.clear()
        heatmap=sns.heatmap(corr,ax=view.ax,cmap='RdBu_r',annot=True,
            mask=matriz_inferior)
        view.graph.figure.canvas.draw()
        try:
            view.ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")
