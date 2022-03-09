# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Experiment\erjinzhidaima_ui\user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from DWaterProgress import DWaterProgress
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 783)
        MainWindow.setAnimated(True)
        MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        # Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        pe  = QtGui.QPalette()
        MainWindow.setAutoFillBackground(True)
        pe.setColor(QtGui.QPalette.Window, QtCore.Qt.white)  # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        MainWindow.setPalette(pe)
        MainWindow.setWindowIcon(QIcon('images/logo.ico'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(770, 260, 311, 281))
        self.textBrowser.setObjectName("textBrowser")
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(460, 90, 181, 51))
        # self.pushButton_2.setStyleSheet("font: 14pt \"微软雅黑\";")
        # self.pushButton_2.setIconSize(QtCore.QSize(64, 64))
        # self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440, 80, 251, 71))
        self.comboBox.setStyleSheet("font: 18pt \"微软雅黑\";")
        self.comboBox.setIconSize(QtCore.QSize(64, 64))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 600, 151, 31))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 600, 151, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 590, 181, 51))
        self.pushButton_4.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.pushButton_4.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 181, 51))
        self.pushButton.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 260, 301, 281))
        self.textEdit.setObjectName("textEdit")
        self.progress = DWaterProgress(self.centralwidget)
        self.progress.setFixedSize(100, 100)
        self.progress.setGeometry(QtCore.QRect(500, 350, 120, 120))
        self.progress.setValue(0)
        self.progress.start()
        self.timer = QTimer(timeout=self.updateProgress)
        self.timer.start(50)
        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QtCore.QRect(460, 350, 201, 81))
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 90, 150, 46))
        self.pushButton_3.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.pushButton_3.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1431, 801))
        self.label_3.setText("")
        # self.label_3.setPixmap(QtGui.QPixmap("image/user.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.textBrowser.raise_()
        # self.pushButton_2.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton.raise_()
        self.textEdit.raise_()
        # self.progressBar.raise_()
        self.progress.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "user_frame"))
        self.comboBox.setItemText(0, _translate("MainWindow", "            DPCNN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "         TextRCNN"))
        self.comboBox.setItemText(2, _translate("MainWindow", "      TextRNN_Att"))
        # self.pushButton_2.setText(_translate("MainWindow", "获取训练模型"))
        self.label.setText(_translate("MainWindow", "测试进度"))
        self.label_2.setText(_translate("MainWindow", "测试结果"))
        self.pushButton_4.setText(_translate("MainWindow", "测试二进制代码段"))
        self.pushButton.setText(_translate("MainWindow", "导入代码段"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "确认"))
        # self.pushButton_2.setStyleSheet('font: 14pt \"微软雅黑\";background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_4.setStyleSheet('font: 14pt \"微软雅黑\";background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton_3.setStyleSheet('font: 14pt \"微软雅黑\";background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.pushButton.setStyleSheet('font: 14pt \"微软雅黑\";background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.textBrowser.setStyleSheet('background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.textEdit.setStyleSheet('background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')

        self.pushButton.clicked.connect(self.openfile)
        self.textEdit.append("<font color=\"#000000\" size='5'>0xe80x720x230x00x00x680xd00x4f0x00x100xe80x940x2d0x00x00x590xc3\n0x8d0x4d0xd00xe90x6a0xce0xff0xff0x8b0x540x240x80x8d0x420xc0x8b0x4a0xcc0x330xc80xe80x360xf70xff0xff0xb80x700x500x00x100xe90xb60xfe0xff0xff\n0xff0x150x500x700x00x100x680x500x500x00x100xc70x50x5c0x640x00x100xb00x110x00x100xa30x600x640x00x100xc60x50x640x640x00x100x00xe80xfd0x2c0x00x00x590xc3</font>")

        self.textBrowser.append("<font color=\"#000000\" size='5'>ATL::_dynamic_initializer_for___AtlBaseModule__\n</font>")
        self.textBrowser.append("\n")
        self.textBrowser.append("<font color=\"#FF0000\" size='5'>_WppControlCallback@16\n\n</font>")
        self.textBrowser.append("\n")
        self.textBrowser.append("<font color=\"#000000\" size='5'>ATL::_dynamic_initializer_for___AtlWinModule__\n\n</font>")
    def updateProgress(self):
        value = self.progress.value()
        if value == 100:
            self.progress.setValue(100)
        else:
            self.progress.setValue(value + 1)

    def openfile(self, Form):
        '''打开系统文件资源管理器的对应文件夹'''
        # import os
        # folder = r'D:\Experiment\test_code'
        # # 方法2：通过startfile
        # os.startfile(folder)
        dialog = QFileDialog()
        my_file_path = dialog.getOpenFileName(self, "打开文件", "/", "*.txt")
        print(my_file_path)
        f = open(my_file_path[0], "r", encoding="utf-8")
        my_data = f.read()
        f.close()
        self.textBrowser.append(my_data)



import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
