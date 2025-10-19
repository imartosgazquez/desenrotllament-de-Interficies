from PySide6.QtWidgets import (QPushButton, QSizePolicy, QApplication, 
QMainWindow, QWidget, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QStackedWidget")
        
        layout = QVBoxLayout()
        b1 = QPushButton("Fixe")
        b1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        b2 = QPushButton("Expansiu")
        b2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(b1)
        layout.addWidget(b2)
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