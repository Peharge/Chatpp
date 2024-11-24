import json
from PyQt5.QtWidgets import QLineEdit, QFormLayout, QStackedWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QInputDialog
from PyQt5.QtWidgets import QFrame
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
import subprocess
from PyQt5.QtWidgets import QMessageBox
import ctypes
from ctypes import wintypes
from PyQt5 import QtGui
import sys
from PyQt5 import QtGui, QtWidgets
import ctypes
from ctypes import wintypes


class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chat++ mini Pro')
        self.setGeometry(1000, 200, 600, 600)

        self.setWindowIcon(QtGui.QIcon(
            'peharge-logo3.6.ico'))

        myappid = u'mycompany.myproduct.subproduct.version'  # Arbritary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        icon_path = "peharge-logo3.6.ico"
        self.setWindowIcon(QIcon(icon_path))

        background_color = QColor(255, 255, 255)
        self.setStyleSheet("background-color: rgb({},{},{})".format(
            background_color.red(), background_color.green(),
            background_color.blue()))

        self.setWindowOpacity(0.85)

        glass_frame = QFrame(self)
        glass_frame.setGeometry(200, 200, 600, 600)
        glass_frame.setStyleSheet("""
                    background-color: rgba(255, 255, 255, 255);
                    border-radius: 10px;
                """)

        icon_path = "peharge-logo3.6.ico"
        self.setWindowIcon(QIcon(icon_path))

        self.accounts_file = 'accounts.json'
        self.load_accounts()

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.login_frame = self.create_login_frame()
        self.create_account_frame = self.create_account_creation_frame()

        self.central_widget.addWidget(self.login_frame)
        self.central_widget.addWidget(self.create_account_frame)

    def create_login_frame(self):
        frame = QFrame(self)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Lade das Bild und skaliere es
        image_path = r"C:\Users\julia\OneDrive - Gewerbeschule Lörrach\Pictures\software\peharge-logo3.62.png"
        pixmap = QPixmap(image_path).scaled(170, 170, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label = QLabel()
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        form_layout = QFormLayout()
        form_layout.setFormAlignment(Qt.AlignCenter)
        form_layout.setLabelAlignment(Qt.AlignLeft)

        space_widget = QWidget(self)
        space_widget.setFixedHeight(40)  # Höhe des Zeilenabstands festlegen
        layout.addWidget(space_widget)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("User name")
        self.user_input.setFont(QFont('Roboto', 12))
        self.user_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                padding: 10px;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)

        user_label = QLabel('User name:', self)
        user_label.setFont(QFont('Roboto', 15))
        form_layout.addRow(user_label, self.user_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFont(QFont('Roboto', 12))
        self.password_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                padding: 10px;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        password_label = QLabel('Password:', self)
        password_label.setFont(QFont('Roboto', 15))
        form_layout.addRow(password_label, self.password_input)

        layout.addLayout(form_layout)

        self.login_button = QPushButton('Sign in', self)
        self.login_button.setStyleSheet("""
            QPushButton {
                font-size: 15px;
                color: black;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                margin-top: 20px;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
            QPushButton:hover {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.create_account_button = QPushButton('Create an account', self)
        self.create_account_button.setStyleSheet("""
            QPushButton {
                font-size: 15px;
                color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                background-color: #ffffff;
                border: none;
                margin-top: 10px;
            }
            QPushButton:hover {
                color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        self.create_account_button.clicked.connect(self.show_create_account_frame)
        layout.addWidget(self.create_account_button, alignment=Qt.AlignCenter)

        self.delete_account_button = QPushButton('Delete account', self)
        self.delete_account_button.setStyleSheet("""
            QPushButton {
                font-size: 15px;
                color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                background-color: #ffffff;
                border: none;
                margin-top: 10px;
            }
            QPushButton:hover {
                color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        self.delete_account_button.clicked.connect(self.delete_account)
        layout.addWidget(self.delete_account_button, alignment=Qt.AlignCenter)

        frame.setLayout(layout)
        return frame

    def create_account_creation_frame(self):
        frame = QFrame(self)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Lade das Bild und skaliere es
        image_path = r"C:\Users\julia\OneDrive - Gewerbeschule Lörrach\Pictures\software\peharge-logo3.62.png"
        pixmap = QPixmap(image_path).scaled(170, 170, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label = QLabel()
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        form_layout = QFormLayout()
        form_layout.setFormAlignment(Qt.AlignCenter)
        form_layout.setLabelAlignment(Qt.AlignLeft)

        space_widget = QWidget(self)
        space_widget.setFixedHeight(40)  # Höhe des Zeilenabstands festlegen
        layout.addWidget(space_widget)

        self.new_user_input = QLineEdit()
        self.new_user_input.setPlaceholderText("User name")
        self.new_user_input.setFont(QFont('Roboto', 12))
        self.new_user_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                padding: 10px;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        new_user_label = QLabel('User name:', self)
        new_user_label.setFont(QFont('Roboto', 15))
        form_layout.addRow(new_user_label, self.new_user_input)

        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText("Password")
        self.new_password_input.setEchoMode(QLineEdit.Password)
        self.new_password_input.setFont(QFont('Roboto', 12))
        self.new_password_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                padding: 10px;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        new_password_label = QLabel('Password:', self)
        new_password_label.setFont(QFont('Roboto', 15))
        form_layout.addRow(new_password_label, self.new_password_input)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm Password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setFont(QFont('Roboto', 12))
        self.confirm_password_input.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                padding: 10px;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                border-radius: 5px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        confirm_password_label = QLabel('Confirm Password:', self)
        confirm_password_label.setFont(QFont('Roboto', 15))
        form_layout.addRow(confirm_password_label, self.confirm_password_input)

        layout.addLayout(form_layout)

        self.create_account_button = QPushButton('Create', self)
        self.create_account_button.setStyleSheet("""
            QPushButton {
                font-size: 15px;
                color: black;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                margin-top: 20px;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
            QPushButton:hover {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        self.create_account_button.clicked.connect(self.create_account)
        layout.addWidget(self.create_account_button, alignment=Qt.AlignCenter)

        self.back_button = QPushButton('Back', self)
        self.back_button.setStyleSheet("""
            QPushButton {
                font-size: 15px;
                color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
                background-color: #ffffff;
                border: none;
                margin-top: 10px;
            }
            QPushButton:hover {
                color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #000000, stop: 1 #808080);
            }
        """)
        self.back_button.clicked.connect(self.show_login_frame)
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        frame.setLayout(layout)
        return frame

    def show_create_account_frame(self):
        self.central_widget.setCurrentWidget(self.create_account_frame)

    def show_login_frame(self):
        self.central_widget.setCurrentWidget(self.login_frame)

    def load_accounts(self):
        try:
            with open(self.accounts_file, 'r') as file:
                self.accounts = json.load(file)
        except FileNotFoundError:
            self.accounts = {}

    def save_accounts(self):
        with open(self.accounts_file, 'w') as file:
            json.dump(self.accounts, file)

    def login(self):
        username = self.user_input.text()
        password = self.password_input.text()
        if username in self.accounts and self.accounts[username] == password:
            QMessageBox.information(self, 'Login Successful', 'You have successfully logged in.')
            self.run_batch_file()
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid username or password.')

    def run_batch_file(self):
        batch_file = 'start_test7-c.bat'  # Hier den Dateinamen der Batch-Datei angeben
        subprocess.Popen([batch_file], shell=True)

    def create_account(self):
        username = self.new_user_input.text()
        password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()
        if password != confirm_password:
            QMessageBox.warning(self, 'Error', 'Passwords do not match.')
        elif username in self.accounts:
            QMessageBox.warning(self, 'Error', 'Username already exists.')
        else:
            self.accounts[username] = password
            self.save_accounts()
            QMessageBox.information(self, 'Success', 'Account created successfully.')
            self.show_login_frame()

    def delete_account(self):
        username, ok = QInputDialog.getText(self, 'Delete Account', 'Enter username:')
        if ok and username in self.accounts:
            del self.accounts[username]
            self.save_accounts()
            QMessageBox.information(self, 'Success', 'Account deleted successfully.')
        elif ok:
            QMessageBox.warning(self, 'Error', 'Username not found.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Setzt das Taskleistensymbol auch für QApplication
    icon_path = "peharge-logo3.6.ico"
    app.setWindowIcon(QtGui.QIcon(icon_path))
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
