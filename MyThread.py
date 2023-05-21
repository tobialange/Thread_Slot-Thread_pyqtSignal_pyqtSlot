from PyQt6.QtCore import QThread, pyqtSignal


class MyThread(QThread):
    text_to_print = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)


    def run(self):
        counter = 0
        while counter < 5:  #True:
            self.sleep(1)
            self.text_to_print.emit("Text vom Thread")
            counter += 1
