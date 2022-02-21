# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formnAhdIU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setMinimumSize(QSize(650, 500))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon = QIcon()
        icon.addFile(u"Icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon1 = QIcon()
        icon1.addFile(u"Icon/help.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon1)
        self.actionAbout_App = QAction(MainWindow)
        self.actionAbout_App.setObjectName(u"actionAbout_App")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        icon2 = QIcon()
        icon2.addFile(u"Icon/4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLogout.setIcon(icon2)
        self.actionLogin = QAction(MainWindow)
        self.actionLogin.setObjectName(u"actionLogin")
        icon3 = QIcon()
        icon3.addFile(u"Icon/3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLogin.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 626, 378))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Opciones = QWidget(self.widget)
        self.Opciones.setObjectName(u"Opciones")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.Opciones.sizePolicy().hasHeightForWidth())
        self.Opciones.setSizePolicy(sizePolicy)
        self.Opciones.setMinimumSize(QSize(100, 100))
        self.Opciones.setMaximumSize(QSize(170, 500))
        self.verticalLayout_3 = QVBoxLayout(self.Opciones)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.Opciones)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(100, 10))
        self.widget_2.setMaximumSize(QSize(170, 120))
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 120))
        self.label_2.setMaximumSize(QSize(120, 120))
        self.label_2.setPixmap(QPixmap(u"Icon/logoCovidBlanco.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.label = QLabel(self.Opciones)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(100, 80))
        self.label.setMaximumSize(QSize(170, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.buscador = QComboBox(self.Opciones)
        self.buscador.addItem("")
        self.buscador.addItem("")
        self.buscador.addItem("")
        self.buscador.setObjectName(u"buscador")
        self.buscador.setMaximumSize(QSize(180, 35))
        self.buscador.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.buscador)

        self.mostrarButton = QPushButton(self.Opciones)
        self.mostrarButton.setObjectName(u"mostrarButton")
        self.mostrarButton.setMinimumSize(QSize(70, 30))
        self.mostrarButton.setMaximumSize(QSize(200, 30))
        self.mostrarButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.mostrarButton)


        self.horizontalLayout.addWidget(self.Opciones)

        self.Grafico = QWidget(self.widget)
        self.Grafico.setObjectName(u"Grafico")
        self.Grafico.setEnabled(True)
        self.Grafico.setMinimumSize(QSize(0, 0))
        self.Grafico.setMaximumSize(QSize(300, 300))
        self.verticalLayout_2 = QVBoxLayout(self.Grafico)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit_2 = QPlainTextEdit(self.Grafico)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMaximumSize(QSize(300, 60))
        self.plainTextEdit_2.setSizeIncrement(QSize(1, 1))
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit_2, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.Grafico)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(200, 0, 251, 71))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titulo = QPlainTextEdit(self.verticalLayoutWidget)
        self.titulo.setObjectName(u"titulo")
        sizePolicy1.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy1)
        self.titulo.setMaximumSize(QSize(230, 50))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.titulo.setFont(font1)
        self.titulo.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.titulo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionHelp)
        self.menuInfo.addAction(self.actionAbout_App)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout_App.setText(QCoreApplication.translate("MainWindow", u"About App", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
#if QT_CONFIG(shortcut)
        self.actionLogout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(shortcut)
        self.actionLogin.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Elige una provincia", None))
        self.buscador.setItemText(0, QCoreApplication.translate("MainWindow", u"Valencia", None))
        self.buscador.setItemText(1, QCoreApplication.translate("MainWindow", u"Alicante", None))
        self.buscador.setItemText(2, QCoreApplication.translate("MainWindow", u"Castellon", None))

        self.mostrarButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n de la provincia", None))
        self.titulo.setPlainText(QCoreApplication.translate("MainWindow", u"Proyecto App Covid", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

