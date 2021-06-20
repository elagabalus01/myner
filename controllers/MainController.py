from views import MainWindow
from .MenuController import MenuController
# from models import DataAdapter
from model import DataAdapter
from .EDA import EDA_Controller
from .FS import FS_Controller
from views import FeatureSelectionWidget
class MainController:
    def __init__(self):
        # self.model=model
        self.view=MainWindow()

        #EXPLORATORY DATA ANALYSIS
        self.model=DataAdapter(None)
        self.eda=EDA_Controller(self.model,self.view)
        
        #AGREGANDO MODULO DE VISUAL SELECTION
        fs_view=FeatureSelectionWidget()
        self.view.tabWidget.insertTab(1,fs_view,"Selección de características")
        self.fs_ctl=FS_Controller(self.model,fs_view)

        #AGREGANDO FILE MENU CONTROLLER
        self.menu_controller=MenuController(self.view,self.model)


    def run(self):
        self.view.show()