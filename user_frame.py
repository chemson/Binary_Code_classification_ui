import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import *
from user import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
class user_ui(Ui_MainWindow, QMainWindow):
    def __int__(self):
        super(user_ui, self).__int__()
        self.setupUi(self)
        self.setWindowTitle('二进制代码段分类预测')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    user_ui_frame = user_ui()
    user_ui_frame.show()
    sys.exit(app.exec_())