# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(494, 373)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 461, 321))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.user_lbl = QLabel(self.horizontalLayoutWidget)
        self.user_lbl.setObjectName(u"user_lbl")

        self.verticalLayout.addWidget(self.user_lbl)

        self.username_le = QLineEdit(self.horizontalLayoutWidget)
        self.username_le.setObjectName(u"username_le")

        self.verticalLayout.addWidget(self.username_le)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.password_le = QLineEdit(self.horizontalLayoutWidget)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setAutoFillBackground(False)
        self.password_le.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_le.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_le)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.verticalLayout_2)

        self.submit_login_btn = QPushButton(self.horizontalLayoutWidget)
        self.submit_login_btn.setObjectName(u"submit_login_btn")
        self.submit_login_btn.setEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.submit_login_btn)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 494, 21))
        Login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        self.submit_login_btn.setDefault(True)


        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.user_lbl.setText(QCoreApplication.translate("Login", u"Nom d'utilisateur :", None))
        self.username_le.setText("")
        self.label_2.setText(QCoreApplication.translate("Login", u"Mot de passe", None))
        self.submit_login_btn.setText(QCoreApplication.translate("Login", u"Valider", None))
    # retranslateUi

