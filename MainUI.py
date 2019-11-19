# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 678)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 1151, 631))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushAdd.setGeometry(QtCore.QRect(700, 300, 111, 32))
        self.pushAdd.setObjectName("pushAdd")
        self.pushrecognize = QtWidgets.QPushButton(self.centralwidget)
        self.pushrecognize.setGeometry(QtCore.QRect(400, 300, 111, 32))
        self.pushrecognize.setObjectName("pushrecognize")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushAdd.setText(_translate("AddStudentWindow", "Add People"))
        self.pushrecognize.setText(_translate("AddStudentWindow", "Start "))

