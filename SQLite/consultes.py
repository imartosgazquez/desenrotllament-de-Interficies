import sqlite3  # Librería para la gestión de bases de datos SQLite
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery 
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QTableView, QMessageBox)

class FinestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexió amb SQLite")  

        # Configuración de la conexión con QSqlDatabase
        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName("SQLite/contactos.db")

        print(conexion.databaseName(), conexion.connectionName())

        if not conexion.open():
            print("No se pudo conectar a la BD")
            exit(True)
        
        # Creación de la tabla
        consulta = QSqlQuery()
        consulta.exec("""
            CREATE TABLE IF NOT EXISTS personas
            (    
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(40) NOT NULL,
                empleo VARCHAR(50),
                email VARCHAR(60) NOT NULL         
            )"""
        )
        conexion.close()

        # Añadimos un nuevo registro
        nom, ocupacio, email = "Iván", "Profesor", "i.martos@profesor.com"

        # Conexión con la base de datos y verificación de ISBN único
        connection = sqlite3.connect("SQLite/contactos.db")
        # Crea un cursor que permite interactuar con la base de datos 
        # a través de connection. Con este cursor, puedes ejecutar 
        # consultas SQL
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO personas (nombre, empleo, email) VALUES (?, ?, ?)", (nom, ocupacio, email))
            connection.commit()  # Guarda los cambios
            QMessageBox.information(self, "Persona afegida correctament", "La persona ha estat afegida correctament.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Ha ocorregut un error: {str(e)}")

        # Configuración de la tabla que muestra los datos de la base de datos
        self.taula = QTableView()
        model = QSqlTableModel()
        model.setTable("personas")  # Nombre de la tabla en la base de datos
        model.select()
        self.taula.setModel(model)

        # Oculta la columna de la ID
        self.taula.setColumnHidden(0, True)

        # Ajusta el tamaño de las columnas para que se adapten al contenido
        self.taula.resizeColumnsToContents()

        self.setCentralWidget(self.taula)  # Define la tabla como el widget central

        # Realizamos una consulta para ver los datos
        cursor.execute("SELECT nombre, empleo, email FROM personas")
        rows = cursor.fetchall()  # Obtiene todas las filas de la consulta

        for row in rows:
            print(row[0], row[1], row[2])  # Accede a cada columna por su índice
        connection.close()

# Punto de inicio de la aplicación
if __name__ == "__main__":
    app = QApplication()
    finestra = FinestraPrincipal()
    finestra.show()  # Muestra la ventana principal
    app.exec()  # Inicia el bucle de la aplicación
