from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QLabel,
)
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from add_student import data_std
from add_staff import data_staff

courses_list = [[], [], [], [], [], [], [], [], [], []]
staff_list = [[], [], [], [], [], [], [], [], [], []]


class Courses(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setStyleSheet("background-color: #F9F8FD;")
        self.username = username
        self.courses_list = courses_list
        self.staff_list = staff_list
        self.UiComponents()

    def UiComponents(self):
        self.showAddedCourse("Data Structures & Algorithms", "CMP 2210", 40, 355)
        self.showAddedCourse("Database", "CMP 2242", 40, 470)
        self.showAddedCourse("Chemistry", "CHE 1241", 40, 585)
        self.showAddedCourse("Circuits", "EPE 1241", 40, 700)
        self.showAddedCourse("OOP Principles", "CMP 1242", 40, 815)

        self.showAddedCourse("Linear Algebra", "MTH 1242", 850, 355)
        self.showAddedCourse("Elctronics", "ELC 2242", 850, 470)
        self.showAddedCourse("Bio-Measurements", "SBE 2230", 850, 585)
        self.showAddedCourse("Bio-Statistics", "SBE 2240", 850, 700)
        self.showAddedCourse("Fluids & Thermo Dynamics", "MEC 102", 850, 815)

        self.hello(self.username)

        # courses word label
        courses_label = QLabel(self)
        courses_label.setText("Courses")
        courses_label.setFont(QFont("Protest Riot", 25))
        courses_label.setStyleSheet(
            "color: rgba(63,71,105); background-color:transparent"
        )
        courses_label.resize(500, 60)
        courses_label.move(40, 270)
        courses_label.setBold = True

        # search textbox
        searchBox = QLineEdit(self)
        searchBox.setPlaceholderText("Search")
        searchBox.setFont(QFont("Arial", 12))
        searchBox.setGeometry(1210, 95, 280, 40)
        searchBox.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; color: black; padding-left: 55px"
        )

        # search icon
        search_label = QLabel(self)
        pixmap = QPixmap("images/icons8-search-30.png")
        search_label.setPixmap(pixmap)
        search_label.move(1225, 100)
        search_label.resize(30, 30)
        search_label.setStyleSheet("background-color: transparent;")

        # number of courses
        num_label = QLabel(self)
        num_label.setText("Courses \ncompleted")
        num_label.setFont(QFont("Arial", 14))
        num_label.move(910, 160)
        num_label.resize(280, 120)
        num_label.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7;padding-left:125px;"
        )
        num10_label = QLabel(self)
        num10_label.setText("10")
        num10_label.setFont(QFont("Protest Riot", 60))
        num10_label.move(930, 160)
        num10_label.resize(120, 100)
        num10_label.setStyleSheet("background-color: transparent;")

        # courses in progress
        inprogress_label = QLabel(self)
        inprogress_label.setText("Courses \nin progress")
        inprogress_label.setFont(QFont("Arial", 14))
        inprogress_label.move(1210, 160)
        inprogress_label.resize(280, 120)
        inprogress_label.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; padding-left:125px;"
        )
        num4_label = QLabel(self)
        num4_label.setText("4")
        num4_label.setFont(QFont("Protest Riot", 60))
        num4_label.move(1250, 160)
        num4_label.resize(120, 100)
        num4_label.setStyleSheet("background-color: transparent;")

    def showAddedCourse(self, name, code, x, y):
        # rectangle of course
        course_rect = QLabel(self)
        course_rect.setStyleSheet("background-color: #F4F4FE; border-radius : 15px; ")
        course_rect.resize(640, 90)
        course_rect.move(x, y)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        course_rect.setGraphicsEffect(shadow)

        # course name
        course_name = QLabel(self)
        course_name.setText(f"{name}\n")
        course_name.setFont(QFont("Exo2", 15))
        course_name.setStyleSheet("background-color: transparent; ")
        course_name.resize(400, 50)
        course_name.move(x + 20, y + 17)
        course_name.setBold = True

        # course code
        self.course_code = QLabel(self)
        self.course_code.setText(f"{code}\n")
        self.course_code.setFont(QFont("Exo2", 10))
        self.course_code.setStyleSheet("background-color: transparent; ")
        self.course_code.resize(100, 50)
        self.course_code.move(x + 20, y + 51)

        # Add button
        self.add_btn = QPushButton(self)
        self.add_btn.setText("+")
        self.add_btn.setFont(QFont("Protest Riot", 24))
        self.add_btn.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #AA9EB4;"
            "};background-color: #EDE1F7; border-radius : 25px;padding-bottom:15px;  color:black;  "
        )
        self.add_btn.resize(50, 50)
        self.add_btn.move(x + 405, y + 20)
        self.add_btn.setCursor(Qt.PointingHandCursor)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        self.add_btn.setGraphicsEffect(shadow)

        # view course button
        view_btn = QPushButton(self)
        view_btn.setText(" View Course")
        view_btn.setFont(QFont("Exo2", 12))
        view_btn.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #393984;"
            "};background-color: #5558AC; border-radius : 10px; padding: 5px; color:white;  "
        )
        view_btn.resize(145, 50)
        view_btn.move(x + 470, y + 20)
        view_btn.setCursor(Qt.PointingHandCursor)

        match code:
            case "CMP 2210":
                self.code1 = "CMP 2210"
                view_btn.clicked.connect(self.showCourse1)
                self.add_btn.clicked.connect(self.addNewPersontoCourse1)
            case "CMP 2242":
                self.code2 = "CMP 2242"
                view_btn.clicked.connect(self.showCourse2)
                self.add_btn.clicked.connect(self.addNewPersontoCourse2)
            case "CHE 1241":
                self.code3 = "CHE 1241"
                view_btn.clicked.connect(self.showCourse3)
                self.add_btn.clicked.connect(self.addNewPersontoCourse3)
            case "EPE 1241":
                self.code4 = "EPE 1241"
                view_btn.clicked.connect(self.showCourse4)
                self.add_btn.clicked.connect(self.addNewPersontoCourse4)
            case "CMP 1242":
                self.code5 = "CMP 1242"
                view_btn.clicked.connect(self.showCourse5)
                self.add_btn.clicked.connect(self.addNewPersontoCourse5)
            case "MTH 1242":
                self.code6 = "MTH 1242"
                view_btn.clicked.connect(self.showCourse6)
                self.add_btn.clicked.connect(self.addNewPersontoCourse6)
            case "ELC 2242":
                self.code7 = "ELC 2242"
                view_btn.clicked.connect(self.showCourse7)
                self.add_btn.clicked.connect(self.addNewPersontoCourse7)
            case "SBE 2230":
                self.code8 = "SBE 2230"
                view_btn.clicked.connect(self.showCourse8)
                self.add_btn.clicked.connect(self.addNewPersontoCourse8)
            case "SBE 2240":
                self.code9 = "SBE 2240"
                view_btn.clicked.connect(self.showCourse9)
                self.add_btn.clicked.connect(self.addNewPersontoCourse9)
            case "MEC 102":
                self.code10 = "MEC 102"
                view_btn.clicked.connect(self.showCourse10)
                self.add_btn.clicked.connect(self.addNewPersontoCourse10)

    def addNewPersontoCourse1(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code1)
        self.add_new_person_window.show()

    def addNewPersontoCourse2(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code2)
        self.add_new_person_window.show()

    def addNewPersontoCourse3(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code3)
        self.add_new_person_window.show()

    def addNewPersontoCourse4(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code4)
        self.add_new_person_window.show()

    def addNewPersontoCourse5(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code5)
        self.add_new_person_window.show()

    def addNewPersontoCourse6(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code6)
        self.add_new_person_window.show()

    def addNewPersontoCourse7(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code7)
        self.add_new_person_window.show()

    def addNewPersontoCourse8(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code8)
        self.add_new_person_window.show()

    def addNewPersontoCourse9(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code9)
        self.add_new_person_window.show()

    def addNewPersontoCourse10(self):
        self.add_new_person_window = AddNewPersontoCourse(self.code10)
        self.add_new_person_window.show()

    def showCourse1(self):
        # dialog appear when button is clicked
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        # tabel contains basic info
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[0]))
        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.setStyleSheet(
            " background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        # tabel content
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Data Structures & Algorithms"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 2210"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3201"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10:00am - 12:00pm"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[0]):
            if ind != len(self.staff_list[0]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[0]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.resizeColumnsToContents()
        info_tabel.resizeRowsToContents()
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        # adding tabel to dialog
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse2(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[1]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Database"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 2242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("14200"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8:00am - 10:00am"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[1]):
            if ind != len(self.staff_list[1]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[1]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse3(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[2]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Chemistry"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CHE 1241"))
        info_tabel.setItem(2, 1, QTableWidgetItem("17102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("12:00pm - 2:00pm"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[2]):
            if ind != len(self.staff_list[2]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[2]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse4(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[3]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Circuits"))
        info_tabel.setItem(1, 1, QTableWidgetItem("EPE 1241"))
        info_tabel.setItem(2, 1, QTableWidgetItem("1125"))
        info_tabel.setItem(3, 1, QTableWidgetItem("1:30pm - 3:00pm"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[3]):
            if ind != len(self.staff_list[3]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[3]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse5(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[4]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("OOP Principles"))
        info_tabel.setItem(1, 1, QTableWidgetItem("CMP 1242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8:00am - 10:00am"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[4]):
            if ind != len(self.staff_list[4]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[4]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse6(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[5]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Linear Algebra"))
        info_tabel.setItem(1, 1, QTableWidgetItem("MTH 1242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3202"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10:15am - 11:30am"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[5]):
            if ind != len(self.staff_list[5]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[5]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse7(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[6]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Elctronics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("ELC 2242"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3201"))
        info_tabel.setItem(3, 1, QTableWidgetItem("10:30am - 12:30pm"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[6]):
            if ind != len(self.staff_list[6]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[6]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse8(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[7]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Bio-Measurements"))
        info_tabel.setItem(1, 1, QTableWidgetItem("SBE 2230"))
        info_tabel.setItem(2, 1, QTableWidgetItem("1204"))
        info_tabel.setItem(3, 1, QTableWidgetItem("12:00pm - 2:00pm"))
        professors = ""
        for ind, proff in enumerate(self.staff_list[7]):
            if ind != len(self.staff_list[7]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[7]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse9(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[8]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Bio-Statistics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("SBE 2240"))
        info_tabel.setItem(2, 1, QTableWidgetItem("3103"))
        info_tabel.setItem(3, 1, QTableWidgetItem("2:00pm - 3:30pm"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[8]):
            if ind != len(self.staff_list[8]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[8]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def showCourse10(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Course")
        dialog.resize(700, 600)
        dialog.setStyleSheet("background-color:#5558AC; margin:10px; margin-right:0px")
        info_tabel = QTableWidget(self)
        info_tabel.resize(700, 600)
        info_tabel.move(1300, 0)
        info_tabel.setColumnCount(2)
        info_tabel.setRowCount(6 + len(self.courses_list[9]))
        info_tabel.setItem(0, 0, QTableWidgetItem("Name"))
        info_tabel.setItem(1, 0, QTableWidgetItem("Code"))
        info_tabel.setItem(2, 0, QTableWidgetItem("Lecture Hall"))
        info_tabel.setItem(3, 0, QTableWidgetItem("Time"))
        info_tabel.setItem(4, 0, QTableWidgetItem("Professors"))
        stdsItem = QTableWidgetItem("Students")
        stdsItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 0, stdsItem)
        grdItem = QTableWidgetItem("Grades")
        grdItem.setFont(QFont("Protest Riot", 16))
        info_tabel.setItem(5, 1, grdItem)
        info_tabel.setItem(0, 1, QTableWidgetItem("Fluids & Thermo Dynamics"))
        info_tabel.setItem(1, 1, QTableWidgetItem("MEC 102"))
        info_tabel.setItem(2, 1, QTableWidgetItem("17102"))
        info_tabel.setItem(3, 1, QTableWidgetItem("8:00am - 9:30am"))

        professors = ""
        for ind, proff in enumerate(self.staff_list[9]):
            if ind != len(self.staff_list[9]) - 1:
                professors += str(proff) + " & "
            else:
                professors += str(proff)
        info_tabel.setItem(4, 1, QTableWidgetItem(professors))

        row = 6
        for student, grade in self.courses_list[9]:
            info_tabel.setItem(row, 0, QTableWidgetItem(student))
            info_tabel.setItem(row, 1, QTableWidgetItem(grade))
            row += 1

        info_tabel.setFont(QFont("Exo2", 14))
        info_tabel.horizontalHeader().setVisible(False)
        info_tabel.verticalHeader().setVisible(False)
        info_tabel.setShowGrid(False)
        info_tabel.horizontalHeader().setStretchLastSection(True)
        info_tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        info_tabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        info_tabel.setStyleSheet(
            "background-color: #F9F8FD ; border-radius : 15px;padding:20px;selection-background-color: #EDE1F7; selection-color: black;"
        )
        info_tabel.verticalHeader().setMinimumSectionSize(50)
        layout = QVBoxLayout()
        layout.addWidget(info_tabel)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()

    def hello(self, name):
        # hello label
        hello_label = QLabel(self)
        hello_label.resize(800, 150)
        hello_label.setStyleSheet(
            "background-color: #EDE1F7; border-radius:20px; padding-left:25px; padding-top:15px  "
        )
        hello_label.move(40, 95)
        hello_label.setText(f"Hello {name}!\n")
        hello_label.setFont(QFont("Protest Riot", 28))

        # It's good to see you again label
        label2 = QLabel(self)
        label2.resize(300, 150)
        label2.move(40, 123)
        label2.setText(" It's good to see you again.")
        label2.setFont(QFont("Protest Riot", 14))
        label2.setStyleSheet(
            "background-color: transparent; border-radius:20px; padding-left:25px;margin-top:0px ;"
        )

        # image label
        img_label = QLabel(self)
        img_label.resize(200, 210)
        img_label.move(540, 35)
        img_label.setStyleSheet(
            "background-color: transparent; margin:0px; padding:0px"
        )
        pixmap = QPixmap("images/student1.png")
        img_label.setPixmap(pixmap)


class AddNewPersontoCourse(QMainWindow):
    def __init__(self, code):
        super().__init__()
        self.course_code = code
        self.checked = None
        self.setGeometry(860, 350, 500, 250)
        self.setWindowTitle("Add")
        self.UiComponents()

    def UiComponents(self):
        p = QPalette()
        gradient = QLinearGradient(0, 0, 100, 200)
        gradient.setColorAt(0.25, QColor(234, 218, 222))
        gradient.setColorAt(0.5, QColor(200, 186, 211))
        gradient.setColorAt(0.75, QColor(166, 149, 183))
        gradient.setColorAt(1.0, QColor(122, 135, 184))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.label = QLabel(self)
        self.label.setStyleSheet(
            "border-radius : 25px; background-color: rgba(255, 255, 255,0.3);margin:30px;"
        )
        self.label.move(0, 0)
        self.label.resize(500, 250)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0, 0)
        self.label.setGraphicsEffect(shadow)

        staff_label = QLabel(self)
        staff_label.setText("Professor")
        staff_label.setFont(QFont("Protest Riot", 18))
        staff_label.setGeometry(50, 45, 200, 50)
        staff_label.setStyleSheet("background-color:transparent;")
        self.staff_box = QCheckBox(self)
        self.staff_box.move(115, 105)
        self.staff_box.resize(30, 25)
        self.staff_box.setStyleSheet("background-color:transparent;")

        student_label = QLabel(self)
        student_label.setText("Student")
        student_label.setFont(QFont("Protest Riot", 18))
        student_label.setGeometry(300, 45, 200, 50)
        student_label.setStyleSheet("background-color:transparent;")
        self.student_box = QCheckBox(self)
        self.student_box.move(335, 105)
        self.student_box.resize(30, 25)
        self.student_box.setStyleSheet("background-color:transparent;")

        self.staff_box.stateChanged.connect(self.uncheck)
        self.student_box.stateChanged.connect(self.uncheck)

        self.next_btn = QPushButton(self)
        self.next_btn.setText("next")
        self.next_btn.setFont(QFont("Protest Riot", 14))
        self.next_btn.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #212442;"
            "};background-color: rgba(63,71,105); border-radius : 15px;  color:black;margin-bottom:5px;color:white  "
        )
        self.next_btn.resize(120, 60)
        self.next_btn.move(190, 140)
        self.next_btn.setCursor(Qt.PointingHandCursor)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        self.next_btn.setGraphicsEffect(shadow)
        self.next_btn.clicked.connect(self.addNewPersontoCourse)

    def uncheck(self, state):
        if state == Qt.Checked:
            if self.sender() == self.student_box:
                self.staff_box.setChecked(False)
                self.checked = "student"
            elif self.sender() == self.staff_box:
                self.student_box.setChecked(False)
                self.checked = "professor"

    def addNewPersontoCourse(self):
        if self.checked == None:
            AddNewPersontoCourseDetails.errorDialog(self, "Please choose one!")
        else:
            self.hide()
            self.add_new_person_window = AddNewPersontoCourseDetails(
                self.checked, self.course_code
            )
            self.add_new_person_window.show()


class AddNewPersontoCourseDetails(QMainWindow):
    def __init__(self, checked, code):
        super().__init__()
        self.mycourses_list = courses_list
        self.staff_list = staff_list
        self.checked = checked
        self.course_code = code
        self.setGeometry(890, 250, 400, 550)
        if self.checked == "professor":
            self.setWindowTitle("Add Staff")
        else:
            self.setWindowTitle("Add Studnet")
        self.UiComponents()
        self.data_file = "data.xlsx"
        try:
            self.existing_data = pd.read_excel(self.data_file)
        except FileNotFoundError:
            self.existing_data = pd.DataFrame()

    def UiComponents(self):
        p = QPalette()
        gradient = QLinearGradient(0, 0, 100, 300)
        gradient.setColorAt(0.25, QColor(234, 218, 222))
        gradient.setColorAt(0.5, QColor(200, 186, 211))
        gradient.setColorAt(0.75, QColor(166, 149, 183))
        gradient.setColorAt(1.0, QColor(122, 135, 184))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.label = QLabel(self)
        self.label.setStyleSheet(
            "border-radius : 25px; background-color: rgba(255, 255, 255,0.3);margin:50px;"
        )
        self.label.move(0, 0)
        self.label.resize(400, 550)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0, 0)
        self.label.setGraphicsEffect(shadow)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(100, 110)
        self.textbox1.resize(200, 50)
        self.textbox1.setPlaceholderText("First Name")
        self.textbox1.setFont(QFont("Protest Riot", 12))
        self.textbox1.setStyleSheet(
            "border-radius : 15px ; background-color: rgba(255,255,255,0.7); padding-left: 30px"
        )

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(100, 180)
        self.textbox2.resize(200, 50)
        self.textbox2.setPlaceholderText("Last Name")
        self.textbox2.setFont(QFont("Protest Riot", 12))
        self.textbox2.setStyleSheet(
            "border-radius : 15px;background-color: rgba(255,255,255,0.7) ; padding-left: 30px"
        )

        self.idBox = QLineEdit(self)
        self.idBox.move(100, 250)
        self.idBox.resize(200, 50)
        self.idBox.setPlaceholderText("ID")
        self.idBox.setFont(QFont("Protest Riot", 12))
        self.idBox.setStyleSheet(
            "border-radius : 15px ; background-color: rgba(255,255,255,0.7); padding-left: 30px"
        )

        self.gradeBox = QLineEdit(self)
        self.gradeBox.move(100, 320)
        self.gradeBox.resize(200, 50)
        self.gradeBox.setFont(QFont("Protest Riot", 12))
        self.gradeBox.setStyleSheet(
            "border-radius : 15px ; background-color: rgba(255,255,255,0.7); padding-left: 30px"
        )
        if self.checked == "student":
            self.gradeBox.setPlaceholderText("Grade")
        else:
            self.gradeBox.setPlaceholderText("Position")

        self.btn = QPushButton(self)
        self.btn.setText("Add")
        self.btn.setFont(QFont("Protest Riot", 15))
        self.btn.resize(130, 50)
        self.btn.move(135, 410)
        self.btn.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #212442;"
            "};border-radius : 15px;background-color: rgba(63,71,105) ;color:white; bold"
        )
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.clicked.connect(self.search)

    def search(self):
        name = self.textbox1.text() + " " + self.textbox2.text()
        id = self.idBox.text()
        if self.checked == "student":
            grade = self.gradeBox.text()
        else:
            position = self.gradeBox.text()

        match self.course_code:
            case "CMP 2210":
                ind = 0
                course_name = "Data Structures & Algorithms"
            case "CMP 2242":
                ind = 1
                course_name = "Database"
            case "CHE 1241":
                ind = 2
                course_name = "Chemistry"
            case "EPE 1241":
                ind = 3
                course_name = "Circuits"
            case "CMP 1242":
                ind = 4
                course_name = "OOP Principles"
            case "MTH 1242":
                ind = 5
                course_name = "Linear Algebra"
            case "ELC 2242":
                ind = 6
                course_name = "Elctronics"
            case "SBE 2230":
                ind = 7
                course_name = "Bio-Measurements"
            case "SBE 2240":
                ind = 8
                course_name = "Bio-Statistics"
            case "MEC 102":
                ind = 9
                course_name = "Fluids & Thermo Dynamics"

        if self.checked == "student":
            if id in data_std and data_std[id].name == name:
                if (name, grade) not in self.mycourses_list[ind]:
                    data_std[id].courses.append((course_name, grade))
                    self.mycourses_list[ind].append((name, grade))
                    self.close()
                else:
                    self.close()
                    self.errorDialog(
                        f"The {self.checked} is already Added to the Course!"
                    )
            else:
                self.errorDialog(f"The {self.checked} doesn't exist!")

        else:
            if (
                id in data_staff
                and data_staff[id].name == name
                and data_staff[id].grade == position
            ):
                if name not in self.staff_list[ind]:
                    data_staff[id].courses.append(course_name)
                    self.staff_list[ind].append(name)
                    self.close()
                else:
                    self.close()
                    self.errorDialog(
                        f"The {self.checked} is already Added to the Course!"
                    )
            else:
                self.errorDialog(f"The {self.checked} doesn't exist!")

    def errorDialog(self, message):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Error")
        dialog.resize(300, 200)
        dialog.setStyleSheet("background-color:#5558AC;")

        label = QLabel(self)
        label.setText(message)
        label.setGeometry(0, 0, 300, 200)
        label.setFont(QFont("Protest Riot", 14))
        label.setStyleSheet(
            "color:black;background:#F9F8FD;margin:10px;padding:15px;border-radius:15px"
        )

        layout = QVBoxLayout()
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.exec()
        dialog.show()
