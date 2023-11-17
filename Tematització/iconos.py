from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStyle)  # edited
from PySide6.QtGui import QPalette, QColor  # nuevo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # recuperamos el icono de la libería estandard de la ventana
        icono = self.style().standardIcon(QStyle.SP_ArrowForward)
        # lo podemos asignar a un botón
        boton = QPushButton(icono, "Botón guardar")

        self.setCentralWidget(boton)

if __name__ == "__main__":
    app = QApplication()

    # creamos nuestra paleta de colores
    paleta = QPalette()
    paleta.setColor(QPalette.Window, QColor(51, 51, 51))
    paleta.setColor(QPalette.WindowText, QColor(235, 235, 235))

    # activamos la paleta en la aplicación
    app.setPalette(paleta)

    window = MainWindow()
    window.show()
    app.exec_()