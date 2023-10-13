from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize # Nuevo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        button = QPushButton("Hola")
        self.setCentralWidget(button)

        # Tamaño mínimo del widget
        self.setMinimumSize(QSize(480, 320))
        # Tamaño máximo del widget
        self.setMaximumSize(QSize(480, 320))
        # Tamaño fijo del widget
        self.setFixedSize(QSize(480, 320))
        # Definimos un receptor para conectar la señal clicked a un método
        button.clicked.connect(self.boton_clicado)
        # Pulsación y liberación
        button.pressed.connect(self.boton_pulsado)
        button.released.connect(self.boton_liberado)
        # Señal para controlar el botón como un altenrador true/salse
        button.setCheckable(True)
        button.clicked.connect(self.boton_alternador)

    def boton_pulsado(self):
        print("¡Me has pulsado!")

    def boton_liberado(self):
        print("¡Me has liberado!")

    def boton_clicado(self):
        print("¡Me has clicado!")

    def boton_alternador(self, valor):
        print("¿Alternado?", valor)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()