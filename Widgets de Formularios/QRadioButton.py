from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton,QHBoxLayout,QWidget
from PySide6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        # creamos un botón radial y lo establecemos de widget central
        radial1 = QRadioButton("Botón radial 1")
        radial2 = QRadioButton("Botón radial 2")
        layout.addWidget(radial1)
        layout.addWidget(radial2)
        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # señal para detectar cambios en el botón
        radial1.toggled.connect(self.estado_cambiado)

        # Podemos activarla por defecto
        radial1.setChecked(True)

        # consultamos el valor actual
        print("¿Activada?", radial1.isChecked())

    def estado_cambiado(self, estado):
        if estado:
            print("Radial marcado")
        else:
            print("Radial desmarcado")

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()