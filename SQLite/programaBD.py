from PySide6.QtWidgets import(
    QApplication,QMainWindow,QTableView
)
from PySide6.QtSql import QSqlDatabase,QSqlTableModel

class FinestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexió amb SQLite")
       
        conexion=QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName("SQLite/contactos.db")

        if not conexion.open():
            print("No se puede conectar a la BDA")
            exit(True)

        self.taula=QTableView()
        model=QSqlTableModel()
        model.setTable("contactos")
        model.select()
        self.taula.setModel(model)

        #amaguem la columna de l'id
        self.taula.setColumnHidden(0,True)

        #canviem el tamany de les columnes
        self.taula.resizeColumnsToContents()

        self.setCentralWidget(self.taula)



if __name__ == "__main__":
    app=QApplication()
    finestra=FinestraPrincipal()
    finestra.show()
    app.exec()