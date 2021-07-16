import seaborn as sns
import numpy as np
class CorrelationController:
    def __init__(self,model,view):
        self.model=model
        self.view=view

    def show_heatmap(self):
        view=self.view
        corr=self.model.data.corr()
        matriz_inferior=np.triu(corr)
        view.graph.clear_axis(view.ax)
        heatmap=sns.heatmap(corr,cbar=False,ax=view.ax,cmap='RdBu_r',annot=True,
            mask=matriz_inferior)
        view.graph.figure.tight_layout()
        view.graph.update_axis(view.ax)
