from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt
class PCA_Controller:
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.bind_signals()
    
    def set_model(self):
        self.view.features_box.clear()
        for feature in self.model.numeric_columns():
            #SUPONDO QUE NO SE PUEDEN PROCESAR OBJETOS
            self.view.features_box.addItem(feature)
        self.view.features_box.insertItem(0,"Ninguna")

    def bind_signals(self):
        self.view.btn_calcular.pressed.connect(self.calcular_pca)

    def calcular_pca(self):
        normalizador = StandardScaler()
        # Se quita la variable dependiente "Y"
        y=self.view.features_box.currentText()
        if y=='Ninguna':
            matriz = self.model.clean_data
        else:
            matriz = self.model.clean_data.drop([y], axis=1)
        # Filtrando propiedades nos numericas
        
        # Se calcula la media y desviación para cada dimensión
        normalizador.fit(matriz)
        # Se normalizan los datos 
        matriz_normalizada = normalizador.transform(matriz)
        #Calcula la matriz de covarianza y obtiene las distancias respecto a los eigenvectores
        num_componentes=len(matriz.columns)
        componentes = PCA(n_components=num_componentes)
        # Se obtiene los componentes
        componentes.fit(matriz_normalizada)
        #Matriz de cargas
        cargas=pd.DataFrame(abs(componentes.components_),columns=matriz.columns)
        self.set_table(self.view.cargas_table,cargas)

    def set_table(self,table,data):
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # #Ocualta los headers
        # self.preview_table.verticalHeader().hide()
        table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        n_col=len(data.columns)
        n_rows=len(data[data.columns[0]])
        table.setColumnCount(n_col)
        table.setRowCount(n_rows)
        # ASIGNANDO LOS DATOS EN LA TABLA
        for i in range(n_col):
            column_name=str(data.columns[i])
            item=QTableWidgetItem(column_name)
            table.setHorizontalHeaderItem(i,item)
            # print(column_name)
            for j in range(n_rows):
                value=data[column_name][j]
                # print(value)
                # item=QTableWidgetItem(str(value))
                item=QTableWidgetItem("{:.4f}".format(value))
                table.setItem(j,i,item)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()