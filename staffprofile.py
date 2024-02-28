from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QLabel,
)
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from add_staff import data_staff


class StaffData(QDialog):
    def __init__(self, staff_id):
        super().__init__()
        self.setGeometry(600, 70, 800, 880)
        self.setWindowTitle("Staff Profile")
        self.staff_id = staff_id
        self.UiComponents(staff_id)

    def UiComponents(self, staff_id):
        self.staff_id = staff_id
        p = QPalette()
        gradient = QLinearGradient(0, 0, 200, 800)
        gradient.setColorAt(0.25, QColor(234, 218, 222))
        gradient.setColorAt(0.5, QColor(200, 186, 211))
        gradient.setColorAt(0.75, QColor(166, 149, 183))
        gradient.setColorAt(1.0, QColor(122, 135, 184))

        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.label = QLabel(self)
        self.label.setStyleSheet(
            "border-radius : 80px; background-color: rgba(255, 255, 255,0.3);"
        )
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
        self.pixmap = QPixmap("./images\person.png")
        self.label0.setPixmap(self.pixmap)
        self.label0.move(335, 35)
        self.label0.resize(200, 200)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox2 = QLabel(self)
        self.textbox2.move(285, 245)
        self.textbox2.resize(300, 50)
        self.textbox2.setText(data_staff[staff_id].name)
        self.textbox2.setFont(QFont("Protest Riot", 12))
        self.textbox2.setStyleSheet(
            "border-radius : 25px;background-color: rgba(255,255,255,0.7) ; padding-left:30px"
        )

        self.ageBox = QLabel(self)
        self.ageBox.move(285, 325)
        self.ageBox.resize(145, 50)
        self.ageBox.setText(data_staff[staff_id].age)
        self.ageBox.setFont(QFont("Protest Riot", 12))
        self.ageBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left:30px"
        )

        self.modBox = QLabel(self)
        self.modBox.move(285, 405)
        self.modBox.resize(300, 50)
        self.modBox.setText(data_staff[staff_id].number)
        self.modBox.setFont(QFont("Protest Riot", 12))
        self.modBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left:30px"
        )

        self.mailBox = QLabel(self)
        self.mailBox.move(285, 485)
        self.mailBox.resize(300, 50)
        self.mailBox.setText(data_staff[staff_id].email)
        self.mailBox.setFont(QFont("Protest Riot", 12))
        self.mailBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left:30px"
        )

        self.gradeBox = QLabel(self)
        self.gradeBox.move(440, 325)
        self.gradeBox.resize(145, 50)
        self.gradeBox.setText(data_staff[staff_id].iid)
        self.gradeBox.setFont(QFont("Protest Riot", 12))
        self.gradeBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left:30px"
        )

        self.DepBox = QLabel(self)
        self.DepBox.move(285, 565)
        self.DepBox.resize(300, 50)
        self.DepBox.setText(data_staff[staff_id].department)
        self.DepBox.setFont(QFont("Protest Riot", 12))
        self.DepBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left:30px"
        )

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.move(285, 645)
        self.tableWidget.setFont(QFont("Protest Riot", 12))
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.resize(300, 170)
        self.tableWidget.setStyleSheet(
            "QTableWidget { border-radius : 25px ; background-color: rgba(255,255,255,0.7);padding-left:10px;padding-top:7px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Courses:"))
        self.update_table(data_staff, staff_id)

    def update_table(self, data_staff, staff_id):
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        length = len(data_staff[staff_id].courses)
        row = 0
        if data_staff[staff_id].courses != []:
            self.tableWidget.setRowCount(length)
            for i in data_staff[staff_id].courses:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(i))
                row += 1
