import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import csv

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from admin import Admin
from add_student import AddStudent

from add_student import data_std
from studentprofile import StudentData


class Students(QWidget):
    def __init__(self):
        super().__init__()
        self.UiComponents()

        self.setWindowTitle("Students ")

        self.setStyleSheet("background-color: #F9F8FD;")

    def UiComponents(self):
        # for corners
        # pinkLabel = QLabel(self)
        # pinkLabel.setStyleSheet("border-radius : 50px; background-color: white;")
        # pinkLabel.setGeometry(0, 8, 1200, 975)

        pinkLabel2 = QLabel(self)
        pinkLabel2.setStyleSheet("border-radius : 50px; background-color: #F4F4FE;")
        pinkLabel2.setGeometry(1100, 8, 550, 975)

        # student word label
        studentWordLabel = QLabel(self)
        studentWordLabel.setText("Students")
        studentWordLabel.setFont(QFont("Protest Riot", 25))
        studentWordLabel.setStyleSheet(
            "background-color: transparent; color: rgba(63,71,105);"
        )
        studentWordLabel.setGeometry(40, 40, 400, 60)
        studentWordLabel.setBold = True

        # statistic word label
        statisticWordLabel = QLabel(self)
        statisticWordLabel.setText("Statistics")
        statisticWordLabel.setFont(QFont("Protest Riot", 25))
        statisticWordLabel.setStyleSheet(
            "background-color: transparent;  color: rgba(63,71,105);"
        )
        statisticWordLabel.setGeometry(1250, 40, 400, 60)
        statisticWordLabel.setBold = True

        # # the two buttons label above
        # btLabel = QLabel(self)
        # btLabel.setStyleSheet("border-radius : 10px; background-color: #B67ADC;")
        # btLabel.setGeometry(900, 130, 105, 40)

        # self.filter = QPushButton(self)
        # self.filter.setFont(QFont("Protest Riot", 15))
        # self.filter.resize(32, 32)
        # self.filter.move(915, 135)
        # self.filter.setStyleSheet(
        #     " QPushButton::hover"
        #     "{"
        #     "background-color : #50336D;"
        #     "};border-radius : 10px;background-color:#7A51A1 ;color:white; bold"
        # )
        # self.filter.setCursor(Qt.PointingHandCursor)
        # self.icon = QIcon(
        #     "icons8-filter-50.jpg"
        # )  # Replace 'icon.png' with the path to your icon file
        # self.filter.setIcon(self.icon)
        # # self.filter.clicked(self.go_to_anotherWindow())

        # self.list = QPushButton(self)
        # self.list.setFont(QFont("Protest Riot", 15))
        # self.list.resize(32, 32)
        # self.list.move(960, 135)
        # self.list.setStyleSheet(
        #     "border-radius : 10px;background-color: #7A51A1 ;color:white; bold"
        # )
        # self.list.setCursor(Qt.PointingHandCursor)
        # self.icon = QIcon(
        #     "icons8-list-30.jpg"
        # )  # Replace 'icon.png' with the path to your icon file
        # self.list.setIcon(self.icon)

        # add student button
        self.addStudent = QPushButton(self)
        self.addStudent.setText("Add Student")
        self.addStudent.setFont(QFont("Exo2", 11))
        self.addStudent.setGeometry(910, 130, 120, 40)
        self.addStudent.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #393984;"
            "};border-radius : 10px; background-color: #5558AC; color: white;"
        )
        self.addStudent.setCursor(Qt.PointingHandCursor)
        self.addStudent.clicked.connect(self.open_add_student_window)

        # search textbox
        self.searchBox = QLineEdit(self)
        self.searchBox.setPlaceholderText("Search")
        self.searchBox.setFont(QFont("Arial", 12))
        self.searchBox.move(620, 405)
        self.searchBox.setGeometry(750, 70, 280, 40)
        self.searchBox.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; color: black; padding-left: 55px"
        )
        self.searchBox.textChanged.connect(self.filter_table)
        # search icon
        search_label = QLabel(self)
        pixmap = QPixmap("images/icons8-search-30.png")
        search_label.setPixmap(pixmap)
        search_label.move(765, 75)
        search_label.resize(30, 30)
        search_label.setStyleSheet("background-color: transparent;")

        # the table
        headertabel = QTableWidget(self)
        headertabel.setColumnCount(4)
        headertabel.setRowCount(1)
        headertabel.setItem(0, 0, QTableWidgetItem("Student ID"))
        headertabel.setItem(0, 1, QTableWidgetItem("Student Name"))
        headertabel.setItem(0, 2, QTableWidgetItem("Student Year"))
        headertabel.setItem(0, 3, QTableWidgetItem("Student Department"))
        headertabel.resizeRowToContents(4)
        headertabel.setFont(QFont("Exo2", 14))
        headertabel.setGeometry(40, 250, 1010, 46)
        headertabel.setStyleSheet(
            "QTableWidget { border: 0px; background-color: #F4F4FE; color: #536e8f; border-radius : 20px;padding-left:15px;selection-background-color: #EDE1F7; selection-color: black; }"
        )
        headertabel.horizontalHeader().setVisible(False)
        headertabel.verticalHeader().setVisible(False)
        headertabel.setShowGrid(False)
        headertabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        headertabel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        headertabel.setGraphicsEffect(shadow)

        self.tableWidget = QTableWidget(self)

        self.tableWidget.setColumnCount(4)

        # self.update_table()

        # a = Admin()
        # a.open_file_dialog()

        # i = 4
        # for row in range(4):
        #     for col in range(4):
        #         self.tableWidget.setItem(row, col, QTableWidgetItem(a.students_data[i]))
        #         i += 1

        # tableWidget.setItem(0, 0, QTableWidgetItem("11067"))
        # tableWidget.setItem(0, 1, QTableWidgetItem("Shahd Ahmed Ragab"))
        # tableWidget.setItem(1, 0, QTableWidgetItem("14675"))
        # tableWidget.setItem(1, 1, QTableWidgetItem("Hassnaa hussam"))
        # tableWidget.setItem(2, 0, QTableWidgetItem("14789"))
        # tableWidget.setItem(2, 1, QTableWidgetItem("Ayat Tarek"))
        # tableWidget.setItem(3, 0, QTableWidgetItem("10923"))
        # tableWidget.setItem(3, 1, QTableWidgetItem("Eman Abd El-Azeem"))

        # tableWidget.setItem(0, 2, QTableWidgetItem("second"))
        # tableWidget.setItem(1, 2, QTableWidgetItem("third"))
        # tableWidget.setItem(2, 2, QTableWidgetItem("first"))
        # tableWidget.setItem(3, 2, QTableWidgetItem("fourth"))
        # tableWidget.setItem(0, 3, QTableWidgetItem("SBE"))
        # tableWidget.setItem(2, 3, QTableWidgetItem("ARC"))
        # tableWidget.setItem(1, 3, QTableWidgetItem("CMP"))
        # tableWidget.setItem(3, 3, QTableWidgetItem("CVE"))
        # self.tableWidget.resizeColumnToContents(10)
        # self.tableWidget.resizeColumnToContents(5)

        self.tableWidget.setFont(QFont("Times", 12))
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)

        # Table will fit the screen horizontally
        self.tableWidget.setGeometry(40, 310, 1010, 600)
        self.tableWidget.setStyleSheet(
            "QTableWidget { border: 0px; background-color: #F4F4FE; color: #536e8f; border-radius : 15px;padding-left:15px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        self.tableWidget.setGraphicsEffect(shadow)
        self.tableWidget.cellClicked.connect(self.show_data)

    # def update_table(self, data_std):
    #     print("inside update table")
    #     self.tableWidget.setRowCount(len(data_std))
    #     row = 0
    #     for id in data_std:
    #         print("inside the table")
    #         self.tableWidget.setItem(row, 0, QTableWidgetItem(data_std[id].iid))
    #         self.tableWidget.setItem(row, 1, QTableWidgetItem(data_std[id].name))
    #         self.tableWidget.setItem(row, 2, QTableWidgetItem(data_std[id].grade))
    #         self.tableWidget.setItem(row, 3, QTableWidgetItem(data_std[id].department))
    #         row += 1
    #         print("id", id)

    def show_data(self, row):
        student_id = self.tableWidget.item(row, 0).text()
        self.profile_student_window = StudentData(student_id)
        self.profile_student_window.show()

    def filter_table(self):
        search_text = self.searchBox.text().strip().lower()
        if not search_text:
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(row, False)
            return

        for row in range(self.tableWidget.rowCount()):
            match_found = False
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item is not None and search_text in item.text().lower():
                    match_found = True
                    break
            self.tableWidget.setRowHidden(row, not match_found)

    def open_add_student_window(self):
        # self.update_table(data_std)
        self.add_student_window = AddStudent(self.tableWidget)
        self.add_student_window.show()
