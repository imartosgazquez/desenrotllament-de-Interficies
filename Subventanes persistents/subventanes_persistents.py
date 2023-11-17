from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit)
import random  # new



class Subventana(QWidget):
    def __init__(self):
        super().__init__()
        # Le damos un tamaño y un título
        self.resize(240, 120)
        self.setWindowTitle("Subventana")
      # creamos una etiqueta con texto aleatorio
        texto = QLineEdit()
        # creamos un layout y añadimos la etiqueta
        layout = QVBoxLayout()
        #layout.addWidget(etiqueta)
        layout.addWidget(texto)
        # asignamos el layout al widget
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Le damos un tamaño y un título
        self.setWindowTitle("Ventana principal")
        # dummy widget para un layout
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # botón para mostrar la subventana
        boton_abrir = QPushButton("Mostrar subventana")
        #boton_abrir.clicked.connect(lambda: self.subventana.show())
        boton_abrir.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_abrir)
        # botón para ocultar la subventana
        boton_cerrar = QPushButton("Ocultar subventana")
        #boton_cerrar.clicked.connect(lambda: self.subventana.hide())
        boton_cerrar.clicked.connect(self.ocultar_subventana)
        layout.addWidget(boton_cerrar)

        # creamos una instancia de la subventana
        self.subventana = Subventana()
    def mostrar_subventana(self):
        self.subventana.show()

    def ocultar_subventana(self):
        self.subventana.hide()
   

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()