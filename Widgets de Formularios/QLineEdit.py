from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un campo de texto
        texto = QLineEdit()
        self.setCentralWidget(texto)

        # Probamos algunas opciones
        texto.setMaxLength(10)
        texto.setPlaceholderText("Escribe máximo 10 caracteres")
        texto.setClearButtonEnabled(True)
        texto.setAlignment(Qt.AlignCenter)

        # Probamos algunas señales
        texto.textChanged.connect(self.texto_cambiado)
        texto.returnPressed.connect(self.enter_presionado)

    def texto_cambiado(self, texto):
        print("Texto cambiado ->", texto)

    def enter_presionado(self):
        # al presionar enter recuperamos el texto a partir del widget central
        texto = self.centralWidget().text()
        print("Enter presionado, texto ->", texto)


if __name__ == "__main__":
    app = QApplication([])
    ventana = MainWindow()
    ventana.show()
    app.exec()