from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit  # editado
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(pedro):
        super().__init__()
        pedro.setWindowTitle("Hola mundo")
        pedro.setMinimumSize(QSize(480, 320))

        # widget input de texto
        texto = QLineEdit()
        # capturamos la señal de texto cambiado
        texto.textChanged.connect(pedro.texto_modificado)

        # establecemos el widget central
        pedro.setCentralWidget(texto)

        # creamos el puntero
        pedro.texto = texto

    def texto_modificado(pedro):
        # recuperasmos el texto del input
        texto_recuperado = pedro.texto.text()
        # modificamos el título de la ventana al vuelo
        pedro.setWindowTitle(texto_recuperado)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()