from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout,QWidget
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout2.addWidget(Caja("red"))
        layout2.addWidget(Caja("yellow"))
        layout2.addWidget(Caja("purple"))
        layout1.addLayout(layout2)
        layout1.addWidget(Caja("green"))
        layout3.addWidget(Caja("red"))
        layout3.addWidget(Caja("purple"))
        layout1.addLayout(layout3)



        # modificamos los márgenes
        layout1.setContentsMargins(0,0,0,0)
        # modificamos el espaciado
        layout1.setSpacing(0)

        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout1)

        # establecemos el dummy widget como widget central
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()