from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QFontDialog, QColorDialog)  # new
from PySide6.QtCore import QTranslator, QLibraryInfo  # nuevo
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

        self.boton = boton

    def boton_clicado(self):
        confirmado, fuente = QFontDialog.getFont(self)
        if confirmado:
            #fuente es un objeto QFont
            self.boton.setFont(fuente)

   # def boton_clicado(self):
      #  color = QColorDialog.getColor()
       # if color.isValid():
        #    # color es un objeto QColor, name() devuelve su código hexadecimal
        #    self.boton.setStyleSheet(f"background-color: {color.name()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

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
    sys.exit(app.exec_())