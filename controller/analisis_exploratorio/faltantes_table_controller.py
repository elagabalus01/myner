from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView
class FaltantesTableController():
    def set_missed_table(self):
        if self.file:
            missed=self.datos.isnull().sum()
            cols=self.datos.axes[1]

            n_col=len(cols)
            self.missed_table.setColumnCount(2)
            self.missed_table.setRowCount(n_col)
            self.missed_table.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
            # #Ocualta los headers
            self.missed_table.verticalHeader().hide()

            item=QTableWidgetItem("Característica")
            self.missed_table.setHorizontalHeaderItem(0,item)
            item=QTableWidgetItem("Número de datos")
            self.missed_table.setHorizontalHeaderItem(1,item)

            for i in range(n_col):
                item=QTableWidgetItem(cols[i])
                self.missed_table.setItem(i,0,item)
                item=QTableWidgetItem(str(missed[i]))
                self.missed_table.setItem(i,1,item)

            header = self.missed_table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
