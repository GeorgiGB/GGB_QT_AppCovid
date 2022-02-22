# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formAQlYaR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import programIcons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(700, 700)
        #MainWindow.setMaximumSize(900, 900)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon = QIcon()
        icon.addFile(u":/Imagenes/Icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon1 = QIcon()
        icon1.addFile(u"Icons/help.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon1)
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        icon2 = QIcon()
        icon2.addFile(u":/Imagenes/Icons/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLogout.setIcon(icon2)
        self.actionAuthor = QAction(MainWindow)
        self.actionAuthor.setObjectName(u"actionAuthor")
        self.actionAuthor.setCheckable(False)
        self.actionAuthor.setEnabled(False)
        self.actionAbout_App_2 = QAction(MainWindow)
        self.actionAbout_App_2.setObjectName(u"actionAbout_App_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widgetGeneral = QWidget(self.centralwidget)
        self.widgetGeneral.setObjectName(u"widgetGeneral")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widgetGeneral.setGeometry(QRect(40, 100, 630, 370))
        self.horizontalLayout = QHBoxLayout(self.widgetGeneral)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Opciones = QWidget(self.widgetGeneral)
        self.Opciones.setObjectName(u"Opciones")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.Opciones.sizePolicy().hasHeightForWidth())
        self.Opciones.setSizePolicy(sizePolicy)
        self.Opciones.setMinimumSize(QSize(100, 100))
        self.Opciones.setMaximumSize(QSize(170, 400))
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
        self.label_2.setPixmap(QPixmap(u":/Imagenes/Icons/logoCovidBlanco.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.elegirProvincia = QLabel(self.Opciones)
        self.elegirProvincia.setObjectName(u"elegirProvincia")
        self.elegirProvincia.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.elegirProvincia.sizePolicy().hasHeightForWidth())
        self.elegirProvincia.setSizePolicy(sizePolicy1)
        self.elegirProvincia.setMinimumSize(QSize(100, 80))
        self.elegirProvincia.setMaximumSize(QSize(170, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)

        self.elegirProvincia.setFont(font)
        self.elegirProvincia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.elegirProvincia)

        self.buscadorProvincia = QComboBox(self.Opciones)
        self.buscadorProvincia.addItem("")
        self.buscadorProvincia.addItem("")
        self.buscadorProvincia.addItem("")
        self.buscadorProvincia.setObjectName(u"buscadorProvincia")
        self.buscadorProvincia.setMaximumSize(QSize(180, 35))
        self.buscadorProvincia.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.buscadorProvincia)

        self.buscadorCiudad = QComboBox(self.Opciones)
        self.buscadorCiudad.setObjectName(u"buscadorCiudad")

        self.verticalLayout_3.addWidget(self.buscadorCiudad)

        self.buscadorCiudad.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Elige un municipio", None))

        self.mostrarButton = QPushButton(self.Opciones)
        self.mostrarButton.setObjectName(u"mostrarButton")
        self.mostrarButton.setMinimumSize(QSize(70, 30))
        self.mostrarButton.setMaximumSize(QSize(200, 30))
        self.mostrarButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.mostrarButton)

        self.horizontalLayout.addWidget(self.Opciones)

        self.GraficoWidget = QWidget(self.widgetGeneral)
        self.GraficoWidget.setObjectName(u"GraficoWidget")
        self.GraficoWidget.setEnabled(True)
        self.GraficoWidget.setMaximumSize(16777215, 16777215)
        self.verticalLayout_2 = QVBoxLayout(self.GraficoWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.informacion = QLabel(self.GraficoWidget)
        self.informacion.setObjectName(u"informacion")
        self.informacion.setMaximumSize(QSize(150, 100))
        font1 = QFont()
        self.informacion.setStyleSheet("""QLabel
                                                           {
                                                           font: 700 18pt "Segoe UI";
                                                           }
                                                           """)

        self.informacion.setFont(font1)

        self.verticalLayout_2.addWidget(self.informacion, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.grafico = QFrame(self.GraficoWidget)
        self.grafico.setObjectName(u"grafico")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.grafico.sizePolicy().hasHeightForWidth())
        self.grafico.setSizePolicy(sizePolicy2)
        self.grafico_2 = QGridLayout(self.grafico)
        self.grafico_2.setSpacing(0)
        self.grafico_2.setObjectName(u"grafico_2")
        self.grafico_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.grafico)

        self.horizontalLayout.addWidget(self.GraficoWidget)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(220, 10, 251, 71))
        self.verticalLayoutTitulo = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutTitulo.setSpacing(0)
        self.verticalLayoutTitulo.setObjectName(u"verticalLayoutTitulo")
        self.verticalLayoutTitulo.setContentsMargins(0, 0, 0, 0)
        self.titulo = QLabel(self.verticalLayoutWidget)
        self.titulo.setObjectName(u"titulo")
        font2 = QFont()
        self.titulo.setStyleSheet("""QLabel
                                           {
                                           font: 700 20pt "Segoe UI";
                                           }
                                           """)

        self.titulo.setFont(font2)

        self.verticalLayoutTitulo.addWidget(self.titulo, 0, Qt.AlignHCenter)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        self.menuAbout_App = QMenu(self.menuInfo)
        self.menuAbout_App.setObjectName(u"menuAbout_App")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        #self.menuFile.addAction(self.actionGithub)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionHelp)
        self.menuInfo.addAction(self.menuAbout_App.menuAction())
        self.menuAbout_App.addAction(self.actionAuthor)
        self.menuAbout_App.addAction(self.actionAbout_App_2)

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
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
#if QT_CONFIG(shortcut)
        self.actionLogout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionAuthor.setText(QCoreApplication.translate("MainWindow", u"Author: Georgi Georgiev DI 2021-2022", None))
        self.actionAbout_App_2.setText(QCoreApplication.translate("MainWindow", u"About App", None))
        self.label_2.setText("")
        self.elegirProvincia.setText(QCoreApplication.translate("MainWindow", u"Elige una provincia", None))
        self.buscadorProvincia.setItemText(0, QCoreApplication.translate("MainWindow", u"Valencia", None))
        self.buscadorProvincia.setItemText(1, QCoreApplication.translate("MainWindow", u"Alicante", None))
        self.buscadorProvincia.setItemText(2, QCoreApplication.translate("MainWindow", u"Castellon", None))

        self.mostrarButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.informacion.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Proyecto App Covid", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.menuAbout_App.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

