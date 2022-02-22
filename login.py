import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
                               QFormLayout, QLineEdit, QLabel, QPushButton)
import main
import bd
from qt_material import apply_stylesheet
from PySide6.QtGui import QKeySequence


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Iniciar Sesion")

        label1 = QLabel("Bienvenido")
        label1.setAlignment(Qt.AlignHCenter)
        label1.setStyleSheet("QLabel{color:yellow}")

        self.setFixedSize(250, 150)

        layoutPrincipal = QFormLayout()

        # Lineas donde introduciremos el nombre y contraseña del usuario
        self.userName = QLineEdit("")
        self.passwd = QLineEdit("")
        self.passwd.setEchoMode(QLineEdit.Password)

        # Con un addRow los añadimos en el layoutPrincipal
        layoutPrincipal.addRow(label1)
        layoutPrincipal.addRow(QLabel("Usuario"), self.userName)
        layoutPrincipal.addRow(QLabel("Contra"), self.passwd)

        self.main1 = None

        self.button1 = QPushButton("Iniciar Sesion")
        layoutPrincipal.addRow(self.button1)
        self.button1.clicked.connect(lambda: self.button_pressed(self.userName.text(), self.passwd.text()))
        self.setLayout(layoutPrincipal)
        # ShortCuts para pulsar enter
        self.button1.setShortcut(QKeySequence(Qt.Key_Return))

    # Con el boton confirmamos si el usuario y la contraseña son correctos para que nos permita pasar al MainWindow

    def button_pressed(self, user, passwd):
        if bd.readBD(user, passwd):
            if self.main1 is None:
                self.main1 = main.MainWindow(self)
                self.hide()
                self.main1.show()


if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme='dark_yellow.xml')
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
