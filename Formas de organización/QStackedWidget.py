from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QStackedWidget, QPushButton, QLabel
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QStackedWidget")

        # Creamos el stacked widget
        self.stack = QStackedWidget()

        # Creamos tres "pantallas"
        pantalla1 = self.crear_pantalla("🟢 Pantalla 1", "lightgreen")
        pantalla2 = self.crear_pantalla("🔵 Pantalla 2", "lightblue")
        pantalla3 = self.crear_pantalla("🔴 Pantalla 3", "lightcoral")

        # Las añadimos a la pila
        self.stack.addWidget(pantalla1)
        self.stack.addWidget(pantalla2)
        self.stack.addWidget(pantalla3)

        # Botones de navegación
        boton1 = QPushButton("Mostrar pantalla 1")
        boton2 = QPushButton("Mostrar pantalla 2")
        boton3 = QPushButton("Mostrar pantalla 3")

        boton1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        boton2.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        boton3.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        #El código anterior con lambdas equivale a
        #def cambiar_pantalla():
           # self.stack.setCurrentIndex(0)
           # boton1.clicked.connect(cambiar_pantalla)


        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def crear_pantalla(self, texto, color):
        """Crea una pantalla simple con color de fondo y texto centrado."""
        etiqueta = QLabel(texto)
        etiqueta.setAlignment(Qt.AlignCenter)
        etiqueta.setStyleSheet(f"background-color: {color}; font-size: 24px; padding: 40px;")
        return etiqueta


if __name__ == "__main__":
    app = QApplication()
    ventana = MainWindow()
    ventana.show()
    app.exec()
