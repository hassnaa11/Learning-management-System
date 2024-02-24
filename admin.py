import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import csv

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal

from math import inf
from staff import staff

data = []
students_data = []
courses_std = []


class Admin(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #F9F8FD;")
        self.data = data
        self.students_data = students_data
        self.courses_std = courses_std
        self.UiComponents()

    def UiComponents(self):
        self.title = QLabel("Admins", self)
        self.title.setFont(QFont("Protest Riot", 25))
        self.title.setStyleSheet(" color: rgba(63,71,105)")
        self.title.setGeometry(40, 40, 300, 100)

        self.searchBox = QLineEdit(self)
        self.searchBox.setPlaceholderText("Search")
        self.searchBox.setFont(QFont("Arial", 12))
        self.searchBox.setGeometry(
            600, 75, 280, 40
        )  # Set the geometry for the search box
        self.searchBox.setStyleSheet(
            "border-radius : 10px; background-color: #EDE1F7; color: black; padding-left: 55px ; padding-right:30px ;font-size: 15px"
        )
        self.searchBox.textChanged.connect(self.filter_table)

        # search icon
        search_label = QLabel(self)
        pixmap = QPixmap("images/icons8-search-30.png")
        search_label.setPixmap(pixmap)
        search_label.move(620, 78)
        search_label.resize(30, 30)
        search_label.setStyleSheet("background-color: transparent;")

        box = QLabel(self)

        box.setGeometry(30, 250, 870, 300)
        box.setStyleSheet("background-color:#F4F4FE; border-radius : 15px;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        box.setGraphicsEffect(shadow)

        pic6 = QPixmap("images/for_admin.png")
        pic6_label = QLabel(box)
        pic6_label.setPixmap(pic6.scaled(200, 200))
        pic6_label.move(10, 10)
        self.content_label1 = QLabel(
            "Manage the data by exporting and importing\nCSV files from here!", box
        )
        self.content_label1.setFont(QFont("Protest Riot"))
        self.content_label1.setStyleSheet(
            "font-size: 25px; color:black ;padding-left:25px;"
        )
        self.content_label1.setAlignment(Qt.AlignCenter)
        self.content_label1.move(210, 50)

        self.exporting_csv = QPushButton("Export", box)
        self.importing_csv = QPushButton("Import", box)
        self.importing_csv.setGeometry(250, 170, 150, 40)
        self.exporting_csv.setGeometry(500, 170, 150, 40)
        self.exporting_csv.setCursor(Qt.PointingHandCursor)
        self.importing_csv.setCursor(Qt.PointingHandCursor)
        self.exporting_csv.setStyleSheet(
            "border-radius : 15px; background-color:#492971 ;"
        )
        self.importing_csv.setStyleSheet(
            """
                                border-radius: 15px;
                                background-color: #5558AC;
                                color: white;
                            }
                            QPushButton:hover {
                                background-color: #393984;
                            }
                            """
        )
        self.exporting_csv.setStyleSheet(
            """
                                border-radius: 15px;
                                background-color: #5558AC;
                                color: white;
                            }
                            QPushButton:hover {
                                background-color: #393984;
                            }
                            """
        )
        self.importing_csv.setFont(QFont("Arial", 15))
        self.exporting_csv.setFont(QFont("Arial", 15))
        self.importing_csv.clicked.connect(self.open_file_dialog)

        headertabel = QTableWidget(self)
        headertabel.setColumnCount(3)
        headertabel.setRowCount(1)
        headertabel.setItem(0, 0, QTableWidgetItem("Admin ID"))
        headertabel.setItem(0, 1, QTableWidgetItem("Admin Name"))
        headertabel.setItem(0, 2, QTableWidgetItem("Admin Username"))

        headertabel.setFont(QFont("Times", 14))
        headertabel.setGeometry(30, 630, 870, 50)

        headertabel.setStyleSheet(
            "QTableWidget { border: 0px; color:black  ; background-color:#F4F4FE  ; border-radius : 15px;padding-left:20px;padding-top:7px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        headertabel.setGraphicsEffect(shadow)
        headertabel.horizontalHeader().setVisible(False)
        headertabel.verticalHeader().setVisible(False)
        headertabel.setShowGrid(False)
        headertabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("11067"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Shahd Ahmed Ragab"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("14675"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Hassnaa hussam"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("14789"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Ayat Tarek"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("10923"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Eman Abd El-Azeem"))

        self.tableWidget.setItem(0, 2, QTableWidgetItem("shahdd"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("hasnaa4"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("Ayatt"))
        self.tableWidget.setItem(3, 2, QTableWidgetItem("Eman304"))

        self.tableWidget.setFont(QFont("Times", 12))
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setShowGrid(False)

        # Table will fit the screen horizontally
        self.tableWidget.setGeometry(30, 700, 870, 200)
        self.tableWidget.setStyleSheet(
            "QTableWidget { border: 0px; background-color:#F4F4FE; color: black ; border-radius : 15px;padding-left:20px;padding-top:7px;selection-background-color: #EDE1F7; selection-color: black}"
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor("#BD80C5"))
        self.tableWidget.setGraphicsEffect(shadow)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

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

    # data = []

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter(
            "All Files (*.*)"
        )  # You can set specific file filters here
        if file_dialog.exec_():
            self.cond = 1
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                # Process the selected file
                # self.process_file(file_path)
                self.selected_file = file_path
                print("hello", self.selected_file)
            # if self.cond == 3:
            #     data.clear()
            #     self.data.clear()
            # students_data = []
            # self.students_data = []

        # self.data = []
        with open(self.selected_file, "r") as file:
            reader = csv.reader(file)
            i, k, j = 0, 0, 0
            self.data.append(inf)
            students_data.append(inf)
            for row in reader:
                for col_ind, col in enumerate(row):
                    if col_ind >= 0 and col_ind <= 3:
                        students_data.insert(k, col)
                        k += 1
                    elif col_ind >= 4 and col_ind <= 6:
                        self.data.insert(i, col)
                        print(col)
                        i += 1
                    elif col_ind >= 8 and col_ind <= 17:
                        if col != "":
                            courses_std.insert(k, col)
                        j += 1

            self.cond += 1

        # s = staff()
        # # s.get_data(self.data)
        # s.update_tabel(self.data)
        # s.tableWidget.repaint()
        # print(self.data)
        # print(len(self.data))
        # print(students_data)
        # print(len(students_data))
        print(courses_std)
        print(len(courses_std))

    # def process_file(self, file_path):
    #     rows = []
    #     with open(file_path, "r") as file:
    #         reader = csv.reader(file)
    #         row_ind = 0
    #         for row in reader:
    #             col_ind = 0
    #             for col in row:
    #                 print(row)

    #     return file_path