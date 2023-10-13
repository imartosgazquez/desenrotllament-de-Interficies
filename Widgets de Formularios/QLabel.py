from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))

        # widget etiqueta
        etiqueta = QLabel("Soy una etiqueta")
        # establecemos el widget central
        self.setCentralWidget(etiqueta)

        # recuperamos la fuente por defecto
        fuente = etiqueta.font()
        # establecemos un tamaño
        fuente.setPointSize(24)
        # la asignamos a la etiqueta
        etiqueta.setFont(fuente)

        # establecemos unas flags de alineamiento
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
  

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()