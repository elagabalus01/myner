from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QThread
from .ClusterWorker import ClusterWorker
from PyQt5.QtCore import Qt
class ClustersController():
    def __init__(self,model,view):
        self.model=model
        self.view=view
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
        view=self.view

        x=view.feature_x_box.currentText()
        y=view.feature_y_box.currentText()
        z=view.feature_z_box.currentText()
        view.graph.clear_axis(view.ax)
        view.ax.scatter(data[x],
            data[y],c=asignar)
        view.ax.set_title('Clusters')
        view.ax.set_xlabel(x)
        view.ax.set_ylabel(y)
        view.graph.update_axis(view.ax)

        view.graph.clear_axis(view.ax_3d)
        view.ax_3d.scatter(data[x],
            data[y],
            data[z],
            c=asignar)
        view.ax_3d.scatter(centroides[x],
            centroides[y],
            centroides[z],
           c=colores[0:num_clusters],s=100)
        view.ax_3d.set_title('Clusters')
        view.ax_3d.set_xlabel(x)
        view.ax_3d.set_ylabel(y)
        view.ax_3d.set_zlabel(z)
        view.graph.update_axis(view.ax_3d)


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
                    # print(type(value))
                    if type(value)==str:
                        item=QTableWidgetItem(str(value))
                    else:
                        item=QTableWidgetItem()
                        item.setData(Qt.DisplayRole,float(value))
                    table.setItem(j,i,item)

        header = table.horizontalHeader()
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
