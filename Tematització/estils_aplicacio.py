from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLineEdit, QSpinBox)
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario = QFormLayout()

        formulario.addRow("Nombre", QLineEdit("Hector"))
        formulario.addRow("Email", QLineEdit(text="hola@ejemplo.com"))
        formulario.addRow("Edad", QSpinBox(value=32))

        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
     # estilo fusion
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())