from controllers.infrastructure.Canvas import Canvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy,QTableWidgetItem
from PyQt5.QtCore import QThread
from .ClusterWorker import ClusterWorker

class ClustersController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.graph=Canvas(Figure(figsize=(10,5)))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.graph.setSizePolicy(sizePolicy)
        self.ax=self.graph.figure.add_subplot(1, 2, 1)
        self.view.graph_grid.addWidget(self.graph,0,0,Qt.AlignHCenter)
        self.ax_3d=self.graph.figure.add_subplot(1, 2, 2, projection='3d')
        self.view.num_clusters_in.setValue(4)
        self.cluster_thread=None
        self.cluster_worker=None
        self.bind_signals()

    def bind_signals(self):
        self.view.feature_x_box.activated.connect(self.plot)
        self.view.feature_y_box.activated.connect(self.plot)
        self.view.feature_z_box.activated.connect(self.plot)
        self.view.num_clusters_in.valueChanged.connect(self.set_num_clusters)

    def set_num_clusters(self,num):
        self.model.num_clusters=num
        self.view.num_clusters_in.setDisabled(True)
        self.view.feature_x_box.setDisabled(True)
        self.view.feature_y_box.setDisabled(True)
        self.view.feature_z_box.setDisabled(True)
        self.view.scroll_clusters.verticalScrollBar().setValue(0)
        self.make_clusters()

    def enable_user_input(self):
        self.view.num_clusters_in.setDisabled(False)
        self.view.feature_x_box.setDisabled(False)
        self.view.feature_y_box.setDisabled(False)
        self.view.feature_z_box.setDisabled(False)

    def make_clusters(self):
        self.cluster_thread=QThread()
        self.cluster_worker=ClusterWorker(self.model)
        self.cluster_worker.moveToThread(self.cluster_thread)

        self.cluster_thread.started.connect(self.cluster_worker.calcular_clusters)
        self.cluster_worker.complete.connect(self.plot)
        self.cluster_worker.complete.connect(self.set_centroides_table)
        self.cluster_worker.complete.connect(self.enable_user_input)

        self.cluster_worker.complete.connect(self.cluster_thread.quit)
        self.cluster_worker.complete.connect(self.cluster_worker.deleteLater)
        self.cluster_thread.finished.connect(self.cluster_thread.deleteLater)

        self.cluster_thread.start()

    def load_model(self):
        self.view.feature_x_box.clear()
        self.view.feature_y_box.clear()
        self.view.feature_z_box.clear()

        for feature in self.model.data.columns:
            self.view.feature_x_box.addItem(feature)
            self.view.feature_y_box.addItem(feature)
            self.view.feature_z_box.addItem(feature)
        self.view.feature_z_box.setCurrentIndex(0)
        self.make_clusters()

    def plot(self):
        data=self.model.data
        asignar=self.model.asignar
        centroides=self.model.centroides
        num_clusters=self.model.num_clusters
        colores=self.model.colores

        x=self.view.feature_x_box.currentText()
        y=self.view.feature_y_box.currentText()
        z=self.view.feature_z_box.currentText()
        self.ax.cla()
        self.ax.clear()
        self.ax.scatter(data[x],
            data[y],c=asignar)
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
            c=asignar)
        self.ax_3d.scatter(centroides[x],
            centroides[y],
            centroides[z],
           c=colores[0:num_clusters],s=100)
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
        data=self.model.centroides
        cols=data.columns
        num_clusters=self.model.num_clusters
        n_col=len(cols)
        n_rows=num_clusters
        table.setColumnCount(n_col)
        table.setRowCount(n_rows)

        for i in range(n_col):
                column_name=str(data.columns[i])
                item=QTableWidgetItem(column_name)
                table.setHorizontalHeaderItem(i,item)
                for j in range(n_rows):
                    value=data[column_name][j]
                    # print(value)
                    item=QTableWidgetItem(str(value))
                    table.setItem(j,i,item)

        header = table.horizontalHeader()
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
