# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add-student.ui'#
# Created by: PyQt5 UI code generator 5.10.1

# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_AddStudentWindow(object):
    def setupUi(self, AddStudentWindow):
        AddStudentWindow.setObjectName("AddStudentWindow")
        AddStudentWindow.resize(423, 400)
        self.centralwidget = QtWidgets.QWidget(AddStudentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 57, 16))
        self.label.resize(200,20)
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 57, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 70, 57, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 57, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 290, 57, 16))
        self.label_5.setObjectName("label_5")

        self.pushAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushAdd.setGeometry(QtCore.QRect(700, 300, 111, 32))
        self.pushAdd.setObjectName("pushAdd")
        self.pushButtonPhoto1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPhoto1.setGeometry(QtCore.QRect(10, 110, 180, 180))
        self.pushButtonPhoto1.setObjectName("pushButtonPhoto1")
        self.pushButtonPhoto2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPhoto2.setGeometry(QtCore.QRect(330, 110, 180, 180))
        self.pushButtonPhoto2.setObjectName("pushButtonPhoto2")
        self.pushButtonPhoto3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPhoto3.setGeometry(QtCore.QRect(10, 310, 180, 180))
        self.pushButtonPhoto3.setObjectName("pushButtonPhoto3")
        self.pushButtonPhoto4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPhoto4.setGeometry(QtCore.QRect(330, 310, 180, 180))
        self.pushButtonPhoto4.setObjectName("pushButtonPhoto4")
        AddStudentWindow.setWidget(self.centralwidget)

        self.retranslateUi(AddStudentWindow)
        QtCore.QMetaObject.connectSlotsByName(AddStudentWindow)

    def retranslateUi(self, AddStudentWindow):
        _translate = QtCore.QCoreApplication.translate
        AddStudentWindow.setWindowTitle(_translate("AddStudentWindow", "Add People"))
        self.label.setText(_translate("AddStudentWindow", "Name And Description"))
        self.label_2.setText(_translate("AddStudentWindow", "Image 1"))
        self.label_3.setText(_translate("AddStudentWindow", "Image 2"))
        self.label_4.setText(_translate("AddStudentWindow", "Image 3"))
        self.label_5.setText(_translate("AddStudentWindow", "Image4"))
        self.pushAdd.setText(_translate("AddStudentWindow", "Add"))
        # self.pushButtonPhoto1.setText(_translate("AddStudentWindow", "PushButton"))
        # self.pushButtonPhoto2.setText(_translate("AddStudentWindow", "PushButton"))
        # self.pushButtonPhoto3.setText(_translate("AddStudentWindow", "PushButton"))
        # self.pushButtonPhoto4.setText(_translate("AddStudentWindow", "PushButton"))
