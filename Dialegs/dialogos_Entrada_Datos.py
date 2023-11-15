from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QInputDialog)  # editado
from PySide6.QtCore import QTranslator, QLibraryInfo  # nuevo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = QInputDialog.getText(self, "Título", "Texto")
        print(dialogo)
        dialogo = QInputDialog.getInt(self, "Título", "Entero")
        print(dialogo)
        dialogo = QInputDialog.getDouble(self, "Título", "Decimal")
        print(dialogo)
        color, confirmado = QInputDialog.getItem(self, "Título",  "Colores", ["Rojo", "Azul", "Blanco", "Verde"])
        #if confirmado:
        print(color)


if __name__ == "__main__":
    app = QApplication()

    # envolvemos la aplicación con el traductor
    translator = QTranslator(app)
    # recuperamos el directorio de traducciones
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    # cargamos la traducción en el traductor
    translator.load("qt_es", translations)
    # la aplicamos
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    app.exec_()