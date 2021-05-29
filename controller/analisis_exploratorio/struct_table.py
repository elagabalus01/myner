from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt
class StructTableController():
    def set_struct_table(self):
        if self.file:
            cols=self.datos.axes[1]
            n_col=len(cols)
            self.estruct_table.setColumnCount(2)
            self.estruct_table.setRowCount(n_col)
            self.estruct_table.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
            # #Ocualta los headers
            self.estruct_table.verticalHeader().hide()

            item=QTableWidgetItem("Característica")
            self.estruct_table.setHorizontalHeaderItem(0,item)
            item=QTableWidgetItem("Tipo de dato")
            self.estruct_table.setHorizontalHeaderItem(1,item)


            for i in range(n_col):
                item=QTableWidgetItem(cols[i])
                self.estruct_table.setItem(i,0,item)
                item=QTableWidgetItem(str(self.datos[cols[i]].dtype))
                self.estruct_table.setItem(i,1,item)
                # print(cols[i],data[cols[i]].dtype)
            header = self.estruct_table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
