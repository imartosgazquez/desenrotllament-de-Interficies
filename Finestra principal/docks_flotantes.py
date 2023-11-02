from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QStatusBar, 
                               QToolBar, QLabel, QDockWidget)
from PySide6.QtCore import Qt 
from PySide6.QtGui import QAction, QIcon
from pathlib import Path

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        self.construir_menu()
        # construimos las herramientas
        self.construir_herramientas()
        # añadimos los docks
        self.construir_docks()
        # creamos una caja como widget central de la ventana principal
        self.setCentralWidget(Caja("gray"))

    def construir_docks(self):
        # creamos un dock
        dock1 = QDockWidget()
        # le damos un título (optativo)
        dock1.setWindowTitle("DOCK 1")
        # establecemos el widget que contendrá
        dock1.setWidget(Caja("green"))
        # ancho mínimo (optativo)
        dock1.setMinimumWidth(100)
        dock1.setFeatures(QDockWidget.NoDockWidgetFeatures | QDockWidget.DockWidgetFloatable |
        QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable)
        # tamaños (optativos)
        dock1.setMinimumWidth(125)
        dock1.setMinimumHeight(100)
        dock1.setMinimumSize(125, 100)
        # lo añadimos en una posición de la ventana principal
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        # creamos más docks para jugar con ellos
        dock2 = QDockWidget()
        dock2.setWindowTitle("DOCK 2")
        dock2.setWidget(Caja("yellow"))
        dock2.setMinimumSize(125, 100)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        dock3 = QDockWidget()
        dock3.setWindowTitle("DOCK 3")
        dock3.setWidget(Caja("blue"))
        dock3.setMinimumSize(125, 100)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock3)

        

    def construir_menu(self):
        # Recuperamos la barra de menú
        menu = self.menuBar()

        # Añadimos un menú de archivo
        menu_archivo = menu.addMenu("&Menú")
        # Añadimos una acción de prueba
        menu_archivo.addAction("&Prueba")
        # Añadimos un submenú
        submenu_archivo = menu_archivo.addMenu("&Submenú")
        # Añadimos una acción de prueba
        submenu_archivo.addAction("Subopción &1")
        submenu_archivo.addAction("Subopción &2")
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
        # accesores de clase
        self.accion_info = accion_info

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")

    def construir_herramientas(self):
        # Creamos una barra de herramientas
        herramientas = QToolBar("Barra de herramientas principal")
        # Podemos agregar la acción salir implícitamente
        herramientas.addAction(QIcon(absPath("exit.png")), "S&alir", self.close)
        # O añadir una acción ya creada para reutilizar código
        herramientas.addAction(self.accion_info)
        # La añadimos a la ventana principal
        self.addToolBar(herramientas)

    def mostrar_info(self):
        dialogo = QMessageBox.information(self, "Diálogo informativo", "Esto es un texto informativo")
        
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()