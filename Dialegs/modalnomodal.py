from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QLabel, QVBoxLayout

class InfoDialog(QDialog):
    def __init__(self, titulo, texto, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(texto))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modal vs No modal")
        btn_modal = QPushButton("Abrir diálogo MODAL")
        btn_no_modal = QPushButton("Abrir diálogo NO modal")
        btn_modal.clicked.connect(self.abrir_modal)
        btn_no_modal.clicked.connect(self.abrir_no_modal)

        w = QPushButton("Interacción principal (prueba a pulsarme)")
        w.setText("Botón principal")
        self.setCentralWidget(w)

        self.addToolBar("Demo").addWidget(btn_modal)
        self.addToolBar("Demo").addWidget(btn_no_modal)

    def abrir_modal(self):
        dlg = InfoDialog("Modal", "Bloquea interacción con la ventana principal", self)
        dlg.setModal(True)      # explícito (exec() ya lo hace modal)
        dlg.exec()              # Bloqueante

    def abrir_no_modal(self):
        self.dlg = InfoDialog("No modal", "No bloquea, puedes seguir usando la ventana principal", self)
        self.dlg.setModal(False)
        self.dlg.show()         # No bloqueante

app = QApplication()
win = MainWindow()
win.resize(420, 200)
win.show()
app.exec()
