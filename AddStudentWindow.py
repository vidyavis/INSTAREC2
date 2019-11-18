import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMdiSubWindow

from AddStudentUI import Ui_AddStudentWindow
from CameraHandler import CameraHandler

import sqlite3

from sqlite3utils import addstudent, connect, getallstudents


subject = []
class AddStudentWindow(QMdiSubWindow):
    def __init__(self):
        super(AddStudentWindow, self).__init__()
        self.ui = Ui_AddStudentWindow()
        self.ui.setupUi(self)

        self.bind_events()

    def bind_events(self):
        icon = self.get_icon()
        self.ui.pushButtonPhoto1.setIcon(icon)
        self.ui.pushButtonPhoto1.setIconSize(QSize(180, 180))
        self.ui.pushButtonPhoto1.clicked.connect(self.get_photo1)
        self.ui.pushButtonPhoto2.setIcon(icon)
        self.ui.pushButtonPhoto2.setIconSize(QSize(180, 180))
        self.ui.pushButtonPhoto2.clicked.connect(self.get_photo2)
        self.ui.pushButtonPhoto3.setIcon(icon)
        self.ui.pushButtonPhoto3.setIconSize(QSize(180, 180))
        self.ui.pushButtonPhoto3.clicked.connect(self.get_photo3)
        self.ui.pushButtonPhoto4.setIcon(icon)
        self.ui.pushButtonPhoto4.setIconSize(QSize(180, 180))
        self.ui.pushButtonPhoto4.clicked.connect(self.get_photo4)

        self.ui.pushAdd.clicked.connect(self.addstudent)

    def get_icon(self):
        pixmap = QPixmap("resources/download.png")
        return QIcon(pixmap)

    def get_photo1(self):
        CameraHandler.get_instance().capture('test.jpg')
        self.pixmap1 = QPixmap("test.jpg")
        self.ui.pushButtonPhoto1.setIcon(QIcon(self.pixmap1))

    def get_photo2(self):
        CameraHandler.get_instance().capture('test.jpg')
        self.pixmap2 = QPixmap("test.jpg")
        self.ui.pushButtonPhoto2.setIcon(QIcon(self.pixmap2))

    def get_photo3(self):
        CameraHandler.get_instance().capture('test.jpg')
        self.pixmap3 = QPixmap("test.jpg")
        self.ui.pushButtonPhoto3.setIcon(QIcon(self.pixmap3))

    def get_photo4(self):
        CameraHandler.get_instance().capture('test.jpg')
        self.pixmap4 = QPixmap("test.jpg")
        self.ui.pushButtonPhoto4.setIcon(QIcon(self.pixmap4))

    def addstudent(self):
        db = connect()
        c = db.cursor()

        addstudent(db,c,self.ui.lineEditName.text())

        c1 = getallstudents(db,c)

        list1 = []

        for r in c1:
            list1.append(r)

        students = filter(lambda r: r[1]==self.ui.lineEditName.text(), list1)
        student = list(students)[0]

        id = student[0]
        studentid = "s%d" % (id,)
        name=self.ui.lineEditName.text()
        subject.append(name)
        print(subject)
        c=int(len(subject))
        if not os.path.exists(os.path.join("training-data", studentid)):
            os.mkdir(os.path.join("training-data", studentid))
        self.pixmap1.save(os.path.join("training-data", studentid, "photo1.jpg"))
        self.pixmap2.save(os.path.join("training-data", studentid, "photo2.jpg"))
        self.pixmap3.save(os.path.join("training-data", studentid, "photo3.jpg"))
        self.pixmap4.save(os.path.join("training-data", studentid, "photo4.jpg"))
        self.hide()

    def photo1_clicked(self):
        print('photo')
