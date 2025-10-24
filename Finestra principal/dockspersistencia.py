from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel
from PySide6.QtCore import QSettings, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persistència de docks")
        self.setCentralWidget(QLabel("Contingut principal", alignment=Qt.AlignCenter))

        # Creem alguns docks
        dock1 = QDockWidget("Dock esquerre")
        # Asignamos un nombre únic a cada dock per a la persistència
        dock1.setObjectName("dockEsquerre")
        dock1.setWidget(QLabel("Verd", alignment=Qt.AlignCenter))
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        dock2 = QDockWidget("Dock dret")
        # Asignamos un nombre únic a cada dock per a la persistència
        dock2.setObjectName("dockCret")
        dock2.setWidget(QLabel("Blau", alignment=Qt.AlignCenter))
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        # Recuperem la configuració guardada (si existeix)
        self.settings = QSettings("CIPFPBatoi", "DI-DocksDemo")
        # "geometry" → posición y tamaño de la ventana.
        # "windowState" → estado visual (maximizada, minimizada, disposición de dock widgets, etc.).
        if self.settings.value("geometry") and self.settings.value("windowState"):
            self.restoreGeometry(self.settings.value("geometry"))
            self.restoreState(self.settings.value("windowState"))
    # Event representa el evento de cierre de la ventana. Que hacer cuando se cierra la ventana.
    def closeEvent(self, event):
        # Guardem l’estat abans de tancar
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        # Llama al método original de la clase padre (QMainWindow.closeEvent) para que Qt complete el cierre correctamente.
        # Es importante incluirlo, porque si no, la ventana podría no cerrarse del todo o no liberar bien los recursos.
        super().closeEvent(event)

app = QApplication()
finestra = MainWindow()
finestra.resize(700, 400)
finestra.show()
app.exec()
