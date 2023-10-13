from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path

def absPath(file):
    # Devuelve la ruta absoluta a un fichero desde el propio script
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 320))
        # creamos la imagen
        imagen = QPixmap(absPath("prueba.jpg"))

        # widget etiqueta
        etiqueta = QLabel(self)

        # la asginamos a la etiqueta
        etiqueta.setPixmap(imagen)

        # establecemos el widget central
        self.setCentralWidget(etiqueta)

        # establecemos unas flags de alineamiento
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
      

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()