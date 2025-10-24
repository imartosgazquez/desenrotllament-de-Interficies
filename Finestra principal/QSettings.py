from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QDialog, QFormLayout, QLineEdit, QHBoxLayout,
    QDialogButtonBox, QColorDialog
)
from PySide6.QtCore import QSettings, Qt

ORG = "CIPFPBatoi"
APP = "DI-PreferenciesBasic"

class PreferenciesBasicaDialog(QDialog):
    """Diàleg simple: demana nom i permet triar color."""
    def __init__(self, nom_inicial="", color_inicial="#ffffff", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preferències (bàsic)")

        # Estat intern
        self._nom = QLineEdit(nom_inicial or "")
        self._color_hex = color_inicial or "#ffffff"

        # Selector de color
        self._lbl_color = QLabel(self._color_hex)
        btn_color = QPushButton("Tria color…")
        btn_color.clicked.connect(self._elegir_color)

        fila_color = QHBoxLayout()
        fila_color.addWidget(self._lbl_color)
        fila_color.addWidget(btn_color)
        fila_color_w = QWidget()
        fila_color_w.setLayout(fila_color)

        # OK / Cancel
        botons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botons.accepted.connect(self.accept)
        botons.rejected.connect(self.reject)

        # Layout formulari
        lay = QFormLayout(self)
        lay.addRow("Nom d'usuari:", self._nom)
        lay.addRow("Color de fons:", fila_color_w)
        lay.addRow(botons)

    def _elegir_color(self):
        c = QColorDialog.getColor(parent=self, title="Tria un color de fons")
        if c.isValid():
            # Ejemplo 32a852
            self._color_hex = c.name()
            # Actualitza etiqueta
            self._lbl_color.setText(self._color_hex)

    def valores(self):
        """Retorna (nom, color_hex)."""
        return self._nom.text().strip(), self._color_hex


class MainWindow(QMainWindow):
    """Aplica i guarda nom i color amb QSettings. Sense menús/toolbars."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preferències bàsic (QSettings)")

        # QSettings
        self.settings = QSettings(ORG, APP)

        # Llig estat inicial (amb valors per defecte)
        nom = self.settings.value("nombre", "")
        color = self.settings.value("color_hex", "#ffffff")

        # Widgets
        self.lbl = QLabel(alignment=Qt.AlignCenter)
        self.btn = QPushButton("Preferències…")
        self.btn.clicked.connect(self._obrir_preferencies)
        
        root = QWidget()
        col = QVBoxLayout(root)
        col.addWidget(self.lbl)
        col.addWidget(self.btn, alignment=Qt.AlignCenter)
        
        self.setCentralWidget(root)

        # Aplica estat inicial
        self._aplica(nom, color)

    def _obrir_preferencies(self):
        # Llig valors actuals
        nom = self.settings.value("nombre", "")
        color = self.settings.value("color_hex", "#ffffff")

        # Obri diàleg amb els valors actuals
        dlg = PreferenciesBasicaDialog(nom_inicial=nom, color_inicial=color, parent=self)
        if dlg.exec():
            nom, color = dlg.valores()

            # Guarda a QSettings
            self.settings.setValue("nombre", nom)
            self.settings.setValue("color_hex", color)

            # Aplica a la UI
            self._aplica(nom, color)

    def _aplica(self, nom, color_hex):
        self.lbl.setText(f"Hola, {nom or 'usuari'}!")
        self.lbl.setStyleSheet(f"background-color: {color_hex};")


if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.resize(420, 220)
    w.show()
    app.exec()
