from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout cuadrícula")

        # Creamos un objeto layout cuadrícula
        layout_cuadrícula = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_cuadrícula)
        self.setCentralWidget(componente_principal)

        # Añadimos cuatro botones a a la primera fila
        layout_cuadrícula.addWidget(QPushButton('0,0'), 0, 0)
        layout_cuadrícula.addWidget(QPushButton('0,1'), 0, 1)
        
        # Añadimos un botón a la seguna fila que ocupe dos columnas
        layout_cuadrícula.addWidget(QPushButton('1,0-1'), 1, 0, 1, 2)
       


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
