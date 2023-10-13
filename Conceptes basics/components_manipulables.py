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
        
        # Señal para controlar el botón como un altenrador true/salse
        button.setCheckable(True)
        button.clicked.connect(self.boton_alternador)
        self.button = button

    def boton_alternador(self, valor):
        if valor:
            self.button.setText("Estoy activado")
        else:
            self.button.setText("Estoy desactivado")


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()