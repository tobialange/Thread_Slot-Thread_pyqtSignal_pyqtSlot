from MyPrinter import MyPrinter
from MyThread import MyThread

printer = MyPrinter()
printer.print_my_text("Hallo Welt")

thread = MyThread()
thread.text_to_print.connect(printer.print_my_text)
thread.start()
