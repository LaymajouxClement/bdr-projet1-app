import sys
from mainwindow import MainWindow
from login import LoginWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QCoreApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())
