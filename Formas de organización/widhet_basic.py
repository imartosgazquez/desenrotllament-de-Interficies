from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class Contenedor(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        caja = Contenedor("green")
        self.setCentralWidget(caja)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()