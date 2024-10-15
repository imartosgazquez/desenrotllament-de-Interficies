from PySide6.QtSql import QSqlDatabase, QSqlQuery
import sys

conexion=QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName("SQLite/contactos.db")

print(conexion.databaseName(),conexion.connectionName())


if not conexion.open():
    print("No se puedo conectar a la BD")
    sys.exit(True)

consulta=QSqlQuery()
consulta.exec("DROP TABLE IF EXISTS contactos")
consulta.exec("""
    CREATE TABLE IF NOT EXISTS contactos
    (    
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(40) NOT NULL,
        empleo VARCHAR(50),
        email VARCHAR(60) NOT NULL         
        )"""
    )

#afegim un nou registre
nom, ocupacio, email="Juan","Professor","jmateu.inf@gmail.com"

consulta.exec(f"""
    INSERT INTO contactos(nombre,empleo,email)
    VALUES('{nom}','{ocupacio}','{email}')
""")

#preparem la consulta
consulta.prepare(
    "INSERT INTO contactos(nombre,empleo,email) VALUES (?,?,?)"
)

#afegim nous registres a la bd segons la preparació anterior
consulta.addBindValue("pepe")
consulta.addBindValue("analista")
consulta.addBindValue("pepe@gmail.com")
consulta.exec()

#per a fer consultes sql
consulta.exec("SELECT nombre,empleo,email FROM contactos")

#hem de recorrer els diferents registres segons la consulta anterior
while consulta.next():
    print(consulta.value("nombre"),
          consulta.value("empleo"),
          consulta.value("email"))

#tanquem la connexió
conexion.close()

