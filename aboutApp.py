from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class aboutApp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About App")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.layout = QVBoxLayout()
        msg = QLabel("Esta aplicación muestra con una grafica los casos de covid "
                     "entre todas las ciudades de la Comunidad Valenciana")
        self.layout.addWidget(msg)
        self.buttonBox.accepted.connect(self.accept)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



