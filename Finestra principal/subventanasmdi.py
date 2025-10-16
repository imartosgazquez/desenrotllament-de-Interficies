from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QMdiSubWindow,
                               QTextEdit, QToolBar, QPushButton)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfície MDI")

        # Àrea MDI com a widget central
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # Barra d'eines per gestionar subfinestres
        tb = QToolBar("MDI")
        self.addToolBar(tb)

        boto_nova = QPushButton("Nova subfinestra")
        boto_cascada = QPushButton("Cascada")
        boto_mosaic = QPushButton("Mosaic")

        boto_nova.clicked.connect(self.nova_subfinestra)
        boto_cascada.clicked.connect(self.mdi.cascadeSubWindows)
        boto_mosaic.clicked.connect(self.mdi.tileSubWindows)

        tb.addWidget(boto_nova)
        tb.addWidget(boto_cascada)
        tb.addWidget(boto_mosaic)

    def nova_subfinestra(self):
        editor = QTextEdit()
        editor.setPlainText("Contingut de la subfinestra")
        sub = QMdiSubWindow()
        sub.setWidget(editor)
        sub.setWindowTitle(f"Document {len(self.mdi.subWindowList()) + 1}")
        self.mdi.addSubWindow(sub)
        sub.show()

app = QApplication(sys.argv)
finestra = MainWindow()
finestra.resize(700, 450)
finestra.show()
sys.exit(app.exec())
