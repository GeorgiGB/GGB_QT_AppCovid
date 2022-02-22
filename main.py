# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtCharts

import aboutApp
import login
from interface import *
from urlRequest import urlRequest


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Cargar los datos del urlRequest
        self.datos = urlRequest()

        # Boton de login
        self.ui.actionLogout.triggered.connect(self.logoutButton)

        # Boton sobre la app
        self.ui.actionAbout_App_2.triggered.connect(self.aboutApp)

        # Mostrar la lista de una provincia
        self.ui.buscadorProvincia.currentTextChanged.connect(self.cargarMunicipio)

        # Mostrar grafico de una ciudad/pueblo

        self.ui.mostrarButton.clicked.connect(self.mostrarGrafica)

        # Boton de salida
        self.ui.actionExit.triggered.connect(lambda: sys.exit())

    # Boton que permite desconectar la sesion
    def logoutButton(self):
        var1 = login.LoginWindow()
        var1.show()
        if var1.isVisible():
            self.hide()

    # Informacion sobre la aplicacion
    def aboutApp(self):
        info = aboutApp.aboutApp()
        info.exec()

    def cargarMunicipio(self):
        self.ui.buscadorCiudad.clear()
        if self.ui.buscadorProvincia.currentIndex() == 0:
            for x in self.datos.arrayVlc:
                self.ui.buscadorCiudad.addItem(x['Municipi'])

        if self.ui.buscadorProvincia.currentIndex() == 1:
            for x in self.datos.arrayAlicante:
                self.ui.buscadorCiudad.addItem(x['Municipi'])

        if self.ui.buscadorProvincia.currentIndex() == 2:
            for x in self.datos.arrayCastellon:
                self.ui.buscadorCiudad.addItem(x['Municipi'])

    def mostrarGrafica(self):
        set0 = QtCharts.QBarSet("Casos PCR+")
        set1 = QtCharts.QBarSet("Incidencia acumulada PCR+")
        set2 = QtCharts.QBarSet("Casos PCR+ 14 dias")
        set3 = QtCharts.QBarSet("Defuncions")



        # Muestra casos de las ciudades dependiendo de la eleccion del municipio

        # 0 es Valencia

        for x in self.datos.arrayVlc:
            if x['Municipi'] == self.ui.buscadorCiudad.currentText():
                set0.append(int(float(x['Casos PCR+'])))
                set1.append(int(str(x['Incidència acumulada PCR+']).replace(" ", "").split(",")[0]))
                set2.append(int(float(x['Casos PCR+ 14 dies'])))
                set3.append(int(float(x['Defuncions'])))

        # 1 es Alicante

        for x in self.datos.arrayAlicante:
            if x['Municipi'] == self.ui.buscadorCiudad.currentText():
                set0.append(int(float(x['Casos PCR+'])))
                set1.append(int(str(x['Incidència acumulada PCR+']).replace(" ", "").split(",")[0]))
                set2.append(int(float(x['Casos PCR+ 14 dies'])))
                set3.append(int(float(x['Defuncions'])))

        # 2 es Castellon

        for x in self.datos.arrayCastellon:
            if x['Municipi'] == self.ui.buscadorCiudad.currentText():
                set0.append(int(float(x['Casos PCR+'])))
                set1.append(int(str(x['Incidència acumulada PCR+']).replace(" ", "").split(",")[0]))
                set2.append(int(float(x['Casos PCR+ 14 dies'])))
                set3.append(int(float(x['Defuncions'])))

        series = QtCharts.QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Contagios Covid últimos 14 Dias")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis = QtCharts.QBarCategoryAxis()
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(sizePolicy)
        self.ui.chart_view.setFixedSize(QSize(400, 300))
        self.ui.grafico_2.addWidget(self.ui.chart_view, 0, 0, 0, 0)
