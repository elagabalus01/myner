from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView
class MissingController():
    def __init__(self,model,view):
        self.model=model
        self.view=view

    def set_missing_table(self):
        if self.model.file:
            missed=self.model.data.isnull().sum()
            cols=self.model.data.axes[1]

            n_col=len(cols)
            self.view.setColumnCount(2)
            self.view.setRowCount(n_col)
            self.view.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
            # #Ocualta los headers
            self.view.verticalHeader().hide()

            item=QTableWidgetItem("Característica")
            self.view.setHorizontalHeaderItem(0,item)
            item=QTableWidgetItem("Número de datos")
            self.view.setHorizontalHeaderItem(1,item)

            for i in range(n_col):
                item=QTableWidgetItem(cols[i])
                self.view.setItem(i,0,item)
                item=QTableWidgetItem()
                item.setData(Qt.DisplayRole,int(missed[i]))
                self.view.setItem(i,1,item)

            header = self.view.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
