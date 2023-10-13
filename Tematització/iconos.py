from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QStyle)  # edited
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor  # nuevo
import sys
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # recuperamos el icono de la libería estandard de la ventana
        icono = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        # lo podemos asignar a un botón
        boton = QPushButton(icono, "Botón guardar")

        self.setCentralWidget(boton)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # creamos nuestra paleta de colores
    paleta = QPalette()
    paleta.setColor(QPalette.Window, QColor(51, 51, 51))
    paleta.setColor(QPalette.WindowText, QColor(235, 235, 235))

    # activamos la paleta en la aplicación
    app.setPalette(paleta)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())