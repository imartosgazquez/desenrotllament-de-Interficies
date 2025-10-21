from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog)  # editado
from PySide6.QtCore import QTranslator, QLibraryInfo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        fichero, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", ".")
        #fichero, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ".")
        print(fichero)

if __name__ == "__main__":
    app = QApplication()

    # envolvemos la aplicación con el traductor
    translator = QTranslator(app)
    # recuperamos el directorio de traducciones
    translations = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    print(translations)
    # cargamos la traducción en el traductor
    translator.load("qt_es", translations)
    # la aplicamos
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    app.exec()
