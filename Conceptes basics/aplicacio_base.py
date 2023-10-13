from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication()
window = QMainWindow()
window.setWindowTitle("Hola mundo")

# Guardamos el botón en una variable
button = QPushButton("Soy un botón")
# Establecemos el botón como widget central de la ventana principal
window.setCentralWidget(button)

window.show()
app.exec_()