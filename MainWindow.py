# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main-window.ui'
# Created by: PyQt5 UI code generator 5.10.1
# WARNING! All changes made in this file will be lost!
import sys
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from AddStudentWindow import AddStudentWindow
from MainUI import Ui_MainWindow
from facerecognition import trainall, predictall
from sqlite3utils import connect
import sqlite3utils

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        subject=[]
        self.login_window = None
        self.show()
        self.bind_events()

    def bind_events(self):
        self.ui.pushAdd.clicked.connect(self.show_add_student_window)
        self.ui.pushrecognize.clicked.connect(self.recognize_face)

    def show_add_student_window(self):
        self.ui.pushrecognize.hide()
        self.ui.pushAdd.hide()
        self.add_student_window = AddStudentWindow()
        self.ui.mdiArea.addSubWindow(self.add_student_window)
        self.add_student_window.show()
        self.show()

    def recognize_face(self):
        self.ui.pushrecognize.hide()
        self.ui.pushAdd.hide()
        db = connect()
        c = db.cursor()
        students = sqlite3utils.get_students(c)
        names = {}
        for id, name in list(students):
            names[id] = name

        trainall()
        self.endcapture = False
        predictall(self.finishrecognize, names)

    def finishrecognize(self):
        return self.endcapture

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
