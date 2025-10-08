from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un campo numérico entero
        numero = QDoubleSpinBox()
        self.setCentralWidget(numero)

        # Probamos algunas opciones
        #numero.setMinimum(0)
        #numero.setMaximum(10)
        numero.setRange(0, 10)
        numero.setSingleStep(0.5)

       # numero.setPrefix("$")
        numero.setSuffix("€")

        # Probamos algunas señales
        numero.valueChanged.connect(self.valor_cambiado)

    def valor_cambiado(self, numero):
        print("Valor cambiado ->", numero)

if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()