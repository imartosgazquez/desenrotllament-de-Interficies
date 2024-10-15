from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from pathlib import Path  #es una clase dentro de pathlib que representa rutas de sistema de archivos.

def absPath(file):
    # Devuelve la ruta absoluta a un fichero desde el propio script
    return str(Path(__file__).parent.absolute() / file)
    # Path(__file__) Crea un objeto Path que representa la ruta relativa del script actual.
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(280, 120))
        self.setMaximumSize(QSize(280, 120))
        # creamos la imagen
        imagen = QPixmap(absPath("prueba.jpg"))
        print(absPath("naturaleza.jpg"))

        # widget etiqueta
        etiqueta = QLabel(self)

        # la asginamos a la etiqueta
        etiqueta.setPixmap(imagen)

        # establecemos el widget central
        self.setCentralWidget(etiqueta)

        # establecemos unas flags de alineamiento
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # hacemos que se escale con la ventana 
        etiqueta.setScaledContents(True) 
      

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()