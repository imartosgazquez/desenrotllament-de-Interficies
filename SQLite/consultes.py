import sys
from PySide6.QtSql import (
    QSqlDatabase, QSqlTableModel, QSqlQuery
)
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QTableView, QMessageBox,
    QWidget, QVBoxLayout, QStatusBar
)
from PySide6.QtCore import Qt


class FinestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexió amb SQLite")
        self.resize(600, 550)

        # 1) Conexión a la BD SQLite/contactos.db
        self._connectar_bd()

        # 2) Crear tabla si no existe
        self._crear_taula_si_no_existe()

        # 3) Insertar registro de ejemplo solo si la tabla está vacía
        self._insertar_demo_si_cal()

        # 4) Crear el modelo SQL y la vista (tabla)
        self._configurar_model_i_taula()

        # 5) Conectar la señal de selección de fila
        self._conectar_seleccio_fila()

        # 6) Montar el layout central
        self._montar_interficie_central()

        # 7) Barra de estado con recuento de registros
        self._configurar_statusbar()
        self._actualitzar_statusbar()

    # ------------------------------------------------------------------
    # BD / DATOS
    # ------------------------------------------------------------------

    def _connectar_bd(self):
        """
        Abre (o crea) la BD SQLite en el archivo local SQLite/contactos.db
        y deja la conexión abierta en self.db para usarla en todo el programa.
        """
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("SQLite/contactos.db")

        if not self.db.open():
            QMessageBox.critical(
                self,
                "Error BD",
                "No s'ha pogut obrir la BD SQLite/contactos.db"
            )
            sys.exit(1)

    def _crear_taula_si_no_existe(self):
        """
        Crea la tabla 'personas' si aún no existe.
        """
        consulta = QSqlQuery()
        consulta.exec(
            """
            CREATE TABLE IF NOT EXISTS personas
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre  VARCHAR(40) NOT NULL,
                empleo  VARCHAR(50),
                email   VARCHAR(60) NOT NULL
            )
            """
        )

    def _taula_buida(self):
        """
        Devuelve True si la tabla 'personas' está vacía.
        """
        consulta = QSqlQuery("SELECT COUNT(*) FROM personas")
        if consulta.next(): #Se situa en el primer (y único) resultado
            total = consulta.value(0)
            return total == 0
        return True

    def _insertar_demo_si_cal(self):
        """
        Inserta un registro de ejemplo SOLO si la tabla está vacía.
        Así los alumnos ven datos nada más ejecutar.
        """
        if not self._taula_buida():
            return

        nom = "Iván"
        ocupacio = "Professor"
        correo = "i.martos@profesor.com"

        consulta = QSqlQuery()
        consulta.prepare(
            "INSERT INTO personas (nombre, empleo, email) VALUES (?, ?, ?)"
        )
        consulta.addBindValue(nom)
        consulta.addBindValue(ocupacio)
        consulta.addBindValue(correo)

        if not consulta.exec():
            QMessageBox.warning(
                self,
                "Error inserció",
                "No s'ha pogut inserir el registre inicial."
            )

    # ------------------------------------------------------------------
    # MODELO Y TABLA
    # ------------------------------------------------------------------

    def _configurar_model_i_taula(self):
        """
        Crea el modelo QSqlTableModel vinculado a la tabla 'personas'
        y la QTableView para mostrar los datos.
        """
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("personas")

        # Estrategia OnFieldChange:
        # cualquier cambio en la celda se guarda directamente en la BD.
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

        # Ejecuta una consulta SELECT para cargar los datos de la tabla personas en el modelo.
        self.model.select()

        # Nombres bonitos para las columnas visibles
        self.model.setHeaderData(1, Qt.Horizontal, "Nom")
        self.model.setHeaderData(2, Qt.Horizontal, "Emplec")
        self.model.setHeaderData(3, Qt.Horizontal, "Email")

        # Creamos la vista de tabla
        self.taula = QTableView()
        self.taula.setModel(self.model)

        # Ocultar la columna ID (columna 0)
        self.taula.setColumnHidden(0, True)

        # Ajustar tamaño de columnas
        self.taula.resizeColumnsToContents()

    def _conectar_seleccio_fila(self):
        """
        Conecta la señal de cambio de fila seleccionada.
        Cuando el usuario selecciona una fila en la tabla,
        leemos sus datos y los mostramos (por consola y en la barra de estado).
        """
        sel_model = self.taula.selectionModel() #emite señales cuando cambia la selección en la tabla
        sel_model.currentRowChanged.connect(self._fila_seleccionada_canvia) #emite señal cuando cambia la fila seleccionada
        #envia la fila actual seleccionada y la anterior seleccionada (current, previous)

    # ------------------------------------------------------------------
    # SELECCIÓN DE FILA
    # ------------------------------------------------------------------

    def _fila_seleccionada_canvia(self, current, previous):
        """
        current = nueva fila seleccionada
        previous = fila seleccionada antes
        Leemos los datos de la fila actual del modelo y los mostramos.
        """
        if not current.isValid():
            print("Sense selecció")
            return

        fila = current.row()

        # Ojo: Aquí estamos leyendo directamente del modelo base (self.model),
        # no de la vista (self.taula), porque la vista puede tener filtros o
        # estar ordenada de forma diferente. Por eso usamos current.row() para obtener
        # la fila correcta en el modelo base.
        idx_nom = self.model.index(fila, 1)    # columna 'nombre'
        idx_emp = self.model.index(fila, 2)    # columna 'empleo'
        idx_cor = self.model.index(fila, 3)    # columna 'email'

        nom = self.model.data(idx_nom)
        emp = self.model.data(idx_emp)
        correo = self.model.data(idx_cor)

        print("Fila seleccionada:")
        print(" - Nom   :", nom)
        print(" - Emplec:", emp)
        print(" - Email :", correo)

        # Feedback visual rápido en la barra de estado
        self.statusBar().showMessage(f"Seleccionat: {nom} ({emp})")

    # ------------------------------------------------------------------
    # UI CENTRAL Y STATUS BAR
    # ------------------------------------------------------------------

    def _montar_interficie_central(self):
        """
        Creamos un QWidget contenedor con un layout vertical simple.
        Ahora solo contiene la tabla, porque en esta versión
        NO incluimos buscador ni otros controles.
        """
        contenidor = QWidget()
        layout = QVBoxLayout(contenidor)
        layout.addWidget(self.taula)

        self.setCentralWidget(contenidor)

    def _configurar_statusbar(self):
        """
        Crea una QStatusBar para mostrar info de estado.
        """
        barra = QStatusBar()
        self.setStatusBar(barra)

    def _actualitzar_statusbar(self):
        """
        Muestra cuántos registros hay en la BD.
        """
        consulta = QSqlQuery("SELECT COUNT(*) FROM personas")
        total = 0
        if consulta.next():
            total = consulta.value(0)

        self.statusBar().showMessage(f"{total} contactes en la BD")


# Punto de inicio de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = FinestraPrincipal()
    finestra.show()
    app.exec()
