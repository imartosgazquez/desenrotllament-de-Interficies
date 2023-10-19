from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QTabWidget,QLineEdit)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout de pestañas
        tabs = QTabWidget()

        # Añadimos varios widgets como pestañas con nombres
        tabs.addTab(QLineEdit(), "Uno")
        tabs.addTab(Caja("magenta"), "Dos")
        tabs.addTab(Caja("purple"), "Tres")
        tabs.addTab(Caja("red"), "Cuatro")

        tabs.setTabPosition(QTabWidget.West)  # West, East, North, South

        # asignamos las pestañas como widget central
        self.setCentralWidget(tabs)
        tabs.setMovable(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())