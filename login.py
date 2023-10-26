from PySide6.QtWidgets import QMainWindow
from client import Client  # Import your Client class
from ui_login import Ui_Login
from mainwindow import MainWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.login_button = self.ui.submit_login_btn
        self.login_button.clicked.connect(self.handle_submit_login_btn)

    def handle_submit_login_btn(self):
        username = self.ui.username_le.text()
        password = self.ui.password_le.text()

        client = Client(user=username, password=password)

        if client.login():
            # Close the LoginWindow
            self.close()

            # Open the MainWindow
            self.main_window = MainWindow(client)
            self.main_window.show()


            print("Login successful")
        else:
            print("Login failed")
