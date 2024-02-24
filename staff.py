import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.uic.properties import QtCore
import csv
import math
from add_staff import AddStaff


class staff(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.data = []
        self.UiComponents()

        self.setWindowTitle("Students ")

        self.setStyleSheet("background-color: #F9F8FD;")
        # self.show()

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
        studentWordLabel.setText("Staff")
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

        # the two buttons label above
        btLabel = QLabel(self)
        btLabel.setStyleSheet("border-radius : 10px; background-color: #B67ADC;")
        btLabel.setGeometry(900, 130, 105, 40)

        self.filter = QPushButton(self)
        self.filter.setFont(QFont("Protest Riot", 15))
        self.filter.resize(32, 32)
        self.filter.move(915, 135)
        self.filter.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #50336D;"
            "};border-radius : 10px;background-color:#7A51A1 ;color:white; bold"
        )
        self.filter.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon(
            "icons8-filter-50.jpg"
        )  # Replace 'icon.png' with the path to your icon file
        self.filter.setIcon(self.icon)
        # self.filter.clicked(self.go_to_anotherWindow())

        self.list = QPushButton(self)
        self.list.setFont(QFont("Protest Riot", 15))
        self.list.resize(32, 32)
        self.list.move(960, 135)
        self.list.setStyleSheet(
            "border-radius : 10px;background-color: #7A51A1 ;color:white; bold"
        )
        self.list.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon(
            "icons8-list-30.jpg"
        )  # Replace 'icon.png' with the path to your icon file
        self.list.setIcon(self.icon)

        # add student button
        self.addStaff = QPushButton(self)
        self.addStaff.setText("Add Staff")
        self.addStaff.setFont(QFont("Exo2", 11))
        self.addStaff.setGeometry(750, 130, 120, 40)
        self.addStaff.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #7A51A1;"
            "};border-radius : 10px; background-color: #B67ADC; color: white;"
        )
        self.addStaff.setCursor(Qt.PointingHandCursor)
        self.addStaff.clicked.connect(self.open_add_staff_window)

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
        headertabel.setColumnCount(3)
        headertabel.setRowCount(1)
        headertabel.setItem(0, 0, QTableWidgetItem("Staff ID"))
        headertabel.setItem(0, 1, QTableWidgetItem("Staff Name"))
        headertabel.setItem(0, 2, QTableWidgetItem("Staff position"))

        headertabel.resizeRowToContents(4)
        headertabel.setFont(QFont("Exo2", 14))
        headertabel.setGeometry(40, 250, 1010, 46)
        headertabel.setStyleSheet(
            "QTableWidget { border: 0px; background-color: #F4F4FE; color: #536e8f; border-radius : 20px;padding-left:15px;selection-background-color: #EDE1F7; selection-color: black}"
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
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        # a = Admin()
        # # a.open_file_dialog()

        # i = 3
        # print("uiiii")
        # # print("lenn: ", (math.sqrt(len(a.data))) - 1)
        # for row in range(4):
        #     for col in range(3):
        #         tableWidget.setItem(row, col, QTableWidgetItem(a.data[i]))
        #         i += 1

        # tableWidget.setItem(0, 0, QTableWidgetItem(a.data[3]))
        # tableWidget.setItem(0, 1, QTableWidgetItem("Eman Mazraban"))
        # tableWidget.setItem(1, 0, QTableWidgetItem("14675"))
        # tableWidget.setItem(1, 1, QTableWidgetItem("Mohamed Islam"))
        # tableWidget.setItem(2, 0, QTableWidgetItem("14789"))
        # tableWidget.setItem(2, 1, QTableWidgetItem("peter Emad"))
        # tableWidget.setItem(3, 0, QTableWidgetItem("10923"))
        # tableWidget.setItem(3, 1, QTableWidgetItem("Mohamed mostafa"))

        # tableWidget.setItem(0, 2, QTableWidgetItem("Professor"))
        # tableWidget.setItem(1, 2, QTableWidgetItem("Professor"))
        # tableWidget.setItem(2, 2, QTableWidgetItem("Teaching Assistant"))
        # tableWidget.setItem(3, 2, QTableWidgetItem("Teaching Assistant"))

        self.tableWidget.resizeColumnToContents(10)
        self.tableWidget.resizeColumnToContents(5)

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

        # def get_data(self, d):
        #     self.data = d
        #     self.update_tabel()

        # def update_tabel(self):
        #     # self.hide()
        #     # a = Admin()
        #     # a.open_file_dialog()
        #     # self.tableWidget.clearContents()
        #     i = 3
        #     print("uiiii")
        #     print("DATA: ", self.data)
        #     # print("lenn: ", (math.sqrt(len(a.data))) - 1)
        #     for row in range(4):
        #         for col in range(3):
        #             self.tableWidget.setItem(row, col, QTableWidgetItem(self.data[i]))
        #             # self.tableWidget.show()
        #             i += 1
        #     # self.repaint()
        #     # self.UiComponents()
        #     # self.show()

    def update_tabel(self, data):
        # self.hide()
        # a = Admin()
        # a.open_file_dialog()
        # self.tableWidget.clearContents()
        i = 3
        print("uiiii")
        print("DATA: ", data)
        # print("lenn: ", (math.sqrt(len(a.data))) - 1)
        for row in range(4):
            for col in range(3):
                self.tableWidget.setItem(row, col, QTableWidgetItem(data[i]))
                # self.tableWidget.show()
                i += 1
        # self.repaint()
        # self.UiComponents()
        # self.show()

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

    def open_add_staff_window(self):
        self.add_staff_window = AddStaff()
        self.add_staff_window.show()
