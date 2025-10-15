from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QStackedWidget, QPushButton, QLabel
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QStackedWidget")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("A dalt"))  
        layout.addStretch()      # Espai flexible
        layout.addWidget(QLabel("A baix"))
        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout)

        # establecemos el dummy widget como widget central
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication()
    ventana = MainWindow()
    ventana.show()
    app.exec()
