# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Experiment\erjinzhidaima_ui\adminer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DWaterProgress import DWaterProgress
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox
from frame import Ui_Form
import time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 750)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1091, 761))
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("image/background.jpg"))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 200, 360, 400))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(430, 90, 251, 71))
        self.comboBox.setStyleSheet("font: 18pt \"微软雅黑\";")
        self.comboBox.setIconSize(QtCore.QSize(64, 64))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 181, 61))
        self.pushButton.setStyleSheet("font: 18pt \"微软雅黑\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 90, 181, 61))
        self.pushButton_2.setStyleSheet("font: 18pt \"微软雅黑\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 270, 341, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 610, 121, 21))
        self.label_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QtCore.QRect(440, 370, 251, 101))
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")
        self.progress = DWaterProgress(self.centralwidget)
        self.progress.setFixedSize(100, 100)
        self.progress.setGeometry(QtCore.QRect(500, 350, 120, 120))
        self.progress.setValue(0)
        self.progress.start()
        self.timer = QTimer(timeout=self.updateProgress)
        self.timer.start(50)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 610, 108, 24))
        self.label_3.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(730, 240, 311, 341))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(850, 610, 108, 24))
        self.label_4.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "admin_frame"))
        self.comboBox.setItemText(0, _translate("MainWindow", "            DPCNN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "         TextRCNN"))
        self.comboBox.setItemText(2, _translate("MainWindow", "      TextRNN_Att"))

        self.pushButton.setText(_translate("MainWindow", "导入数据集"))
        self.pushButton.setStyleSheet('font: 18pt \"微软雅黑\";background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')

        self.pushButton_2.setText(_translate("MainWindow", "超参数设置"))
        self.pushButton_2.setStyleSheet('font: 18pt \"微软雅黑\"; background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')

        self.label_2.setText(_translate("MainWindow", "训练过程损失值"))
        self.label_3.setText(_translate("MainWindow", "训练进度"))
        self.label_4.setText(_translate("MainWindow", "模型架构展示"))
        self.textBrowser.setStyleSheet('background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.textBrowser_2.setStyleSheet('background-color: rgb(245, 245, 245);border-radius: 10px; border: 2px groove gray;border-style: outset;')

        self.pushButton.clicked.connect(self.show_message)

        self.pushButton_2.clicked.connect(self.show_train_pic)



    def updateProgress(self):
        value = self.progress.value()
        if value == 100:
            self.progress.setValue(0)
        else:
            self.progress.setValue(value + 1)


    def show_message(self):
        QMessageBox.information(self.centralwidget, "tips", "<font size='8'>数据库连接成功！<br>数据集导入成功~</font>", QMessageBox.Ok)


    # def show_frame(self):
    #     main_window_2 = QtWidgets.QWidget()
    #     ui_2 = Ui_Form()
    #     ui_2.setupUi(main_window_2)
    #     main_window_2.show()
    #
    def show_train_pic(self):
        self.label_5.setPixmap(QtGui.QPixmap("images/show.jpg").scaled(self.label_5.width(), self.label_5.height()))
        self.label_5.raise_()


    # def printf(self, mes):
    #         self.textBrowser.append(mes)  # 在指定的区域显示提示信息
    #         self.cursot = self.textBrowser.textCursor()
    #         self.textBrowser.moveCursor(self.cursot.End)
    #         QtWidgets.QApplication.processEvents()
    def text_browser_show(self, mes):
        self.textBrowser.append(mes)
        my_cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(my_cursor.End)
        time.sleep(1)  # 0:00:01.156
        QtWidgets.QApplication.processEvents(QtCore.QEventLoop.AllEvents)
import sys
if __name__ == "__main__":
    mess = ['Batch#1.0 Loss 0.029193976894021034', 'Batch#11.0 Loss 0.028306826949119568','Batch#21.0 Loss 0.027743274345993996', 'Batch#31.0 Loss 0.026946524158120155','Batch#41.0 Loss 0.02675837278366089', 'Batch#51.0 Loss 0.02659144438803196', 'Batch#61.0 Loss 0.0266268253326416', 'Batch#71.0 Loss 0.02659398317337036', 'Batch#81.0 Loss 0.02664218470454216', 'Batch#91.0 Loss 0.026688430458307266','Batch#101.0 Loss 0.026684805750846863','Batch#111.0 Loss 0.02681974321603775', 'Batch#121.0 Loss 0.02694016322493553','Batch#131.0 Loss 0.026971837505698204','Batch#141.0 Loss 0.027012072503566742', 'Batch#151.0 Loss 0.027072833850979805', 'Batch#161.0 Loss 0.027135884389281273', 'Batch#171.0 Loss 0.027164345607161522', 'Batch#181.0 Loss 0.027238601818680763', 'Batch#191.0 Loss 0.027333956211805344', 'Batch#201.0 Loss 0.027402378618717194', 'Batch#211.0 Loss 0.027472248300909996', 'Batch#221.0 Loss 0.027511319145560265','Batch#231.0 Loss 0.02754528820514679','epoch : 1: E : 0.02759311906993389']
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    main_window.show()
    for i in range(len(mess)):
        ui.text_browser_show(mess[i])
        time.sleep(0.1)
    sys.exit(app.exec_())