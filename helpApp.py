from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class helpApp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About App")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.layout = QVBoxLayout()
        msg = QLabel("Como usar la app\n" 
                     "1. Seleccione una provincia.\n"
                     "2. Eliga un municipio.\n"
                     "3. Pulsa mostrar.")

        self.layout.addWidget(msg)
        self.buttonBox.accepted.connect(self.accept)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)