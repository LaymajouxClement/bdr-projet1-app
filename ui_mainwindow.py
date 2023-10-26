# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(677, 486)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_tw = QTabWidget(self.centralwidget)
        self.menu_tw.setObjectName(u"menu_tw")
        self.menu_tw.setEnabled(True)
        self.menu_tw.setGeometry(QRect(20, 0, 601, 421))
        self.tables_tab = QWidget()
        self.tables_tab.setObjectName(u"tables_tab")
        self.horizontalLayoutWidget = QWidget(self.tables_tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 411, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.table_lbl = QLabel(self.horizontalLayoutWidget)
        self.table_lbl.setObjectName(u"table_lbl")
        self.table_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.table_lbl)

        self.table_cb = QComboBox(self.horizontalLayoutWidget)
        self.table_cb.setObjectName(u"table_cb")

        self.horizontalLayout.addWidget(self.table_cb)

        self.submit_table_cb_btn = QPushButton(self.horizontalLayoutWidget)
        self.submit_table_cb_btn.setObjectName(u"submit_table_cb_btn")

        self.horizontalLayout.addWidget(self.submit_table_cb_btn)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.table_tv = QTableView(self.tables_tab)
        self.table_tv.setObjectName(u"table_tv")
        self.table_tv.setGeometry(QRect(20, 100, 551, 271))
        self.menu_tw.addTab(self.tables_tab, "")
        self.stats_tab = QWidget()
        self.stats_tab.setObjectName(u"stats_tab")
        self.tabWidget_2 = QTabWidget(self.stats_tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 40, 561, 331))
        self.score_tab = QWidget()
        self.score_tab.setObjectName(u"score_tab")
        self.equipe_tv = QTableView(self.score_tab)
        self.equipe_tv.setObjectName(u"equipe_tv")
        self.equipe_tv.setGeometry(QRect(20, 10, 521, 281))
        self.tabWidget_2.addTab(self.score_tab, "")
        self.stade_tab = QWidget()
        self.stade_tab.setObjectName(u"stade_tab")
        self.stade_tv = QTableView(self.stade_tab)
        self.stade_tv.setObjectName(u"stade_tv")
        self.stade_tv.setGeometry(QRect(10, 10, 531, 311))
        self.tabWidget_2.addTab(self.stade_tab, "")
        self.stat_generator_btn = QPushButton(self.stats_tab)
        self.stat_generator_btn.setObjectName(u"stat_generator_btn")
        self.stat_generator_btn.setGeometry(QRect(10, 10, 191, 24))
        self.menu_tw.addTab(self.stats_tab, "")
        self.admin_tab = QWidget()
        self.admin_tab.setObjectName(u"admin_tab")
        self.admin_tab.setEnabled(True)
        self.admin_site_tab = QTabWidget(self.admin_tab)
        self.admin_site_tab.setObjectName(u"admin_site_tab")
        self.admin_site_tab.setGeometry(QRect(10, 0, 571, 381))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget = QWidget(self.tab_4)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 20, 461, 238))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.equipeB_cb = QComboBox(self.gridLayoutWidget)
        self.equipeB_cb.setObjectName(u"equipeB_cb")
        self.equipeB_cb.setEnabled(False)

        self.gridLayout.addWidget(self.equipeB_cb, 4, 2, 1, 1)

        self.arbitre_cb_lbl = QLabel(self.gridLayoutWidget)
        self.arbitre_cb_lbl.setObjectName(u"arbitre_cb_lbl")
        self.arbitre_cb_lbl.setEnabled(False)

        self.gridLayout.addWidget(self.arbitre_cb_lbl, 5, 1, 1, 1)

        self.create_calendrier_btn = QPushButton(self.gridLayoutWidget)
        self.create_calendrier_btn.setObjectName(u"create_calendrier_btn")
        self.create_calendrier_btn.setEnabled(False)

        self.gridLayout.addWidget(self.create_calendrier_btn, 7, 2, 1, 1)

        self.eqB_cb_lbl = QLabel(self.gridLayoutWidget)
        self.eqB_cb_lbl.setObjectName(u"eqB_cb_lbl")
        self.eqB_cb_lbl.setEnabled(False)

        self.gridLayout.addWidget(self.eqB_cb_lbl, 4, 1, 1, 1)

        self.equipeA_cb = QComboBox(self.gridLayoutWidget)
        self.equipeA_cb.setObjectName(u"equipeA_cb")
        self.equipeA_cb.setEnabled(False)

        self.gridLayout.addWidget(self.equipeA_cb, 3, 2, 1, 1)

        self.create_form_calendrier_btn = QPushButton(self.gridLayoutWidget)
        self.create_form_calendrier_btn.setObjectName(u"create_form_calendrier_btn")

        self.gridLayout.addWidget(self.create_form_calendrier_btn, 1, 0, 1, 1)

        self.stade_cb_lbl = QLabel(self.gridLayoutWidget)
        self.stade_cb_lbl.setObjectName(u"stade_cb_lbl")
        self.stade_cb_lbl.setEnabled(False)

        self.gridLayout.addWidget(self.stade_cb_lbl, 2, 1, 1, 1)

        self.arbitre_cb = QComboBox(self.gridLayoutWidget)
        self.arbitre_cb.setObjectName(u"arbitre_cb")
        self.arbitre_cb.setEnabled(False)

        self.gridLayout.addWidget(self.arbitre_cb, 5, 2, 1, 1)

        self.stade_cb = QComboBox(self.gridLayoutWidget)
        self.stade_cb.setObjectName(u"stade_cb")
        self.stade_cb.setEnabled(False)

        self.gridLayout.addWidget(self.stade_cb, 2, 2, 1, 1)

        self.eqA_cb_lbl = QLabel(self.gridLayoutWidget)
        self.eqA_cb_lbl.setObjectName(u"eqA_cb_lbl")
        self.eqA_cb_lbl.setEnabled(False)

        self.gridLayout.addWidget(self.eqA_cb_lbl, 3, 1, 1, 1)

        self.calendrier_date_de = QDateTimeEdit(self.gridLayoutWidget)
        self.calendrier_date_de.setObjectName(u"calendrier_date_de")
        self.calendrier_date_de.setEnabled(False)

        self.gridLayout.addWidget(self.calendrier_date_de, 6, 2, 1, 1)

        self.admin_site_tab.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tableView = QTableView(self.tab_5)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 30, 531, 192))
        self.match_edit_btn = QPushButton(self.tab_5)
        self.match_edit_btn.setObjectName(u"match_edit_btn")
        self.match_edit_btn.setEnabled(False)
        self.match_edit_btn.setGeometry(QRect(390, 270, 80, 24))
        self.lineEdit = QLineEdit(self.tab_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(240, 270, 141, 24))
        self.lineEdit_2 = QLineEdit(self.tab_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QRect(20, 270, 91, 24))
        self.lineEdit_3 = QLineEdit(self.tab_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QRect(130, 270, 91, 24))
        self.admin_site_tab.addTab(self.tab_5, "")
        self.menu_tw.addTab(self.admin_tab, "")
        self.params_tab = QWidget()
        self.params_tab.setObjectName(u"params_tab")
        self.verticalLayoutWidget = QWidget(self.params_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(29, 19, 531, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.username_lbl = QLabel(self.verticalLayoutWidget)
        self.username_lbl.setObjectName(u"username_lbl")

        self.verticalLayout.addWidget(self.username_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.disconnect_btn = QPushButton(self.verticalLayoutWidget)
        self.disconnect_btn.setObjectName(u"disconnect_btn")

        self.verticalLayout.addWidget(self.disconnect_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.menu_tw.addTab(self.params_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 677, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.menu_tw.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.admin_site_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.table_lbl.setText(QCoreApplication.translate("MainWindow", u"Choix de la table :", None))
        self.submit_table_cb_btn.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.menu_tw.setTabText(self.menu_tw.indexOf(self.tables_tab), QCoreApplication.translate("MainWindow", u"Tables", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.score_tab), QCoreApplication.translate("MainWindow", u"Score Equipe", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.stade_tab), QCoreApplication.translate("MainWindow", u"Meilleur Stade", None))
        self.stat_generator_btn.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer les Statistiques", None))
        self.menu_tw.setTabText(self.menu_tw.indexOf(self.stats_tab), QCoreApplication.translate("MainWindow", u"Statistiques", None))
        self.arbitre_cb_lbl.setText(QCoreApplication.translate("MainWindow", u"Choix de l'Arbitre: ", None))
        self.create_calendrier_btn.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er", None))
        self.eqB_cb_lbl.setText(QCoreApplication.translate("MainWindow", u"Choix de l'Equipe B: ", None))
        self.create_form_calendrier_btn.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9voir un nouveau match", None))
        self.stade_cb_lbl.setText(QCoreApplication.translate("MainWindow", u"Choix du stade:", None))
        self.eqA_cb_lbl.setText(QCoreApplication.translate("MainWindow", u"Choix de l'Equipe A: ", None))
        self.admin_site_tab.setTabText(self.admin_site_tab.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Calendrier", None))
        self.match_edit_btn.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Nombre de Spectateurs", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Nbr buts ClubA", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Nbr buts ClubB", None))
        self.admin_site_tab.setTabText(self.admin_site_tab.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Match", None))
        self.menu_tw.setTabText(self.menu_tw.indexOf(self.admin_tab), QCoreApplication.translate("MainWindow", u"Administration", None))
        self.username_lbl.setText(QCoreApplication.translate("MainWindow", u"Nom D'utilisateur : {USERNAME}", None))
        self.disconnect_btn.setText(QCoreApplication.translate("MainWindow", u"Se D\u00e9connecter", None))
        self.menu_tw.setTabText(self.menu_tw.indexOf(self.params_tab), QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
    # retranslateUi

