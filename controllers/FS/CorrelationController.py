from controllers.infrastructure.Canvas import Canvas
from matplotlib.figure import Figure
import seaborn as sns
class CorrelationController:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=None
        
        #Mask oculta los valores diferente de 0 mask=matriz_inferior
    
    def show_heatmap(self):
        heatmap=sns.heatmap(self.model.data.corr(),cmap='RdBu_r',annot=True)
        self.graph=Canvas(heatmap.figure)
        # self.graph.figrue=heatmap.figure
        # self.axe=self.graph.figure.add_subplot(1, 1, 1)
        self.view.correlation_grid.addWidget(self.graph,1,0,1,2)


    