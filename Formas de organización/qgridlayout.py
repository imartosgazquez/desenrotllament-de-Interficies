from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QGridLayout, QWidget)
import sys




class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout en cuadrícula
        cuadricula = QGridLayout()

        # añadimos widgets en las celdas usando los índices
        cuadricula.addWidget(Caja("orange"), 0, 0)
        cuadricula.addWidget(Caja("purple"), 1, 1)
        cuadricula.addWidget(Caja("magenta"), 2, 2)
        cuadricula.addWidget(Caja("gray"), 2, 0)
        cuadricula.addWidget(Caja("red"), 0, 2)


        # cremos el widget dummy y le asignamos el layout horizontal
        widget = QWidget()
        widget.setLayout(cuadricula)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()