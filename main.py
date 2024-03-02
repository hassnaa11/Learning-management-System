from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal
from staff import staff
from admin import Admin
from students import Students
from courses import Courses


class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        self.clicked.emit()


class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        QFontDatabase.addApplicationFont("fonts\ProtestRiot-Regular.ttf")
        QFontDatabase.addApplicationFont("fonts\Exo2-Regular.ttf")
        QFontDatabase.addApplicationFont("fonts\Exo2-SemiBold.ttf")
        self.setWindowTitle("Learning System")
        self.setGeometry(0, 0, 2000, 1000)
        self.setStyleSheet("background-color:  #5558AC; border-radius:40px;")

        self.content_widgets = {
            "Classes": Courses(username),
            "Admin": Admin(),
            "Students": Students(),
            "Staff": staff(),
        }

        self.UiComponents()
        self.show_content("Classes")
        self.showMaximized()

    def UiComponents(self):
        layout = QHBoxLayout()
        navbar = QWidget()
        self.admin_label = ClickableLabel("Admin", navbar)
        self.admin_label.clicked.connect(lambda: self.show_content("Admin"))
        self.admin_label.setFont(QFont("Broadway", 20))
        self.admin_label.move(80, 290)
        self.admin_label.setStyleSheet(
            " QLabel::hover" "{" "color : white;" "};color: #E1D7EB;"
        )
        self.admin_label.setCursor(Qt.PointingHandCursor)

        self.classes_label = ClickableLabel("Classes", navbar)
        self.classes_label.clicked.connect(lambda: self.show_content("Classes"))
        self.classes_label.setFont(QFont("Broadway", 20))
        self.classes_label.move(80, 380)
        self.classes_label.setStyleSheet(
            " QLabel::hover" "{" "color : white;" "};color: #E1D7EB"
        )
        self.classes_label.setCursor(Qt.PointingHandCursor)

        self.students_label = ClickableLabel("Students", navbar)
        self.students_label.clicked.connect(lambda: self.show_content("Students"))
        self.students_label.setFont(QFont(" Broadway", 20))
        self.students_label.move(80, 470)
        self.students_label.setStyleSheet(
            " QLabel::hover" "{" "color : white;" "};color: #E1D7EB"
        )
        self.students_label.setCursor(Qt.PointingHandCursor)

        self.stuff_label = ClickableLabel("Staff", navbar)
        self.stuff_label.clicked.connect(lambda: self.show_content("Staff"))

        self.stuff_label.setFont(QFont("Broadway", 20))
        self.stuff_label.move(80, 560)
        self.stuff_label.setStyleSheet(
            " QLabel::hover" "{" "color : white;" "};color: #E1D7EB"
        )
        self.stuff_label.setCursor(Qt.PointingHandCursor)

        navbar.setStyleSheet("background-color: #5558AC")

        # logo
        pic0 = QPixmap("images\logo.png")
        pic0_label = QLabel(navbar)
        pic0_label.setPixmap(pic0)
        pic0_label.move(40, 60)

        pic2 = QPixmap("images/admin.png")
        pic2_label = QLabel(navbar)
        pic2_label.setPixmap(pic2.scaled(50, 50))
        pic2_label.move(10, 280)

        pic3 = QPixmap("images/classes.png")
        pic3_label = QLabel(navbar)
        pic3_label.setPixmap(pic3.scaled(50, 50))
        pic3_label.move(10, 370)

        pic4 = QPixmap("images/students.png")
        pic4_label = QLabel(navbar)
        pic4_label.setPixmap(pic4.scaled(50, 50))
        pic4_label.move(10, 460)

        pic5 = QPixmap("images/staff.png")
        pic5_label = QLabel(navbar)
        pic5_label.setPixmap(pic5.scaled(50, 50))
        pic5_label.move(10, 550)

        layout.addWidget(navbar, 1)

        self.page = QWidget()
        self.page.setStyleSheet("background-color: white")
        layout.addWidget(self.page, 5)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.content_layout = QVBoxLayout(self.page)
        self.current_content = None

    def show_content(self, content):
        if self.current_content == content:
            return

        self.clear_content_layout()
        content_widget = self.content_widgets.get(content)
        if content_widget:
            self.content_layout.addWidget(content_widget)
            content_widget.show()

        self.current_content = content

    def clear_content_layout(self):
        if self.content_layout.count() > 0:
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            widget.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow("Student")
    sys.exit(app.exec_())
