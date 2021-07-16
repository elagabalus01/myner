from views import MainWindow
from .MenuController import MenuController
# from models import DataAdapter
from model import DataAdapter
from .EDA import EDA_Controller
from views import EDA_Widget
from .FS import FS_Controller
from views import FeatureSelectionWidget
from .kmeans import KmeansController
from views import KmeansWidget
from .Asociacion import AsociacionController
from views import AprioriWidget
from views import AprioriCadenasWidget
class MainController:
    def __init__(self):
        # self.model=model
        self.view=MainWindow()
        self.model=DataAdapter(None)

        #AGREGANDO FILE MENU CONTROLLER
        self.menu_controller=MenuController(self.view,self.model)
        self.view.tabWidget.hide()

        #EXPLORATORY DATA ANALYSIS
        eda_view=EDA_Widget()
        self.view.tabWidget.insertTab(1,eda_view,"Análisis exploratorio")
        self.eda_ctl=EDA_Controller(self.model,eda_view)
        eda_view.loaded.connect(self.menu_controller.aumentar_carga)

        #AGREGANDO MODULO DE VISUAL SELECTION
        fs_view=FeatureSelectionWidget()
        self.view.tabWidget.insertTab(2,fs_view,"Selección de características")
        self.fs_ctl=FS_Controller(self.model,fs_view)
        fs_view.loaded.connect(self.menu_controller.aumentar_carga)

        #AGREGANDO MODULO DE K-MEANS
        km_view=KmeansWidget()
        self.view.tabWidget.insertTab(3,km_view,"K-means")
        self.km_ctl=KmeansController(self.model,km_view)
        km_view.loaded.connect(self.menu_controller.aumentar_carga)

        # AGREGANDO MODULO DE REGLAS DE ASOCIaCION
        ar_view=AprioriCadenasWidget()
        self.view.tabWidget.insertTab(4,ar_view,"Reglas de asocicion")
        self.ar_ctl=AsociacionController(self.model,ar_view)
        ar_view.loaded.connect(self.menu_controller.aumentar_carga)


    def run(self):
        self.view.showMaximized()
        # self.view.show()
