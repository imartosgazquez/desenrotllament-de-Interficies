from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QFormLayout, QWidget, QLineEdit)
from PySide6.QtCore import Qt  

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout en formulario
        formulario = QFormLayout()

        # añadimos widgets con etiquetas en filas
        formulario.addRow("Nombre",QLineEdit("Tu nombre aquí"))
        formulario.addRow("Campo 2", Caja("purple"))
        formulario.addRow("Magenta", Caja("magenta"))
        formulario.addRow("Gris", Caja("gray"))
        formulario.addRow("Campo 5", Caja("red"))

        # configuraciones extra
        formulario.setLabelAlignment(Qt.AlignRight)
        formulario.setFormAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # cremos el widget dummy y le asignamos el layout
        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()