from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QApplication,
    QLabel,
)
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import csv
import sys
from main import MainWindow


class login_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 1500, 850)
        self.setWindowTitle("Edraak")
        self.UiComponents()
        self.show()

    def UiComponents(self):
        # Protest Riot Font
        QFontDatabase.addApplicationFont("fonts\ProtestRiot-Regular.ttf")

        # background gradient
        p = QPalette()
        gradient = QLinearGradient(0, 0, 200, 800)
        gradient.setColorAt(0.25, QColor(234, 218, 222))
        gradient.setColorAt(0.5, QColor(200, 186, 211))
        gradient.setColorAt(0.75, QColor(166, 149, 183))
        gradient.setColorAt(1.0, QColor(122, 135, 184))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        # logo
        self.logo = QLabel(self)
        self.pixmap = QPixmap("images\logo.png")
        self.logo.setPixmap(self.pixmap)
        self.logo.move(1300, 60)
        self.logo.resize(150, 90)

        # background of username & pass
        self.background = QLabel(self)
        self.background.setStyleSheet(
            "border-radius : 80px; background-color: rgba(255, 255, 255,0.3);"
        )
        self.background.move(510, 265)
        self.background.resize(515, 430)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0, 0)
        self.background.setGraphicsEffect(shadow)

        # big person image
        self.person_img = QLabel(self)
        self.person_img.setStyleSheet(
            "border-radius : 100px; background-color: rgba(63,71,105)"
        )
        self.pixmap = QPixmap("./images\person.png")
        self.person_img.setPixmap(self.pixmap)
        self.person_img.move(670, 150)
        self.person_img.resize(200, 200)
        self.person_img.setAlignment(QtCore.Qt.AlignCenter)

        # Username textbox
        self.username_textbox = QLineEdit(self)
        self.username_textbox.move(620, 405)
        self.username_textbox.resize(300, 50)
        self.username_textbox.setPlaceholderText("Username")
        self.username_textbox.setFont(QFont("Protest Riot", 12))
        self.username_textbox.setStyleSheet(
            "border-radius : 25px ; background-color: rgba(255,255,255,0.7); padding-left: 65px"
        )

        # password textbox
        self.password_textbox = QLineEdit(self)
        self.password_textbox.move(620, 485)
        self.password_textbox.resize(300, 50)
        self.password_textbox.setPlaceholderText("Password")
        self.password_textbox.setFont(QFont("Protest Riot", 12))
        self.password_textbox.setStyleSheet(
            "border-radius : 25px;background-color: rgba(255,255,255,0.7) ; padding-left: 20px"
        )
        self.password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)

        # small person image next to username textbox
        self.person_img2 = QLabel(self)
        self.person_img2.setStyleSheet(
            "border-radius : 30px; background-color: rgba(63,71,105)"
        )
        self.pixmap = QPixmap("./images\person1.png")
        self.person_img2.setPixmap(self.pixmap)
        self.person_img2.move(620, 400)
        self.person_img2.resize(60, 60)
        self.person_img2.setAlignment(QtCore.Qt.AlignCenter)

        # lock image next to password textbox
        self.lock_img = QLabel(self)
        self.lock_img.setStyleSheet(
            "border-radius : 30px; background-color: rgba(63,71,105)"
        )
        self.pixmap = QPixmap("./images\lock.png")
        self.lock_img.setPixmap(self.pixmap)
        self.lock_img.move(875, 481)
        self.lock_img.resize(60, 60)
        self.lock_img.setAlignment(QtCore.Qt.AlignCenter)

        # Login button
        self.login_btn = QPushButton(self)
        self.login_btn.setText("LogIn")
        self.login_btn.setFont(QFont("Protest Riot", 15))
        self.login_btn.resize(190, 50)
        self.login_btn.move(670, 590)
        self.login_btn.setStyleSheet(
            " QPushButton::hover"
            "{"
            "background-color : #212442;"
            "}; border-radius : 25px;background-color: rgba(63,71,105) ;color:white"
        )
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.clicked.connect(self.login)

    def login(self):
        username = self.username_textbox.text()
        password = self.password_textbox.text()
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if username == row[2] and password == row[3]:
                    self.hide()  # Hide the login window
                    main_window = MainWindow(
                        row[1]
                    )  # Create an instance of the main window
                    main_window.show()
                    break
            else:
                self.errorDialog()

    def errorDialog(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle("Error")
        dialog.resize(300, 200)
        dialog.setStyleSheet("background-color:#5558AC;")

        label = QLabel(self)
        label.setText("Password or Username is wrong!")
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


app = QApplication(sys.argv)
window = login_window()
sys.exit(app.exec_())
