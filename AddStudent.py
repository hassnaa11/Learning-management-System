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
import pandas as pd


class AddStudent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 20, 1200, 1000)
        self.setWindowTitle("Edraak")
        self.UiComponents()
        # self.show()
        self.data_file = "data.xlsx"
        try:
            self.existing_data = pd.read_excel(self.data_file)
        except FileNotFoundError:
            self.existing_data = pd.DataFrame()

    def UiComponents(self):
        QFontDatabase.addApplicationFont("./ProtestRiot-Regular.ttf")
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
        self.label.move(510, 165)
        self.label.resize(515, 820)
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
        self.label0.move(670, 50)
        self.label0.resize(200, 200)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(620, 305)
        self.textbox1.resize(300, 50)
        self.textbox1.setPlaceholderText("First Name")
        self.textbox1.setFont(QFont("Protest Riot", 12))
        self.textbox1.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(620, 385)
        self.textbox2.resize(300, 50)
        self.textbox2.setPlaceholderText("Last Name")
        self.textbox2.setFont(QFont("Protest Riot", 12))
        self.textbox2.setStyleSheet(
            "border-radius : 25px;background-color: rgba(255,255,255,0.7) ; padding-left: 65px"
        )
        # self.textbox2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ageBox = QLineEdit(self)
        self.ageBox.move(620, 465)
        self.ageBox.resize(145, 50)
        self.ageBox.setPlaceholderText("Age")
        self.ageBox.setFont(QFont("Protest Riot", 12))
        self.ageBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.modBox = QLineEdit(self)
        self.modBox.move(620, 545)
        self.modBox.resize(300, 50)
        self.modBox.setPlaceholderText("Phone Number")
        self.modBox.setFont(QFont("Protest Riot", 12))
        self.modBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.mailBox = QLineEdit(self)
        self.mailBox.move(620, 625)
        self.mailBox.resize(300, 50)
        self.mailBox.setPlaceholderText("Email")
        self.mailBox.setFont(QFont("Protest Riot", 12))
        self.mailBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.gradeBox = QLineEdit(self)
        self.gradeBox.move(775, 465)
        self.gradeBox.resize(145, 50)
        self.gradeBox.setPlaceholderText("Grade")
        self.gradeBox.setFont(QFont("Protest Riot", 12))
        self.gradeBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.DepBox = QLineEdit(self)
        self.DepBox.move(620, 705)
        self.DepBox.resize(300, 50)
        self.DepBox.setPlaceholderText("Department")
        self.DepBox.setFont(QFont("Protest Riot", 12))
        self.DepBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.btn = QPushButton(self)
        self.btn.setText("Add")
        self.btn.setFont(QFont("Protest Riot", 15))
        self.btn.resize(130, 50)
        self.btn.move(670, 900)
        self.btn.setStyleSheet(
            "border-radius : 25px;background-color: rgba(63,71,105) ;color:white; bold"
        )
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.clicked.connect(self.submit_data)

        self.rbtn = QPushButton(self)
        self.rbtn.setFont(QFont("Protest Riot", 15))
        self.rbtn.resize(50, 50)
        self.rbtn.move(810, 900)
        self.rbtn.setStyleSheet(
            "border-radius : 25px;background-color: rgba(63,71,105) ;color:white; bold"
        )
        self.rbtn.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon(
            "icons8-back-50.png"
        )  # Replace 'icon.png' with the path to your icon file
        self.rbtn.setIcon(self.icon)
        self.rbtn.clicked.connect(self.clear_form)

        self.female = QLabel(self)

        self.female.setStyleSheet(
            "border-radius : 30px; background-color: rgba(177,161,172)"
        )
        self.pixmap = QPixmap("icons8-female-64.png")
        self.female.setPixmap(self.pixmap)
        self.female.move(670, 770)
        self.female.resize(60, 60)
        self.female.setAlignment(QtCore.Qt.AlignCenter)

        self.femalebox = QCheckBox(self)
        self.femalebox.move(694, 840)
        self.femalebox.resize(20, 20)

        self.male = QLabel(self)
        self.male.setStyleSheet(
            "border-radius : 30px; background-color: rgba(63,71,105)"
        )

        self.pixmap = QPixmap("icons8-male-64.png")
        self.male.setPixmap(self.pixmap)
        self.male.move(780, 770)
        self.male.resize(60, 60)
        self.male.setAlignment(QtCore.Qt.AlignCenter)

        self.malebox = QCheckBox(self)
        self.malebox.move(803, 840)
        self.malebox.resize(20, 20)

        # choose one box
        self.femalebox.stateChanged.connect(self.uncheck)
        self.malebox.stateChanged.connect(self.uncheck)

    def submit_data(self):
        name = self.textbox1.text() + " " + self.textbox2.text()
        age = self.ageBox.text()
        grade = self.gradeBox.text()
        number = self.modBox.text()
        email = self.mailBox.text()
        department = self.DepBox.text()
        if self.femalebox.isChecked():
            checked = "Female"
        else:
            checked = "Male"

        # Append new data to the existing data
        new_data = pd.DataFrame(
            {
                "Name": [name],
                "Age": [age],
                "Grade": [grade],
                "Phone Number": [number],
                "Email": [email],
                "Department": [department],
                "Gender": [checked],
            }
        )
        self.existing_data = pd.concat(
            [self.existing_data, new_data], ignore_index=True
        )

        # Save the combined data to the Excel file
        self.existing_data.to_excel(self.data_file, index=False)

        self.close()

    def clear_form(self):
        self.textbox1.clear()
        self.textbox2.clear()
        self.ageBox.clear()
        self.gradeBox.clear()
        self.modBox.clear()
        self.mailBox.clear()
        self.DepBox.clear()
        self.femalebox.setChecked(False)

    def uncheck(self, state):

        # checking if state is checked
        if state == Qt.Checked:

            # if first check box is selected
            if self.sender() == self.femalebox:

                # making other check box to uncheck
                self.malebox.setChecked(False)
            # self.checkBoxB.setChecked(False)

            # if second check box is selected
            elif self.sender() == self.malebox:

                # making other check box to uncheck
                self.femalebox.setChecked(False)


app = QApplication(sys.argv)
window = AddStudent()
sys.exit(app.exec_())
