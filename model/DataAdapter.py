import pandas as pd
from .infrastructure.observable import Observable

class DataAdapter(Observable):
    '''
    data: Es el dataframe original generado del archivo
    clean_data: Es un dataframe con datos númericos, sin los registros
                con NaN, con las columnas filtradas
    num_cols: Lista de etiquetas de las características númericas
    str_cols: Lisa de etiquetas de las características no númericas
    objects: Lista de etiquetas de las características cualitativas
    filtered: Lista catacterísticas descartadas
    '''
    def __init__(self,filepath=None):
        super().__init__()
        self.data=None
        self.clean_data=None
        self.clean_numeric_data=None
        self.num_cols=None
        self.str_cols=None
        self.objects=None
        self.filtered=[]
        self.file=filepath
        if filepath:
            self.loadFile(filepath)

    def loadFile(self,filepath,has_header=True):
        self.file=filepath
        self.filtered=[]
        if not has_header:
            self.data=pd.read_csv(filepath,header=None)
            columns=[f'Feature {i}' for i in range(len(self.data.columns))]
            self.data.columns=columns
        else:
            self.data=pd.read_csv(filepath)
        self._classifyFeatures()
        self._limpiar_datos()

    def _limpiar_datos(self):
        self.clean_data=self.data
        if len(self.filtered)>0:
            self.clean_data=self.clean_data.drop(self.filtered,axis=1)
        self.clean_data=self.clean_data.drop(self.str_cols,axis=1)
        self.clean_numeric_data=self.clean_data.drop(self.objects,axis=1)
        self.clean_numeric_data=self.clean_numeric_data.dropna()

    def filter_columns(self,filtered:list):
        self.filtered=filtered
        self._limpiar_datos()
        self.notify_observers(msg="UPDATE")

    def _classifyFeatures(self):
        #Clasifica las características en cuantitativas, no númericas y
        # cualitativas
        str_cols=[]
        num_cols=[]
        objects=[]
        for feature in self.data.columns:
            #SUPONDO QUE NO SE PUEDEN PROCESAR OBJETOS
            if self.data[feature].dtype!='object':
                num_cols.append(feature)
            else:
                if self.data[feature].nunique() <= 10:
                    objects.append(feature)
                else:
                    str_cols.append(feature)
        self.num_cols=num_cols
        self.str_cols=str_cols
        self.objects=objects

    def numeric_columns(self):
        return self.num_cols

    def numeric_data(self):
        numeric_data=self.data
        numeric_data=numeric_data.drop(self.str_cols+self.objects,axis=1)
        numeric_data=numeric_data.dropna()
        return numeric_data
