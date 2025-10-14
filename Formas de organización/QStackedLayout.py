from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QStackedLayout, QWidget
from PySide6.QtCore import Qt

class Caja(QLabel):
    def __init__(self, color):
        super().__init__(color)              # muestro el nombre del color
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(300, 200)        # tamaño razonable
        self.setStyleSheet(f"background-color:{color}; color:white; font-size:24px;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        pila = QStackedLayout()
        pila.addWidget(Caja("orange"))
        pila.addWidget(Caja("magenta"))
        pila.addWidget(Caja("purple"))
        pila.addWidget(Caja("red"))

        contenedor = QWidget()
        contenedor.setLayout(pila)
        self.setCentralWidget(contenedor)

        # guardar la referencia para usarla en keyPressEvent
        self.pila = pila

        # asegurar que recibimos eventos de teclado
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()

    def keyPressEvent(self, event):
        idx = self.pila.currentIndex()
        max_idx = self.pila.count() - 1

        if event.key() == Qt.Key_Right:
            idx += 1
        elif event.key() == Qt.Key_Left:
            idx -= 1
        else:
            # dejar que otras teclas se manejen como siempre
            return super().keyPressEvent(event)

        # efecto “infinito”
        if idx > max_idx:
            idx = 0
        elif idx < 0:
            idx = max_idx

        self.pila.setCurrentIndex(idx)
        # y ahora sí, pasamos al comportamiento por defecto
        super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec()
