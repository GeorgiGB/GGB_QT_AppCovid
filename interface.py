# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formWpoLIo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(650, 500)
        #MainWindow.setMaximumSize(1000, 1000)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        icon = QIcon()
        icon.addFile(u"Icon/exit.png", QSize())
        self.actionExit.setIcon(icon)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        icon1 = QIcon()
        icon1.addFile("Icon/help.jpg", QSize())
        self.actionHelp.setIcon(icon1)
        self.actionAbout_App = QAction(MainWindow)
        self.actionAbout_App.setObjectName(u"actionAbout_App")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        icon2 = QIcon()
        icon2.addFile(u"Icon/4.png", QSize())
        self.actionLogout.setIcon(icon2)
        self.actionLogin = QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        icon3 = QIcon()
        icon3.addFile("Icon/3.png", QSize())
        self.actionLogin.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titulo = QPlainTextEdit(self.centralwidget)
        self.titulo.setObjectName("titulo")
        self.titulo.setGeometry(QRect(220, 39, 230, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        self.titulo.setMaximumSize(QSize(230, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)

        self.titulo.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 626, 378))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Opciones = QWidget(self.widget)
        self.Opciones.setObjectName(u"Opciones")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(150)
        sizePolicy1.setVerticalStretch(80)
        sizePolicy1.setHeightForWidth(self.Opciones.sizePolicy().hasHeightForWidth())
        self.Opciones.setSizePolicy(sizePolicy1)
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
        
        #label 2
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.label2.Text("Proyecto Covid")
        self.label_2.setMinimumSize(QSize(120, 120))
        self.label_2.setMaximumSize(QSize(120, 120))
        self.label_2.setPixmap(QPixmap("Icon/logoCovidBlanco.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.label = QLabel(self.Opciones)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 80))
        self.label.setMaximumSize(QSize(170, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
    
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

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
        self.plainTextEdit_2.setFont(font1)
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit_2)


        self.horizontalLayout.addWidget(self.Grafico, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", "Help", None))
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout_App.setText(QCoreApplication.translate("MainWindow", "About App", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", "Logout", None))
#if QT_CONFIG(shortcut)
        self.actionLogout.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+Shift+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionLogin.setText(QCoreApplication.translate("MainWindow", "Login", None))
#if QT_CONFIG(shortcut)
        self.actionLogin.setShortcut(QCoreApplication.translate("MainWindow", "Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.titulo.setPlainText(QCoreApplication.translate("MainWindow","Proyecto App Covid", None))
        self.label_2.setText("Proyecto App Covid")
        self.label.setText(QCoreApplication.translate("MainWindow", "Elige una provincia", None))
        self.buscador.setItemText(0, QCoreApplication.translate("MainWindow", "Valencia", None))
        self.buscador.setItemText(1, QCoreApplication.translate("MainWindow", "Alicante", None))
        self.buscador.setItemText(2, QCoreApplication.translate("MainWindow", "Castellon", None))

        self.mostrarButton.setText(QCoreApplication.translate("MainWindow", "Mostrar", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", "Informaci\u00f3n de la provincia", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "Profile", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", "Info", None))



