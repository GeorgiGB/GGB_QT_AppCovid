# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet
from interface import *
from urlRequest import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionLogin.triggered.connect(self.pepe)
        self.ui.actionExit.triggered.connect(lambda: sys.exit())

    def pepe(self):
        print("A")


if __name__ == "__main__":
    # Para quitar el error: "Qt WebEngine seems to be initialized from a plugin"
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    apply_stylesheet(app, theme='dark_yellow.xml')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
