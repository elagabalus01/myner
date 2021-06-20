import sys
from PyQt5.QtWidgets import QApplication
from controllers import MainController
# import qdarkstyle
import QBreeze.qbreeze_resources

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(open('./QBreeze/dark.qss').read())
    #app.setStyleSheet(open('./themes/dark.css').read())

    # app.setStyleSheet(open('./StyleSheets-for-PyQt5/Ubuntu.qss').read())
    # win=Window()
    # win.show()
    win=MainController()
    win.run()
    sys.exit(app.exec())
