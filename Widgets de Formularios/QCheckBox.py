from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox  # edited
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos una casilla y la establecemos de widget central
        casilla = QCheckBox("Casilla de verificación")
        self.setCentralWidget(casilla)

        # señal para detectar cambios en la casilla
        casilla.stateChanged.connect(self.estado_cambiado)

        # la podemos desactivar
        casilla.setEnabled(False)

        # establecemos el triestado por defecto, también funcionan los otros dos
        casilla.setCheckState(Qt.PartiallyChecked)

    def estado_cambiado(self, estado):
        if (estado==2):
            print("Casilla marcada")
        if (estado==0):
            print("Casilla desmarcada")
        if (estado==1):
            print("Casilla parcialmente desmarcada")


if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()