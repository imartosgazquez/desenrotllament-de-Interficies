from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(Caja("green"))
        # le añadimos unas cuantas cajas
        layout.addWidget(Caja("green"))
        layout.addWidget(Caja("blue"))
        layout.addWidget(Caja("red"))

        # modificamos los márgenes
        layout.setContentsMargins(15,5,15,5)
        # modificamos el espaciado
        layout.setSpacing(10)

        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout)

        # establecemos el dummy widget como widget central
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()