from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QMessageBox)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

        boton = QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)

    def boton_clicado(self):
        # creamos un diálogo de tipo cuestión
        #dialogo = QMessageBox.question(self, "Diálogo de cuestión", "Esta es una pregunta de prueba")
        #dialogo = QMessageBox.about(self, "Acerca de", "<p>Información del programa</p><p>Segundo parágrado</p>")
        #dialogo = QMessageBox.critical(self, "Diálogo de error", "Ha ocurrido algo malo")
        #dialogo = QMessageBox.information(self, "Diálogo informativo", "Esto es un texto informativo")
        #dialogo = QMessageBox.warning(self, "Diálogo de aviso", "Cuidado con este diálogo")
        dialogo = QMessageBox.warning(self, "Diálogo de aviso", "¿Estás seguro de aplicar los cambios?", buttons=QMessageBox.Apply | QMessageBox.Cancel, defaultButton=QMessageBox.Cancel)

        if dialogo == QMessageBox.Apply:
            print("Aplicamos los cambios")
        else:
            print("Cancelamos los cambios")

        if dialogo == QMessageBox.Ok:
            print("He presionado el botón OK")

        # ahora podemos comprobar qué tipo de botón se devuelve
        if dialogo == QMessageBox.Yes:
            print("Ha respondido sí")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())