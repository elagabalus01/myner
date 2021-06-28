import pandas as pd
from .infrastructure.observable import Observable

class DataAdapter(Observable):
    def __init__(self,filepath=None):
        super().__init__()
        self.data=None
        self.clean_data=None
        self.num_cols=None
        self.str_cols=None
        self.objects=None
        self.file=filepath
        if filepath:
            # self.data=pd.read_csv(filepath)
            self.loadFile(filepath)


    def loadFile(self,filepath):
        self.file=filepath
        self.data=pd.read_csv(filepath)
        self.num_cols,self.str_cols,self.objects=self._num_cols()
        self._limpiar_datos()


    def _limpiar_datos(self):
        self.clean_data=self.data
        self.clean_data=self.clean_data.drop(self.str_cols,axis=1)
        self.clean_data=self.clean_data.dropna()

    def _num_cols(self):
        #Columnas numericas
        str_cols=[]
        num_cols=[]
        objects=[]
        for feature in self.data.columns:
            #SUPONDO QUE NO SE PUEDEN PROCESAR OBJETOS
            if self.data[feature].dtype!='object':
                num_cols.append(feature)
            else:
                str_cols.append(feature)
                if self.data[feature].nunique() <= 10:
                    objects.append(feature)
        return num_cols,str_cols,objects

    def numeric_columns(self):
        return self.num_cols

    def string_columns(self):
        return self.str_cols


# def getDataFrame(filepath):
#     return pd.read_csv(filepath)

# datos=pd.read_csv('data.csv')
# renglones=datos.axes[0]
# header=datos.axes[1]
# # for i in range(0,len(header)):
# #     print(header[i],type(header[i]),sep='')
# # for column in header:
# #     print(column,type(column),sep=',')
# def get_head_dtype(data):
#     cols=datos.axes[1]
#     n_col=len(cols)
#     for i in range(0,n_col):
#         print(cols[i],data[cols[i]].dtype)
