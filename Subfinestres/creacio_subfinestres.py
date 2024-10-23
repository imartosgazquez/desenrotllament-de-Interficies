from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel)

class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        # Le damos un tamaño y un título
        self.resize(240, 120)
        self.setWindowTitle("Subventana")
        # creamos una etiqueta
        etiqueta = QLabel("Soy una subventana")
        # creamos un layout y añadimos la etiqueta
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        # asignamos el layout al widget
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Le damos un tamaño y un título
        self.setWindowTitle("Ventana principal")
        # dummy widget para un layout
        layout = QVBoxLayout(self)
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # botón para abrir la subventana
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)

    def mostrar_subventana(self):
        self.subventana = Subventana()
        self.subventana.show()

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()