from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt
class PreviewTableController():
    def set_preview_table(self):
        n_rows=10
        if self.file:
            print("Corrient")
            # Inhabilita la modificación de las celdas
            self.preview_table.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
            # #Ocualta los headers
            # self.preview_table.verticalHeader().hide()
            self.preview_table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
            n_col=len(self.datos.columns)
            self.preview_table.setColumnCount(n_col)
            self.preview_table.setRowCount(n_rows)
            # ASIGNANDO LOS DATOS EN LA TABLA
            for i in range(n_col):
                column_name=str(self.datos.columns[i])
                item=QTableWidgetItem(column_name)
                self.preview_table.setHorizontalHeaderItem(i,item)
                # print(column_name)
                for j in range(n_rows):
                    value=self.datos[column_name][j]
                    # print(value)
                    item=QTableWidgetItem(str(value))
                    self.preview_table.setItem(j,i,item)
