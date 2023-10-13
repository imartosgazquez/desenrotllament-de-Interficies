from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox  # edited
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un desplegable
        desplegable = QComboBox()
        self.setCentralWidget(desplegable)

        desplegable.addItems(["Opción 1", "Opción 2", "Opción 3"])

        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_cambiado)

    def indice_cambiado(self, valor):
        print("Nuevo índice ->", valor)

    def texto_cambiado(self, texto):
        print("Nuevo texto ->", texto)

  

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()