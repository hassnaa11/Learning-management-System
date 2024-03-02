from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic.properties import QtCore
import pyqtgraph as pg
from PyQt5 import QtGui
from add_staff import AddStaff
from add_staff import data_staff
from staffprofile import StaffData


class staff(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UiComponents()
        self.setWindowTitle("Students ")
        self.setStyleSheet("background-color: #F9F8FD;")

    def UiComponents(self):
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

        # add student button
        self.addStaff = QPushButton(self)
        self.addStaff.setText("Add Staff")
        self.addStaff.setFont(QFont("Exo2", 11))
        self.addStaff.setGeometry(910, 130, 120, 40)
        self.addStaff.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #393984;"
            "};border-radius : 10px; background-color: #5558AC; color: white;"
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
        self.tableWidget.setColumnCount(3)

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
        self.tableWidget.cellClicked.connect(self.show_data)

        # Graph
        self.plot_widget = pg.PlotWidget(self)
        self.plot_widget.setLabel("left", " No.of professors")
        self.plot_widget.setLabel("bottom", "year")
        axis = self.plot_widget.getAxis("bottom")
        self.plot_widget.move(1170, 300)  # Set the position
        self.plot_widget.resize(300, 300)
        axis.setTicks(
            [[(1, "First"), (2, "Second"), (3, "Third"), (4, "fourth"), (5, "prep")]]
        )
        self.data = {"First": 1, "Second": 2, "Third": 3, "Fourth": 4, "Prep": 5}
        self.x_values = [1, 2, 3, 4, 5]
        self.plot_widget.setBackground(QtGui.QColor(100, 50, 254, 25))
        self.updatee = QPushButton(self)
        self.updatee.setText("update graph")
        self.updatee.setFont(QFont("Exo2", 11))
        self.updatee.setGeometry(1270, 630, 120, 40)
        self.updatee.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #7A51A1;"
            "};border-radius : 10px; background-color: #B67ADC; color: white;"
        )
        self.updatee.setCursor(Qt.PointingHandCursor)
        # self.updatee.clicked.connect(self.update_graph)

    def show_data(self, row):
        staff_id = self.tableWidget.item(row, 0).text()
        self.profile_staff_window = StaffData(staff_id)
        self.profile_staff_window.show()

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
        self.add_staff_window = AddStaff(self.tableWidget)
        self.add_staff_window.show()
