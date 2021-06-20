import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QFileDialog,
    QTableWidgetItem
)
from PyQt5.uic import loadUi

from prueba_2 import Ui_MainWindow
import csv
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.boton_ejecutar.clicked.connect(self.ejecutar_funcion)
    def set_data(self):
        for i in range(10):
            for j in renge(10):
                item=QTableWidgetItem(data[i][j])
                self.tableWidget.setItem(i,j,item)
    def ejecutar_funcion(self):
        open_files=QFileDialog()
        open_files.getOpenFileName(self,"Open Image", "/home/elagabalus", "Image Files (*.png *.jpg *.bmp)")
#
#     def findAndReplace(self):
#         dialog = FindReplaceDialog(self)
#         dialog.exec()
#
#     def about(self):
#         QMessageBox.about(
#             self,
#             "About Sample Editor",
#             "<p>A sample text editor app built with:</p>"
#             "<p>- PyQt</p>"
#             "<p>- Qt Designer</p>"
#             "<p>- Python</p>",
#         )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # win=QMainWindow(parent=None)
    # win2=Ui_MainWindow()
    # win2.setupUi(win)
    # # print(help(win2.pushButton_2))
    # win2.pushButton_3.clicked.connect(ejecutar_funcion)
    # # self.boton_ejecutar.clicked.connect(self.toolButton.click)
    # # win = Window()
    # win.show()
    # sys.exit(app.exec())
    win=Window()
    win.show()
    sys.exit(app.exec())
