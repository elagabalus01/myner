from PyQt5 import QtCore
import time
class OWorker(QtCore.QObject):
    load_status=QtCore.pyqtSignal(str)
    def run(self):
        self.load_status.emit("START")
        time.sleep(10)
        self.load_status.emit("END")
