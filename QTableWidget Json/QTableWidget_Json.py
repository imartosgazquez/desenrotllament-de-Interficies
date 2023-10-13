from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem)
import json
from PySide6.QtCore import Qt  

dades=[]
dades.append({
        "nom":"Juan",
        "ocupació":"Profesor",
        "email":"djfd@s.com"
    })

contactes=[
        ("Jose","Programador","sfhjd@sdfsdf.com"),
        ("Lorena","Analista","sfhjd@sdfsdf.com"),
        ("Paco","Expert Python","sfhjd@sdfsdf.com"),
    ]

for nombre, empleo, email in contactes:
        dades.append({
            "nom": nombre,
            "ocupació": empleo,
            "email": email
        })

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #creació i escritura de fitxer json amb les dades
        with open(("contactes.json"),"w") as fitxer:
            json.dump(dades,fitxer)

        #lectura del fitxer json
        with open(("contactes.json"),"r") as fitxer:
            self.dades=json.load(fitxer)
            for contacte in dades:
                print(contacte["nom"],contacte["ocupació"],contacte["email"])

                self.tabla=QTableWidget()
                self.columnas=["nom","ocupació","email"]
                self.tabla.setRowCount(len(self.dades))
                
                self.tabla.setColumnCount(len(self.columnas))
                
                self.tabla.setHorizontalHeaderLabels(self.columnas)
                print(self.tabla)

        for i, fila in enumerate(self.dades):
            for j, columna in enumerate(self.columnas):
                item=QTableWidgetItem()
                item.setData(Qt.EditRole,fila[columna])
                self.tabla.setItem(i,j,item)

        #redimensionem les columnes
        self.tabla.resizeColumnsToContents()
        #camviem titols
        self.tabla.setHorizontalHeaderItem(0,QTableWidgetItem("Nom"))
        self.tabla.setHorizontalHeaderItem(1,QTableWidgetItem("Ocupació"))
        self.tabla.setHorizontalHeaderItem(2,QTableWidgetItem("Email"))
        self.tabla.itemChanged.connect(self.celdaModificada)
        self.setCentralWidget(self.tabla)

    def celdaModificada(self,item):
        fila, camp=item.row(),self.columnas[item.column()]
        self.dades[fila][camp]=item.data(Qt.EditRole)
        with open(("contactos.json"),"w") as fitxer:
            json.dump(self.dades,fitxer)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()