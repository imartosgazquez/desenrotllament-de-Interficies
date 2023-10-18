from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow, QLabel):
    def __init__(self):
        QMainWindow.__init__(self)
        QLabel.__init__(self)
        self.etiqueta = QLabel()
        self.setCentralWidget(self.etiqueta)
        self.etiqueta.setStyleSheet(f"background-color:green")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()