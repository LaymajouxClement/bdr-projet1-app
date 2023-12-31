from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from client import Client

class MainWindow(QMainWindow):
    def __init__(self,client):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.username_lbl.setText(f"Nom d'utilisateur: {client.user}")

        # On défini le client
        self.client: Client = client

        self.items = []

        self.disconnect_button = self.ui.disconnect_btn
        self.disconnect_button.clicked.connect(self.handle_disconnect_btn)

        self.submit_table_cb_btn = self.ui.submit_table_cb_btn
        self.submit_table_cb_btn.clicked.connect(self.handle_submit_table_cb_btn)

        self.create_form_calendrier_btn = self.ui.create_form_calendrier_btn
        self.create_form_calendrier_btn.clicked.connect(self.handle_create_form_calendrier_btn)

        self.create_calendrier_btn = self.ui.create_calendrier_btn
        self.create_calendrier_btn.clicked.connect(self.handle_create_calendrier_btn)


        # on remplie le ComboBox
        self.fill_table_cb()

        self.stat_generator_btn = self.ui.stat_generator_btn
        self.stat_generator_btn.clicked.connect(self.handle_stat_generator_btn)

        # on enleve les pages stats + admin si region de l'user != Region1
        self.tab_manager()

        self.fill_match_admin_tv() # on met à jour la table d'administration des matchs
        self.ui.match_admin_tv.clicked.connect(self.handle_match_admin_tv)

        self.match_edit_btn = self.ui.match_edit_btn
        self.match_edit_btn.clicked.connect(self.handle_match_edit_btn)

        self.refresh_match_btn = self.ui.refresh_match_btn
        self.refresh_match_btn.clicked.connect(self.handle_refresh_match_btn)

        self.selected_match_admin = None

    def generate_table_view(self,sql):
        rows = self.client.query(sql)
        # Create a model for the QTableView
        model = QStandardItemModel()

        # Set the number of rows and columns in the model
        model.setRowCount(len(rows))
        if len(rows)>0:
            model.setColumnCount(len(rows[0]))  # Assuming all rows have the same number of columns

        # Populate the model with data
        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                item = QStandardItem(str(cell))
                model.setItem(i, j, item)

        return model


    def tab_manager(self):
        if self.client.user != "Site1":
            self.ui.menu_tw.setTabEnabled(1, False)
            # self.ui.menu_tw.setTabEnabled(2, False)
            self.ui.admin_site_tab.setTabEnabled(0,False)

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
            # print(sql)
            model = self.generate_table_view(sql)
            # Set the model for the QTableView
            self.ui.table_tv.setModel(model)

    def handle_stat_generator_btn(self):
        # self.stat_generator_btn.setEnabled(False)
        # fill stade stats
        self.stat_stade_generator()
        self.stat_equipe_generator()

    def stat_equipe_generator(self):
        sql = '''
        SELECT
            cs.CodeClub,
            cs.NomClub,
            SUM(
                CASE
                    WHEN (m.NbreButsClubA > m.NbreButsClubB AND c.ClubA = cs.CodeClub) OR
                         (m.NbreButsClubA < m.NbreButsClubB AND c.ClubB = cs.CodeClub) THEN 1
                    ELSE 0
                END
            ) AS "nbVictoires",
            SUM(
                CASE
                    WHEN (m.NbreButsClubA < m.NbreButsClubB AND c.ClubA = cs.CodeClub) OR
                         (m.NbreButsClubA > m.NbreButsClubB AND c.ClubB = cs.CodeClub) THEN 1
                    ELSE 0
                END
            ) AS "nbDefaites"
        FROM
            AllClubSportifSite1 cs
        JOIN
            calendriersite1 c ON  c.cluba = cs.codeclub OR c.clubb = cs.codeclub
        JOIN
            matchsite1 m ON c.codematch = m.codematch

        GROUP BY
            cs.CodeClub, cs.NomClub
        ORDER BY
            "nbVictoires" DESC, "nbDefaites" ASC'''

        model = self.generate_table_view(sql)
        self.ui.equipe_tv.setModel(model)

    def stat_stade_generator(self):
        sql = '''
        SELECT
            S.Nom AS "Nom du Stade",
            SUM(M.NbreSpectateurs) AS "Somme des Spectateurs"
        FROM AllStadeSite1 S
        JOIN MatchSite1 M
        ON
            S.Code = M.CodeStade
        GROUP BY
            S.Nom
        ORDER BY
            SUM(M.NbreSpectateurs) DESC'''


        # Set the model for the QTableView
        model = self.generate_table_view(sql)
        self.ui.stade_tv.setModel(model)

    def handle_create_form_calendrier_btn(self):
        # click du bouton "prévoir un nouveau match"
        # 1: activer le formulaire
        self.ui.arbitre_cb_lbl.setEnabled(True)
        self.ui.eqA_cb_lbl.setEnabled(True)
        self.ui.eqB_cb_lbl.setEnabled(True)
        self.ui.stade_cb_lbl.setEnabled(True)
        self.ui.arbitre_cb.setEnabled(True)
        self.ui.equipeA_cb.setEnabled(True)
        self.ui.equipeB_cb.setEnabled(True)
        self.ui.stade_cb.setEnabled(True)
        self.ui.calendrier_date_de.setEnabled(True)
        self.ui.create_calendrier_btn.setEnabled(True)

        self.fill_stade_cb()
        self.fill_equipes_cb()
        self.fill_arbitre_cb()

    def fill_stade_cb(self):
        sql ='''SELECT Nom FROM AllStadeSite1'''
        rows = self.client.query(sql)
        self.items = ["Choisir un Stade"]
        for row in rows:
            self.items.append(row[0]) # on ajoute le nom de la table
        self.ui.stade_cb.addItems(self.items)

    def fill_equipes_cb(self):
        sql ='''SELECT NomClub FROM AllClubSportifSite1'''
        rows = self.client.query(sql)
        self.items = ["Choisir une Equipe"]
        for row in rows:
            self.items.append(row[0]) # on ajoute le nom de la table
        self.ui.equipeA_cb.addItems(self.items)
        self.ui.equipeB_cb.addItems(self.items)

    def fill_arbitre_cb(self):
        sql ='''SELECT Code FROM ArbitreSite1'''
        rows = self.client.query(sql)
        self.items = ["Choisir un Arbitre"]
        for row in rows:
            self.items.append(str(row[0])) # on ajoute le nom de la table
        self.ui.arbitre_cb.addItems(self.items)

    def get_region_of_stade(self,nomstade_str):
        sql = f"""
            SELECT region
            FROM Site1.allstadesite1 s
            JOIN matchsite1 m
            ON m.codestade=s.code
            WHERE s.nom='{nomstade_str}'
        """
        print(sql)
        return self.client.query(sql)[0][0]

    def handle_create_calendrier_btn(self):
        stade = self.ui.stade_cb.currentText()
        equipeA = self.ui.equipeA_cb.currentText()
        equipeB = self.ui.equipeB_cb.currentText()
        arbitre = self.ui.arbitre_cb.currentText()
        date_match = self.ui.calendrier_date_de.date().toPython()
        heure_match = self.ui.calendrier_date_de.time().toPython()

        if equipeA == equipeB:
            return

        sql = f"""
        INSERT INTO
            MatchSite1(CodeMatch, NbreButsClubA, NbreButsClubB, NbreSpectateurs, CodeArbitre, CodeStade)
        VALUES(
            (SELECT MAX(CodeMatch)+1 FROM MatchSite1),
            0,
            0,
            0,
            {arbitre},
            (SELECT Code FROM AllStadeSite1 WHERE Nom='{stade}')
        )"""      
        # print(sql)
        self.client.query(sql)

        sql = f"""
        INSERT INTO
            CalendrierSite1(CodeMatch, DateMatch, Heure, ClubA, ClubB, Stade)
        VALUES(
            (SELECT MAX(CodeMatch) FROM MatchSite1),
            TO_DATE('{date_match}', 'YYYY-MM-DD'),
            TO_TIMESTAMP('{heure_match}', 'HH24:MI:SS'),
            (SELECT CodeClub FROM AllClubSportifSite1 WHERE NomClub='{equipeA}'),
            (SELECT CodeClub FROM AllClubSportifSite1 WHERE NomClub='{equipeB}'),
            (SELECT Code FROM AllStadeSite1 WHERE Nom='{stade}')
        )"""

        self.client.query(sql)
        # print(sql)

        self.client.commit() # on valide le commit

        self.ui.arbitre_cb_lbl.setEnabled(False)
        self.ui.eqA_cb_lbl.setEnabled(False)
        self.ui.eqB_cb_lbl.setEnabled(False)
        self.ui.stade_cb_lbl.setEnabled(False)
        self.ui.arbitre_cb.setEnabled(False)
        self.ui.equipeA_cb.setEnabled(False)
        self.ui.equipeB_cb.setEnabled(False)
        self.ui.stade_cb.setEnabled(False)
        self.ui.calendrier_date_de.setEnabled(False)
        self.ui.create_calendrier_btn.setEnabled(False)

        self.fill_match_admin_tv() # on met à jour la table d'administration des matchs

    def handle_refresh_match_btn(self):
        if self.client.user != "Site1":
            sql = f"""
            DROP MATERIALIZED VIEW Match{self.client.user}
            """
            self.client.query(sql)

            sql = f"""
            CREATE MATERIALIZED VIEW Match{self.client.user}
            REFRESH ON DEMAND
            AS
            SELECT m.CodeMatch, m.NbreButsClubA, m.NbreButsClubB, m.NbreSpectateurs, m.CodeArbitre, m.CodeStade
            FROM Site1.MatchSite1 m, Site1.AllStadeSite1 s
            WHERE m.CodeStade=s.Code AND s.region={self.client.user[-1]}
            """
            self.client.query(sql)
        self.fill_match_admin_tv()

    def fill_match_admin_tv(self):
        sql = f"""SELECT * FROM match{self.client.user}
        """
        model = self.generate_table_view(sql)
        self.ui.match_admin_tv.setModel(model)

    def handle_match_admin_tv(self,index):
        row = index.row()
        model = self.ui.match_admin_tv.model()

        # Ensure the model is a QStandardItemModel
        if isinstance(model, QStandardItemModel):
            num_columns = model.columnCount()

            row_data = []
            for column in range(num_columns):
                item = model.item(row, column)
                if item:
                    cell_data = item.text()
                    row_data.append(cell_data)
            self.selected_match_admin = row_data
            self.ui.nbreButsA_le.setEnabled(True)
            self.ui.nbreButsA_le.setText(row_data[1])
            self.ui.nbreButsB_le.setEnabled(True)
            self.ui.nbreButsB_le.setText(row_data[2])
            self.ui.nbreSpectateurs_le.setEnabled(True)
            self.ui.nbreSpectateurs_le.setText(row_data[3])
            self.ui.match_edit_btn.setEnabled(True)

    def handle_match_edit_btn(self):
        # TODO UPDATE the match
        codeMatch = self.selected_match_admin[0]
        try:
            nbrButsA = int(self.ui.nbreButsA_le.text())
            nbrButsB = int(self.ui.nbreButsB_le.text())
            nbrSpecs = int(self.ui.nbreSpectateurs_le.text())
        except:
            return
        if self.client.user != "Site1":
            sql = f"""
            UPDATE
                SITE1.matchsite1
            SET
                NbreButsClubA = {nbrButsA},
                NbreButsClubB = {nbrButsB},
                NbreSpectateurs = {nbrSpecs}
            WHERE
                CodeMatch={codeMatch}
            """
            self.client.query(sql)

            sql = f"""
            DROP MATERIALIZED VIEW Match{self.client.user}
            """
            self.client.query(sql)

            sql = f"""
            CREATE MATERIALIZED VIEW Match{self.client.user}
            REFRESH ON DEMAND
            AS
            SELECT m.CodeMatch, m.NbreButsClubA, m.NbreButsClubB, m.NbreSpectateurs, m.CodeArbitre, m.CodeStade
            FROM MatchSite1 m, AllStadeSite1 s
            WHERE m.CodeStade=s.Code AND s.region={self.client.user[-1]}
            """
            self.client.query(sql)


        self.ui.nbreButsA_le.setEnabled(False)
        self.ui.nbreButsB_le.setEnabled(False)
        self.ui.nbreSpectateurs_le.setEnabled(False)
        self.ui.match_edit_btn.setEnabled(False)

        self.fill_match_admin_tv() # on met à jour la table d'administration des matchs
