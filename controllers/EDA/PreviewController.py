from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtCore import Qt
class PreviewController:
    def __init__(self,model,view):
        self.model=model
        self.view=view

    def set_preview_table(self):
        n_rows=10
        if self.model.file:
            print("Corrient")
            # Inhabilita la modificación de las celdas
            self.view.preview_table.setEditTriggers(
                QAbstractItemView.NoEditTriggers
            )
            # #Ocualta los headers
            # self.preview_table.verticalHeader().hide()
            self.view.preview_table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
            n_col=len(self.model.data.columns)
            self.view.preview_table.setColumnCount(n_col)
            self.view.preview_table.setRowCount(n_rows)
            # ASIGNANDO LOS DATOS EN LA TABLA
            for i in range(n_col):
                column_name=str(self.model.data.columns[i])
                item=QTableWidgetItem(column_name)
                self.view.preview_table.setHorizontalHeaderItem(i,item)
                # print(column_name)
                for j in range(n_rows):
                    value=self.model.data[column_name][j]
                    # print(value)
                    item=QTableWidgetItem(str(value))
                    self.view.preview_table.setItem(j,i,item)
