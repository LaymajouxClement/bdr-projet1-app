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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
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
        self.equipe_tv.setGeometry(QRect(20, 10, 521, 311))
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
        self.tabWidget_3 = QTabWidget(self.admin_tab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(10, 0, 571, 381))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.menu_tw.addTab(self.admin_tab, "")
        self.params_tab = QWidget()
        self.params_tab.setObjectName(u"params_tab")
        self.verticalLayoutWidget = QWidget(self.params_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(29, 19, 531, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

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
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.menu_tw.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


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
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Calendrier", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Arbitre", None))
        self.menu_tw.setTabText(self.menu_tw.indexOf(self.admin_tab), QCoreApplication.translate("MainWindow", u"Administration", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nom D'utilisateur : {USERNAME}", None))
        self.disconnect_btn.setText(QCoreApplication.translate("MainWindow", u"Se D\u00e9connecter", None))
        self.menu_tw.setTabText(self.menu_tw.indexOf(self.params_tab), QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
    # retranslateUi

