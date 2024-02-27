from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QInputDialog,
    QApplication,
    QLabel,
)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from add_student import data_std

class StudentData(QDialog):
    def __init__(self, student_id):
        super().__init__()
        self.setGeometry(550, 50, 800, 850)
        self.setWindowTitle("Edraak")
        self.student_id = student_id
        self.UiComponents(student_id)

    def UiComponents(self, student_id):
        self.student_id = student_id
        QFontDatabase.addApplicationFont("./ProtestRiot-Regular.ttf")
        p = QPalette()
        gradient = QLinearGradient(0, 0, 200, 800)
        gradient.setColorAt(0.25, QColor(234, 218, 222))
        gradient.setColorAt(0.5, QColor(200, 186, 211))
        gradient.setColorAt(0.75, QColor(166, 149, 183))
        # gradient.setColorAt(0.75, QColor(178, 214, 205))
        gradient.setColorAt(1.0, QColor(122, 135, 184))


        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.label = QLabel(self)
        self.label.setStyleSheet(
            "border-radius : 80px; background-color: rgba(255, 255, 255,0.3);"
        )
        #self.label.move(510, 165)
        self.label.move(175, 180)
        self.label.resize(515, 655)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0, 0)
        self.label.setGraphicsEffect(shadow)

        self.label0 = QLabel(self)
        self.label0.setStyleSheet(
            "border-radius : 100px; background-color: rgba(63,71,105)"
        )
        self.pixmap = QPixmap("person.png")
        self.label0.setPixmap(self.pixmap)
        self.label0.move(335, 35)
        self.label0.resize(200, 200)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)



        self.textbox2 = QLabel(self)
        self.textbox2.move(285, 245)
        self.textbox2.resize(300, 50)
        self.textbox2.setText(data_std[student_id].name)
        self.textbox2.setFont(QFont("Protest Riot", 12))
        self.textbox2.setStyleSheet(
            "border-radius : 25px;background-color: rgba(255,255,255,0.7) ; padding-left: 65px"
        )
        #self.textbox2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ageBox = QLabel(self)
        self.ageBox.move(285, 325)
        self.ageBox.resize(145, 50)
        self.ageBox.setText(data_std[student_id].age)
        self.ageBox.setFont(QFont("Protest Riot", 12))
        self.ageBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )


        self.modBox = QLabel(self)
        self.modBox.move(285, 405)
        self.modBox.resize(300, 50)
        self.modBox.setText(data_std[student_id].number)
        self.modBox.setFont(QFont("Protest Riot", 12))
        self.modBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )


        self.mailBox = QLabel(self)
        self.mailBox.move(285, 485)
        self.mailBox.resize(300, 50)
        self.mailBox.setText(data_std[student_id].email)
        self.mailBox.setFont(QFont("Protest Riot", 12))
        self.mailBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )


        self.gradeBox = QLabel(self)
        self.gradeBox.move(440, 325)
        self.gradeBox.resize(145, 50)
        self.gradeBox.setText(data_std[student_id].iid)
        self.gradeBox.setFont(QFont("Protest Riot", 12))
        self.gradeBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.DepBox = QLabel(self)
        self.DepBox.move(285, 565)
        self.DepBox.resize(300, 50)
        self.DepBox.setText(data_std[student_id].department)
        self.DepBox.setFont(QFont("Protest Riot", 12))
        self.DepBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.classes = QLabel(self)
        self.classes.move(285, 645)
        self.classes.resize(300, 140)
        self.classes.setText("Courses")
        self.classes.setFont(QFont("Protest Riot", 12))
        self.classes.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )
        #self.classes = QLabel(self)
        #self.classes.move(285, 645)
        #self.classes.resize(300, 100)
        #self.classes.setText(data_std[student_id].courses)
        #self.classes.setFont(QFont("Protest Riot", 12))
        #self.classes.setStyleSheet(
        #    "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        #)
