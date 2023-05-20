from PyQt6.QtCore import QObject, pyqtSlot


class MyPrinter(QObject):
    def __init__(self, parent=None):
        super(MyPrinter, self).__init__(parent)

    @pyqtSlot(str)
    def print_my_text(self, text):
        print("Printer: " + text)
