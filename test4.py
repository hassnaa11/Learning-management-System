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
from data import Data
import re
# from students import Students

data_std = {}


class AddStudent(QDialog):
    def __init__(self):
        super().__init__()
        self.data_std = data_std
        self.setGeometry(500, 100, 950, 700)
        self.setWindowTitle("Add New Student")
        self.UiComponents()
        self.show()

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
        self.label.move(150, 165)
        self.label.resize(700, 500)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0, 0)
        self.label.setGraphicsEffect(shadow)

        self.label0 = QLabel(self)
        self.label0.setStyleSheet(
            "border-radius : 100px; background-color: rgba(63,71,105)"
        )
        self.pixmap = QPixmap("images/person.png")
        self.label0.setPixmap(self.pixmap)
        self.label0.move(400, 35)
        self.label0.resize(200, 200)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(200, 275)
        self.textbox1.resize(300, 50)
        self.textbox1.setPlaceholderText("First Name")
        self.textbox1.setFont(QFont("Protest Riot", 12))
        self.textbox1.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(510, 275)
        self.textbox2.resize(300, 50)
        self.textbox2.setPlaceholderText("Last Name")
        self.textbox2.setFont(QFont("Protest Riot", 12))
        self.textbox2.setStyleSheet(
            "border-radius : 25px;background-color: rgba(255,255,255,0.7) ; padding-left: 65px"
        )

        self.idBox = QLineEdit(self)
        self.idBox.move(200, 515)
        self.idBox.resize(145, 50)
        self.idBox.setPlaceholderText("ID")
        self.idBox.setFont(QFont("Protest Riot", 12))
        self.idBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 40px"
        )

        self.yearBox = QLineEdit(self)
        self.yearBox.move(353, 515)
        self.yearBox.resize(145, 50)
        self.yearBox.setPlaceholderText("Year")
        self.yearBox.setFont(QFont("Protest Riot", 12))
        self.yearBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 40px"
        )

        self.ageBox = QLineEdit(self)
        self.ageBox.move(510, 435)
        self.ageBox.resize(145, 50)
        self.ageBox.setPlaceholderText("Age")
        self.ageBox.setFont(QFont("Protest Riot", 12))
        self.ageBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 40px"
        )

        self.modBox = QLineEdit(self)
        self.modBox.move(200, 355)
        self.modBox.resize(300, 50)
        self.modBox.setPlaceholderText("Phone Number")
        self.modBox.setFont(QFont("Protest Riot", 12))
        self.modBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.mailBox = QLineEdit(self)
        self.mailBox.move(510, 355)
        self.mailBox.resize(300, 50)
        self.mailBox.setPlaceholderText("Email")
        self.mailBox.setFont(QFont("Protest Riot", 12))
        self.mailBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.gradeBox = QLineEdit(self)
        self.gradeBox.move(665, 435)
        self.gradeBox.resize(145, 50)
        self.gradeBox.setPlaceholderText("Grade")
        self.gradeBox.setFont(QFont("Protest Riot", 12))
        self.gradeBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 40px"
        )

        self.DepBox = QLineEdit(self)
        self.DepBox.move(200, 435)
        self.DepBox.resize(300, 50)
        self.DepBox.setPlaceholderText("Department")
        self.DepBox.setFont(QFont("Protest Riot", 12))
        self.DepBox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        self.btn = QPushButton(self)
        self.btn.setText("Add")
        self.btn.setFont(QFont("Protest Riot", 15))
        self.btn.resize(200, 50)
        self.btn.move(350, 595)
        self.btn.setStyleSheet(
            "border-radius : 25px;background-color: rgba(63,71,105) ;color:white; bold"
        )
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.clicked.connect(self.submit_data)

        self.rbtn = QPushButton(self)
        self.rbtn.setFont(QFont("Protest Riot", 15))
        self.rbtn.resize(50, 50)
        self.rbtn.move(560, 596)
        self.rbtn.setStyleSheet(
            "border-radius : 25px;background-color: rgba(63,71,105) ;color:white; bold"
        )
        self.rbtn.setCursor(Qt.PointingHandCursor)
        self.icon = QIcon(
            'images/back.pnp'
        )  # Replace 'icon.png' with the path to your icon file
        self.rbtn.setIcon(self.icon)
        self.rbtn.clicked.connect(self.clear_form)

        self.female = QLabel(self)

        self.female.setStyleSheet(
            "border-radius : 30px; background-color: rgba(177,161,172)"
        )
        self.pixmap = QPixmap("images/femal.png")
        self.female.setPixmap(self.pixmap)
        self.female.move(535, 515)
        self.female.resize(60, 60)
        self.female.setAlignment(QtCore.Qt.AlignCenter)

        self.femalebox = QCheckBox(self)
        self.femalebox.move(610, 535)
        self.femalebox.resize(20, 20)

        self.male = QLabel(self)
        self.male.setStyleSheet(
            "border-radius : 30px; background-color: rgba(63,71,105)"
        )

        self.pixmap = QPixmap("images/male.png")
        self.male.setPixmap(self.pixmap)
        self.male.move(665, 515)
        self.male.resize(60, 60)
        self.male.setAlignment(QtCore.Qt.AlignCenter)

        self.malebox = QCheckBox(self)
        self.malebox.move(740, 535)
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
        iid = self.idBox.text()
        year = self.yearBox.text()

        name = self.textbox1.text().strip()
        age = self.ageBox.text().strip()
        email = self.mailBox.text().strip()
        grade = self.gradeBox.text().strip()
        number = self.modBox.text().strip()
        department = self.DepBox.text().strip()
        iid = self.idBox.text().strip()
        year = self.yearBox.text().strip()

        if not name:
            self.show_error_message('Name is required.')
            return

        if not re.match(r'^[a-zA-Z\s]+$', name):
            self.show_error_message('Name should only contain letters and spaces.')
            return

        if not department:
            self.show_error_message('Department is required.')
            return

        if not re.match(r'^[a-zA-Z\s]+$', name):
            self.show_error_message('Department should only contain letters and spaces.')
            return

        if not year:
            self.show_error_message('Year is required.')
            return

        if not re.match(r'^[a-zA-Z\s]+$', name):
            self.show_error_message('Year should only contain letters and spaces.')
            return

        if not age:
            self.show_error_message('Age is required.')
            return

        if not age.isdigit():
            self.show_error_message('Age should be a number.')
            return

        if not grade:
            self.show_error_message('Grade is required.')
            return

        if not grade.isdigit():
            self.show_error_message('Grade should be a number.')
            return

        if not iid:
            self.show_error_message('ID is required.')
            return

        if not iid.isdigit():
            self.show_error_message('ID should be a number.')
            return

        if not number:
            self.show_error_message('Phone Number is required.')
            return

        if not number.isdigit():
            self.show_error_message('Phone Number should be a number.')
            return

        if not email:
            self.show_error_message('Email is required.')
            return

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            self.show_error_message('Invalid email format.')
            return

        self.show_success_message('Form is valid!')

        if self.femalebox.isChecked():
            checked = "Female"
        else:
            checked = "Male"

        #data_std[iid] = Data(
        #    iid, name, age, grade, number, email, department, year, checked, []
        #)
        # Students.update_table(Students, data_std)

        #print("data: ", data_std[iid].name)
        self.close()

    def clear_form(self):
        self.textbox1.clear()
        self.textbox2.clear()
        self.ageBox.clear()
        self.gradeBox.clear()
        self.modBox.clear()
        self.mailBox.clear()
        self.DepBox.clear()
        self.idBox.clear()
        self.yearBox.clear()
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

    def show_error_message(self, message):
        QMessageBox.warning(self, 'Error', message)

    def show_success_message(self, message):
        QMessageBox.information(self, 'Success', message)

app = QApplication(sys.argv)
window = AddStudent()
sys.exit(app.exec_())