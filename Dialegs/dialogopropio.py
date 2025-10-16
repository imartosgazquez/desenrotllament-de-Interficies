from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog,
                               QLineEdit, QSpinBox, QFormLayout,
                               QDialogButtonBox, QMessageBox, QPushButton)
import sys

class UsuariDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nou usuari")

        # Camps del formulari
        self.nom = QLineEdit()
        self.edat = QSpinBox()
        self.edat.setRange(0, 120)

        # Botons d'acceptar/cancel·lar
        botons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botons.accepted.connect(self.valida_i_accepta)
        botons.rejected.connect(self.reject)

        # Disseny del formulari
        layout = QFormLayout(self)
        layout.addRow("Nom:", self.nom)
        layout.addRow("Edat:", self.edat)
        layout.addRow(botons)

    def valida_i_accepta(self):
        if not self.nom.text().strip():
            QMessageBox.warning(self, "Validació", "El nom no pot estar buit.")
            return
        if self.edat.value() < 18:
            QMessageBox.warning(self, "Validació", "Cal ser major de 18 anys.")
            return
        self.accept()  # Dades vàlides → tancar amb èxit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        boto = QPushButton("Afegir usuari")
        boto.clicked.connect(self.crea_usuari)
        self.setCentralWidget(boto)

    def crea_usuari(self):
        dlg = UsuariDialog(self)
        if dlg.exec():  # Si l’usuari accepta
            QMessageBox.information(self, "Acceptat",
                f"Usuari: {dlg.nom.text()} ({dlg.edat.value()} anys)")
        else:
            QMessageBox.information(self, "Cancel·lat", "Operació cancel·lada")

app = QApplication(sys.argv)
finestra = MainWindow()
finestra.resize(320, 160)
finestra.show()
sys.exit(app.exec())
