from controllers.infrastructure.Canvas import Canvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from PyQt5.QtWidgets import QTableWidgetItem

class ClustersController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=Canvas(Figure(figsize=(10,5)))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.ax=self.graph.figure.add_subplot(1, 2, 1)
        self.view.graph_grid.addWidget(self.graph,0,0,Qt.AlignHCenter)
        self.km=None
        self.ax_3d=self.graph.figure.add_subplot(1, 2, 2, projection='3d')
        self.colores=['red','blue','green','yellow',
                        'brown','purple','turquoise','orange',
                        'darkred','deeppink','lime','dimgray']
        self.asignar=[]
        self.centroides=None
        self.num_clusters=4
        self.view.num_clusters_in.setValue(4)
        self.bind_signals()

    def set_colors(self):
        asignar_aux=[]
        for grupo in self.km.labels_:
            asignar_aux.append(self.colores[grupo])
        self.asignar=asignar_aux

    def bind_signals(self):
        self.view.feature_x_box.activated.connect(self.plot)
        self.view.feature_y_box.activated.connect(self.plot)
        self.view.feature_z_box.activated.connect(self.plot)
        self.view.num_clusters_in.valueChanged.connect(self.set_num_clusters)

    def calcular_clusters(self):
        data=self.model.clean_data
        self.km=KMeans(n_clusters=self.num_clusters,random_state=0).fit(data)
        self.km.predict(data)

    def set_num_clusters(self,num):
        self.num_clusters=num
        self.make_clusters()

    def make_clusters(self):
        self.calcular_clusters()
        self.calcular_centroides()
        self.set_colors()
        self.set_centroides_table()
        self.plot()

    def load_model(self):
        for feature in self.model.numeric_columns():
            self.view.feature_x_box.addItem(feature)
            self.view.feature_y_box.addItem(feature)
            self.view.feature_z_box.addItem(feature)
        self.view.feature_z_box.setCurrentIndex(0)
        self.make_clusters()
    
    def calcular_centroides(self):
        data=self.model.clean_data
        self.centroides=self.km.cluster_centers_
        self.centroides=pd.DataFrame(self.centroides.round(4),
            columns=data.columns)
        self.centroides['Color']=self.colores[0:self.num_clusters]

    def plot(self):
        data=self.model.clean_data
        x=self.view.feature_x_box.currentText()
        y=self.view.feature_y_box.currentText()
        z=self.view.feature_z_box.currentText()
        self.ax.cla()
        self.ax.clear()
        self.ax.scatter(data[x],
            data[y],c=self.asignar)
        self.ax.set_title('Clusters')
        self.ax.set_xlabel(x)
        self.ax.set_ylabel(y)
        self.ax.figure.canvas.draw()
        self.ax.figure.canvas.flush_events()

        try:
            self.ax.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")

        self.ax_3d.cla()
        self.ax_3d.clear()
        self.ax_3d.scatter(data[x],
            data[y],
            data[z],
            c=self.asignar)
        self.ax_3d.scatter(self.centroides[x],
            self.centroides[y],
            self.centroides[z],
           c=self.colores[0:self.num_clusters],s=100)
        self.ax_3d.set_title('Clusters')
        self.ax_3d.set_xlabel(x)
        self.ax_3d.set_ylabel(y)
        self.ax_3d.set_zlabel(z)
        try:
            self.ax_3d.figure.canvas.draw()
            self.ax_3d.figure.canvas.flush_events()
        except AttributeError:
            print(f"{type(self.ax_3d)} no tiene figure canvas")
        try:
            self.ax_3d.redraw_in_frame()
        except AttributeError:
            print("No tenía caché")

            
    def set_centroides_table(self):
        table=self.view.centroides_table
        data=self.centroides
        cols=data.columns
        n_col=len(cols)

        table.setColumnCount(n_col)
        table.setRowCount(self.num_clusters)

        for i in range(n_col):
                column_name=str(data.columns[i])
                item=QTableWidgetItem(column_name)
                table.setHorizontalHeaderItem(i,item)
                for j in range(self.num_clusters):
                    value=data[column_name][j]
                    # print(value)
                    item=QTableWidgetItem(str(value))
                    table.setItem(j,i,item)

        header = table.horizontalHeader()

