from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel
from PySide6.QtCore import QSettings, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persistència de docks")
        self.setCentralWidget(QLabel("Contingut principal", alignment=Qt.AlignCenter))

        # Creem alguns docks
        dock1 = QDockWidget("Dock esquerre")
        dock1.setWidget(QLabel("Verd", alignment=Qt.AlignCenter))
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        dock2 = QDockWidget("Dock dret")
        dock2.setWidget(QLabel("Blau", alignment=Qt.AlignCenter))
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        # Recuperem la configuració guardada (si existeix)
        self.settings = QSettings("CIPFPBatoi", "DI-DocksDemo")
        if self.settings.value("geometry") and self.settings.value("windowState"):
            self.restoreGeometry(self.settings.value("geometry"))
            self.restoreState(self.settings.value("windowState"))

    def closeEvent(self, event):
        # Guardem l’estat abans de tancar
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        super().closeEvent(event)

app = QApplication(sys.argv)
finestra = MainWindow()
finestra.resize(700, 400)
finestra.show()
sys.exit(app.exec())
