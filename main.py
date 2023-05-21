from PyQt6.QtWidgets import QApplication
import sys
from MyPrinter import MyPrinter
from MyThread import MyThread

printer = MyPrinter()
printer.print_my_text("Hallo Welt")

thread = MyThread()
thread.text_to_print.connect(printer.print_my_text)
thread.start()


app = QApplication(sys.argv)
sys.exit(app.exec())
