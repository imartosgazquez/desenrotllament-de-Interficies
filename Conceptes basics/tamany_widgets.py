from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize # Nuevo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        button = QPushButton("Hola")
        self.setCentralWidget(button)

        # Redimensión simple
        #self.resize(480, 320)
        # Tamaño mínimo de la ventana
        self.setMinimumSize(QSize(480, 320))
 # Tamaño máximo de la ventana
        self.setMaximumSize(QSize(880, 320))


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()