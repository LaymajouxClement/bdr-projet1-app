from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from client import Client

class MainWindow(QMainWindow):
    def __init__(self,client):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # On défini le client
        self.client: Client = client

        self.items = []

        self.disconnect_button = self.ui.disconnect_btn
        self.disconnect_button.clicked.connect(self.handle_disconnect_btn)

        self.submit_table_cb_btn = self.ui.submit_table_cb_btn
        self.submit_table_cb_btn.clicked.connect(self.handle_submit_table_cb_btn)

        # on remplie le ComboBox
        self.fill_table_cb()

        self.stat_generator_btn = self.ui.stat_generator_btn
        self.stat_generator_btn.clicked.connect(self.handle_stat_generator_btn)

        # on enleve les pages stats + admin si region de l'user != Region1
        self.tab_manager()

    def tab_manager(self):
        if self.client.user != "Site1":
            self.ui.menu_tw.setTabEnabled(1, False)
            self.ui.menu_tw.setTabEnabled(2, False)

    def handle_disconnect_btn(self):
        self.close()
        # TODO re-open login

    def fill_table_cb(self):
        # TODO get tables
        sql = "SELECT table_name FROM user_tables"
        rows = self.client.query(sql)
        self.items = ["Choisir une table"]
        for row in rows:
            self.items.append(row[0]) # on ajoute le nom de la table
        self.ui.table_cb.addItems(self.items)

    def handle_submit_table_cb_btn(self):
        # si c'est autre que : Choisir une table on remplie la tableView
        choice = self.ui.table_cb.currentText()
        if choice != self.items[0]:
            sql = f"SELECT * FROM {choice}"
            rows = self.client.query(sql)
            # Create a model for the QTableView
            model = QStandardItemModel()

            # Set the number of rows and columns in the model
            model.setRowCount(len(rows))
            model.setColumnCount(len(rows[0]))  # Assuming all rows have the same number of columns

            # Populate the model with data
            for i, row in enumerate(rows):
                for j, cell in enumerate(row):
                    item = QStandardItem(str(cell))
                    model.setItem(i, j, item)

            # Set the model for the QTableView
            self.ui.table_tv.setModel(model)

    def handle_stat_generator_btn(self):
        # fill stade stats
        self.stat_generator_btn.setEnabled(False)

        sql = 'SELECT S.Nom AS "Nom du Stade", SUM(M.NbreSpectateurs) AS "Somme des Spectateurs"\
        FROM StadeSite1 S\
        JOIN MatchSite1 M ON S.Code = M.CodeStade\
        GROUP BY S.Nom\
        ORDER BY SUM(M.NbreSpectateurs) DESC'
        rows = self.client.query(sql)

        # Create a model for the QTableView
        model = QStandardItemModel()

        # Set the number of rows and columns in the model
        model.setRowCount(len(rows))
        model.setColumnCount(len(rows[0]))  # Assuming all rows have the same number of columns

        # Populate the model with data
        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                item = QStandardItem(str(cell))
                model.setItem(i, j, item)

        # Set the model for the QTableView
        self.ui.stade_tv.setModel(model)
        print(rows)
