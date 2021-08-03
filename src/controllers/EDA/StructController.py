from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt
class StructController():
    def __init__(self,model,view):
        self.model=model
        self.view=view

    def set_struct_table(self):
        if self.model.file:
            cols=self.model.data.axes[1]
            n_col=len(cols)
            self.view.estruct_table.setColumnCount(2)
            self.view.estruct_table.setRowCount(n_col)
            self.view.estruct_table.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
            # #Ocualta los headers
            self.view.estruct_table.verticalHeader().hide()

            item=QTableWidgetItem("Característica")
            self.view.estruct_table.setHorizontalHeaderItem(0,item)
            item=QTableWidgetItem("Tipo de dato")
            self.view.estruct_table.setHorizontalHeaderItem(1,item)


            for i in range(n_col):
                item=QTableWidgetItem(cols[i])
                self.view.estruct_table.setItem(i,0,item)
                item=QTableWidgetItem(str(self.model.data[cols[i]].dtype))
                self.view.estruct_table.setItem(i,1,item)
                # print(cols[i],data[cols[i]].dtype)
            header = self.view.estruct_table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
