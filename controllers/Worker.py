from PyQt5 import QtCore
import time
class Worker(QtCore.QThread):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    list_of_dict_signals = QtCore.pyqtSignal(list)
    str_signal = QtCore.pyqtSignal(str)
    painting_status = QtCore.pyqtSignal(str)
    def __init__(self):
        # super(Worker, self).__init__()
        QtCore.QThread.__init__(self)
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.running=False
    def stop(self):
        self.running=False
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        if self.running:
            self.painting_status.emit("START")
            time.sleep(10)
            self.painting_status.emit("END")
            self.running=False
