import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qt sample')
        self.resize(400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_()) # 进入程序的主循环直到exit()被调用，即运行程序
