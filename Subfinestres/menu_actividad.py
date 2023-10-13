from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar, QLabel,QVBoxLayout, QWidget)
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
from PySide6.QtGui import QPixmap
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class Subventana(QWidget):
    def __init__(self,animal):
        super().__init__()
        # Le damos un tamaño y un título
        self.resize(240, 120)
        self.setWindowTitle("Subventana animal")
        # creamos la imagen
        if animal == "perro":
            imagen = QPixmap(absPath("perro.jpeg"))
        else:
            imagen = QPixmap(absPath("mono.jpeg"))

        # creamos etiqueta para volcar la imagen en un layout
        etiqueta = QLabel(self)
        # la asginamos a la etiqueta
        etiqueta.setPixmap(imagen)
        # creamos un layout y añadimos la etiqueta
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        # asignamos el layout al widget
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        # construimos nuestro menú
        self.construir_menu()

    def construir_menu(self):
        # Recuperamos la barra de menú
        menu = self.menuBar()

        # Añadimos un menú de archivo
        menu_archivo = menu.addMenu("&Menú")
        # Añadimos una acción de prueba
        menu_archivo.addAction("&Prueba")
        
        
        subopcio=menu_archivo.addMenu("Submenú")
        self.accio2=QAction(QIcon(absPath("perro.jpeg")),"Botó 2")
        self.accio3=QAction(QIcon(absPath("mono.jpeg")),"Botó 3")
        subopcio.addAction(self.accio2)
        subopcio.addAction(self.accio3)
        self.accio2.triggered.connect(lambda: self.mostrar_animal("perro"))
        self.accio3.triggered.connect(lambda: self.mostrar_animal("mono"))
        # Añadimos un separador
        menu_archivo.addSeparator()
        # Añadimos una acción completa
        menu_archivo.addAction(
            QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")

        # Añadimos un menú de ayuda
        menu_ayuda = menu.addMenu("Ay&uda")
        # Creamos una acción específica para mostrar información
        accion_info = QAction("&Información", self)
        # Podemos configurar un icono en la acción
        accion_info.setIcon(QIcon(absPath("info.png")))
        # También podemos especificar un accesor
        accion_info.setShortcut("Ctrl+I")
        # Le configuramos una señal para ejecutar un método
        accion_info.triggered.connect(self.mostrar_info)
        # Añadimos un texto de ayuda
        accion_info.setStatusTip("Muestra información irrelevante")
        # Añadimos la acción al menú
        menu_ayuda.addAction(accion_info)

        # Añadimos una barra de estado
        self.setStatusBar(QStatusBar(self))

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")
        
    def mostrar_animal(self, animal):
        self.subventana = Subventana(animal)
        self.subventana.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())