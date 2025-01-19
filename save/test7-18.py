import sys
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QDateTime
import subprocess
import re
import time
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QListWidget, QListWidgetItem, QScrollArea, QDialog, QGridLayout, QFrame
import pyttsx3
from PyQt5.QtGui import QPixmap, QIcon, QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import Qt
import string
import json
import html
import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtCore import QDateTime, Qt
import html
import re
import json
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMainWindow
import docx
import os
from striprtf.striprtf import rtf_to_text
from odf.opendocument import load
from odf.text import P
import ctypes
from ctypes import wintypes
from PyQt5 import QtGui
import sys
from PyQt5 import QtGui, QtWidgets
import ctypes
from ctypes import wintypes
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QGraphicsDropShadowEffect, QScrollBar
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QFileDialog
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTabWidget, QWidget, QLabel, QLineEdit, QFormLayout, QPushButton
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt, QEvent
import PyPDF2
import torch

if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(torch.cuda.get_device_name(i))
        print(torch.cuda.get_device_capability(i))
        print(torch.cuda.get_device_properties(i))
else:
    print("CUDA is not available.")

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setup_chat_navigation()
        self.is_muted = False

    class MainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat++ mini Pro')
        self.setGeometry(0, 0, 1920, 1000)

        self.setWindowIcon(QtGui.QIcon(
            'C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico'))

        myappid = u'mycompany.myproduct.subproduct.version'  # Arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        background_color = QColor(34, 34, 34)
        self.setStyleSheet("background-color: rgb({},{},{})".format(
            background_color.red(), background_color.green(),
            background_color.blue()))

        self.setWindowOpacity(0.9)

        glass_frame = QFrame(self)
        glass_frame.setGeometry(0, 0, 1920, 1000)
        glass_frame.setStyleSheet("""
            background-color: rgb(34, 34, 34);
            color: #ffffff;
            border-radius: 10px;
        """)

        icon_path = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Ein Widget erstellen, das die Hauptlayout enthält
        central_widget = QWidget(self)

        # Vertikales Layout für das zentrale Widget erstellen
        layout = QVBoxLayout(central_widget)

        # Beispielinhalt hinzufügen, der länger als das Fenster ist
        for i in range(20):
            layout.addWidget(QScrollBar())

        self.setStyleSheet(
            """
            QScrollBar:vertical {
                background: #808080; /* Grau */
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #ffffff; /* Weiß */
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical {
                background: none;
            }
            QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::handle:hover:vertical {
                background: #cccccc; /* Hellgrau */
            }
            QScrollBar::handle:vertical {
                background: #ffffff; /* Weiß *
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #dddddd; /* Helleres Hellgrau */
            }
            """
        )

        main_layout = QHBoxLayout(self)

        sidebar_layout = QVBoxLayout()

        self.chat_list = QListWidget()
        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        self.chat_list.setGraphicsEffect(shadow_effect)
        self.chat_list.setFont(QFont('Arial', 12))
        self.chat_list.setStyleSheet("""
            QListWidget {
                background-color: #1c1c1c;
                padding: 20px;
                border: 2px solid #4a4a4a;
                border-radius: 5px;
                color: #ffffff;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 2px solid #4a4a4a;
                color: #ffffff;
            }
            QListWidget::item:hover {
                border-bottom: 3px solid #0078d7;
            }
            QListWidget::item:selected {
                background-color: #0078d7;
                border-bottom: 3px solid #0078d7;
            }
            QScrollBar:vertical {
                background-color: #1c1c1c; /* Farbe der Zieh-Leiste */
                width: 10px;
                border: none; /* Entfernt eventuelle Ränder */
            }

            QScrollBar::handle:vertical {
                background-color: #ffffff; /* Farbe der Zieh-Leiste */
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical {
                background: none;
            }

            QScrollBar::sub-line:vertical {
                background: none;
            }

            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        self.chat_list.setFixedWidth(250)
        self.chat_list.itemClicked.connect(self.item_clicked_handler)
        sidebar_layout.addWidget(self.chat_list)

        button_layout = QHBoxLayout()

        new_chat_button = QPushButton('+')
        new_chat_button.setFixedSize(100, 55)
        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        new_chat_button.setGraphicsEffect(shadow_effect)
        new_chat_button.setFont(QFont('Arial', 15, QFont.Bold))
        new_chat_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                padding: 5px;
                margin: 10px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #00ff00, stop: 1 #008000);
            }
            QPushButton:pressed {
                background-color: #333333;
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #00ff00, stop: 1 #008000);
            }
        """)
        new_chat_button.clicked.connect(self.create_new_chat)
        button_layout.addWidget(new_chat_button, alignment=Qt.AlignTop)

        delete_chat_button = QPushButton('-')
        delete_chat_button.setFixedSize(100, 55)
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        delete_chat_button.setGraphicsEffect(shadow_effect)
        delete_chat_button.setFont(QFont('Arial', 15, QFont.Bold))
        delete_chat_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                padding: 5px;
                margin: 10px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #ff0000, stop: 1 #008000);
            }
            QPushButton:pressed {
                background-color: #333333;
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #ff0000, stop: 1 #008000);
            }
        """)
        delete_chat_button.clicked.connect(self.delete_current_chat)
        button_layout.addWidget(delete_chat_button, alignment=Qt.AlignTop)

        sidebar_layout.addLayout(button_layout)

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)

        main_area_layout = QVBoxLayout()

        self.chat_scroll_area = QScrollArea()
        self.chat_scroll_area.setWidgetResizable(True)
        self.chat_scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
            }

            QScrollArea > QWidget > QWidget {
                background-color: #222222; /* Hintergrundfarbe der inneren Widgets */
            }

            QScrollArea > QWidget > QScrollBar:vertical {
                background-color: #222222; /* Hintergrundfarbe der inneren Widgets */
                width: 10px;
                border: none; /* Entfernt eventuelle Ränder */
            }

            QScrollBar::handle:vertical {
                background-color: #ffffff;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
            }

            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }

        """)

        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_widget.setLayout(self.chat_layout)
        self.chat_scroll_area.setWidget(self.chat_widget)

        main_area_layout.addWidget(self.chat_scroll_area)

        input_layout = QVBoxLayout()

        text_send_layout = QHBoxLayout()

        self.text_input_box = QTextEdit()
        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        self.text_input_box.setGraphicsEffect(shadow_effect)
        self.text_input_box.setPlaceholderText("Send a message to Chat++")
        self.text_input_box.setFont(QFont('Arial', 13))
        self.text_input_box.setStyleSheet("""
            QTextEdit {
                background-color: #1c1c1c;
                padding: 10px;
                border: 2px solid #4a4a4a;
                border-radius: 5px;
                color: #ffffff;
            }
            QScrollBar:vertical {
                background-color: #1c1c1c; /* Farbe der Zieh-Leiste */
                width: 10px;
                border: none; /* Entfernt eventuelle Ränder */
            }

            QScrollBar::handle:vertical {
                background-color: #ffffff; /* Farbe der Zieh-Leiste */
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical {
                background: none;
            }

            QScrollBar::sub-line:vertical {
                background: none;
            }

            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        text_send_layout.addWidget(self.text_input_box)

        self.send_button = QPushButton()
        self.send_button.setFixedSize(80, 80)
        self.send_button.setFont(QFont('Arial', 35, QFont.Bold))
        self.send_button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)
        self.send_button.clicked.connect(self.process_input)
        text_send_layout.addWidget(self.send_button)
        # Icon-Größe auf die gewünschte Größe setzen
        self.send_button.setIconSize(QtCore.QSize(50, 50))  # Hier Größe der SVG-Datei angeben
        self.send_button.setIconSize(QSize(50, 50))  # Hier Größe der SVG-Datei angeben
        self.send_button.setIcon(QIcon('send-nor.svg'))

        self.setLayout(layout)

        # Event-Filter hinzufügen
        self.send_button.installEventFilter(self)

        input_layout.addLayout(text_send_layout)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)  # Setze den Abstand zwischen den Buttons auf 15px


        def move_send_button_up():
            self.send_button.move(self.send_button.x(), self.send_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_send_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        self.send_button.pressed.connect(move_send_button_up)
        self.send_button.released.connect(lambda: move_send_button_down(self.send_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        self.send_button.enterEvent = lambda event: move_send_button_up()
        self.send_button.leaveEvent = lambda event: move_send_button_down(self.send_button)

        self.setLayout(button_layout)

        self.setting_button3 = QPushButton()

        self.setting_button3.setFixedSize(200, 35)
        self.setting_button3.setFont(QFont('Arial', 12))
        self.setting_button3.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(self.setting_button3)
        # Icon-Größe auf die gewünschte Größe setzen
        self.setting_button3.setIconSize(QtCore.QSize(30, 30))  # Hier Größe der SVG-Datei angeben
        self.setting_button3.setIconSize(QSize(30, 30))  # Hier Größe der SVG-Datei angeben
        self.setting_button3.setIcon(QIcon(''))

        renderer = QSvgRenderer('C:\\Users\\julia\\PycharmProjects\\test23\\peharge-logo3.4.svg')

        pixmap = QPixmap(50, 50)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        icon = QIcon(pixmap)
        peharge_button = QPushButton()
        peharge_button.setIcon(icon)

        # Erstelle den special_char_button.
        peharge_button.setFixedSize(75, 35)
        peharge_button.setFont(QFont('Arial', 20, QFont.Bold))
        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        peharge_button.setGraphicsEffect(shadow_effect)
        peharge_button.setIconSize(QtCore.QSize(20, 22))  # Hier Größe der SVG-Datei angeben
        peharge_button.setIconSize(QSize(20, 22))  # Hier Größe der SsVG-Datei angeben
        peharge_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(peharge_button, alignment=Qt.AlignRight)
        peharge_button.clicked.connect(self.peharge)
        button_layout.setContentsMargins(0, 20, 0, 0)  # Setze den oberen Abstand auf 20px.

        # Definiere eine Funktion, um den Button um 10px nach oben zu verschieben.
        def move_peharge_button_up():
            peharge_button.move(peharge_button.x(), peharge_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_peharge_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        peharge_button.pressed.connect(move_peharge_button_up)
        peharge_button.released.connect(lambda: move_peharge_button_down(peharge_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        peharge_button.enterEvent = lambda event: move_peharge_button_up()
        peharge_button.leaveEvent = lambda event: move_peharge_button_down(peharge_button)

        self.setLayout(button_layout)

        # Erstelle den special_char_button.
        special_char_button = QPushButton()
        special_char_button.setIcon(QIcon('C:\\Users\\julia\\PycharmProjects\\test23\\smily.svg'))
        special_char_button.setFixedSize(75, 35)
        special_char_button.setFont(QFont('Arial', 20, QFont.Bold))
        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        special_char_button.setGraphicsEffect(shadow_effect)

        special_char_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(special_char_button)
        special_char_button.clicked.connect(self.show_special_characters)
        button_layout.setContentsMargins(0, 20, 0, 0)  # Setze den oberen Abstand auf 20px.

        # Definiere eine Funktion, um den Button um 10px nach oben zu verschieben.
        def move_button_up():
            special_char_button.move(special_char_button.x(), special_char_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        special_char_button.pressed.connect(move_button_up)
        special_char_button.released.connect(lambda: move_button_down(special_char_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        special_char_button.enterEvent = lambda event: move_button_up()
        special_char_button.leaveEvent = lambda event: move_button_down(special_char_button)

        self.setLayout(button_layout)

        icon_pathso = 'C:\\Users\\julia\\PycharmProjects\\test23\\chart-simple-solid.svg'

        special_char_button2 = QPushButton()
        special_char_button2.setIcon(QIcon(icon_pathso))

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        special_char_button2.setGraphicsEffect(shadow_effect)
        special_char_button2.setFixedSize(75, 35)
        special_char_button2.setFont(QFont('Arial', 12, QFont.Bold))
        special_char_button2.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(special_char_button2)
        special_char_button2.clicked.connect(self.show_special_characters2)

        def move_special_char_button2_up():
            special_char_button2.move(special_char_button2.x(), special_char_button2.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_special_char_button2_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.


        special_char_button2.pressed.connect(move_special_char_button2_up)
        special_char_button2.released.connect(lambda: move_special_char_button2_down(special_char_button2))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        special_char_button2.enterEvent = lambda event: move_special_char_button2_up()
        special_char_button2.leaveEvent = lambda event: move_special_char_button2_down(special_char_button2)

        self.setLayout(button_layout)

        icon_pathi = 'C:\\Users\\julia\\PycharmProjects\\test23\\camera-solid.svg'

        image_char_button = QPushButton()
        image_char_button.setIcon(QIcon(icon_pathi))

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        image_char_button.setGraphicsEffect(shadow_effect)
        image_char_button.setFixedSize(75, 35)
        image_char_button.setFont(QFont('Arial', 12, QFont.Bold))
        image_char_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(image_char_button)
        image_char_button.clicked.connect(self.img_re)

        def move_image_char_button_up():
            image_char_button.move( image_char_button.x(),  image_char_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_image_char_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        image_char_button.pressed.connect(move_image_char_button_up)
        image_char_button.released.connect(lambda: move_image_char_button_down(image_char_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        image_char_button.enterEvent = lambda event: move_image_char_button_up()
        image_char_button.leaveEvent = lambda event: move_image_char_button_down(image_char_button)

        self.setLayout(button_layout)


        icon_pathd = 'C:\\Users\\julia\\PycharmProjects\\test23\\folder-solid.svg'

        text_pdf = QPushButton()
        text_pdf.setIcon(QIcon(icon_pathd))

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        text_pdf.setGraphicsEffect(shadow_effect)
        text_pdf.setFixedSize(75, 35)
        text_pdf.setFont(QFont('Arial', 12, QFont.Bold))
        text_pdf.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(text_pdf)
        text_pdf.clicked.connect(self.load_document)

        def move_text_pdf_up():
            text_pdf.move( text_pdf.x(),  text_pdf.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_text_pdf_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        text_pdf.pressed.connect(move_text_pdf_up)
        text_pdf.released.connect(lambda: move_text_pdf_down(text_pdf))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        text_pdf.enterEvent = lambda event: move_text_pdf_up()
        text_pdf.leaveEvent = lambda event: move_text_pdf_down(text_pdf)

        self.setLayout(button_layout)

        # Pfad zur SVG-Datei
        icon_pathco = 'C:\\Users\\julia\\PycharmProjects\\test23\\code-imp-img.svg'

        code_button = QPushButton()

        # Icon laden und auf die gewünschte Größe skalieren
        icon_pixmap = QPixmap(icon_pathco).scaled(70, 70)
        icon = QIcon(icon_pixmap)
        code_button.setIcon(icon)

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(code_button)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        code_button.setGraphicsEffect(shadow_effect)
        code_button.setFixedSize(75, 35)
        code_button.setIconSize(QtCore.QSize(20, 20))  # Hier Größe der SVG-Datei angeben
        code_button.setIconSize(QSize(20, 20))  # Hier Größe der SsVG-Datei angeben
        code_button.setFont(QFont('Arial', 12, QFont.Bold))
        code_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(code_button)
        code_button.clicked.connect(self.load_code)

        def move_code_button_up():
            code_button.move(code_button.x(), code_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_code_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        code_button.pressed.connect(move_code_button_up)
        code_button.released.connect(lambda: move_code_button_down(code_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        code_button.enterEvent = lambda event: move_code_button_up()
        code_button.leaveEvent = lambda event: move_code_button_down(code_button)

        self.setLayout(button_layout)

        renderer = QSvgRenderer('C:\\Users\\julia\\PycharmProjects\\test23\\microphone-solid.svg')

        pixmap = QPixmap(34, 41)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        icon = QIcon(pixmap)
        vtv_char_button2 = QPushButton()
        vtv_char_button2.setIcon(icon)

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        vtv_char_button2.setGraphicsEffect(shadow_effect)
        vtv_char_button2.setFixedSize(75, 35)
        vtv_char_button2.setFont(QFont('Arial', 12, QFont.Bold))
        vtv_char_button2.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(vtv_char_button2)
        vtv_char_button2.clicked.connect(self.vtv)

        def move_vtv_char_button2_up():
            vtv_char_button2.move(vtv_char_button2.x(), vtv_char_button2.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_vtv_char_button2_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.


        vtv_char_button2.pressed.connect(move_vtv_char_button2_up)
        vtv_char_button2.released.connect(lambda: move_vtv_char_button2_down(vtv_char_button2))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        vtv_char_button2.enterEvent = lambda event: move_vtv_char_button2_up()
        vtv_char_button2.leaveEvent = lambda event: move_vtv_char_button2_down(vtv_char_button2)

        self.setLayout(button_layout)

        # Pfad zur SVG-Datei
        icon_pathsh = 'C:\\Users\\julia\\PycharmProjects\\test23\\video-chat.svg'

        vc_button = QPushButton()

        # Icon laden und auf die gewünschte Größe skalieren
        icon_pixmap = QPixmap(icon_pathsh).scaled(70, 70)
        icon = QIcon(icon_pixmap)
        vc_button.setIcon(icon)

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(vc_button)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        vc_button.setGraphicsEffect(shadow_effect)
        vc_button.setFixedSize(75, 35)
        vc_button.setIconSize(QtCore.QSize(16, 16))  # Hier Größe der SVG-Datei angeben
        vc_button.setIconSize(QSize(16, 16))  # Hier Größe der SsVG-Datei angeben
        vc_button.setFont(QFont('Arial', 12, QFont.Bold))
        vc_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(vc_button)
        vc_button.clicked.connect(self.ob_rec)

        def move_vc_button_up():
            vc_button.move(vc_button.x(), vc_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_vc_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        vc_button.pressed.connect(move_vc_button_up)
        vc_button.released.connect(lambda: move_vc_button_down(vc_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        vc_button.enterEvent = lambda event: move_vc_button_up()
        vc_button.leaveEvent = lambda event: move_vc_button_down(vc_button)

        self.setLayout(button_layout)

        # Pfad zur SVG-Datei
        icon_pathig = 'C:\\Users\\julia\\PycharmProjects\\test23\\img_gen_img.svg'

        img_gen_button = QPushButton()

        # Icon laden und auf die gewünschte Größe skalieren
        icon_pixmap = QPixmap(icon_pathig).scaled(70, 70)
        icon = QIcon(icon_pixmap)
        img_gen_button.setIcon(icon)

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(img_gen_button)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        img_gen_button.setGraphicsEffect(shadow_effect)
        img_gen_button.setFixedSize(75, 35)
        img_gen_button.setIconSize(QtCore.QSize(19, 19))  # Hier Größe der SVG-Datei angeben
        img_gen_button.setIconSize(QSize(19, 19))  # Hier Größe der SsVG-Datei angeben
        img_gen_button.setFont(QFont('Arial', 12, QFont.Bold))
        img_gen_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(img_gen_button)
        img_gen_button.clicked.connect(self.img_gen)

        def move_img_gen_button_up():
            img_gen_button.move(img_gen_button.x(), img_gen_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_img_gen_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        img_gen_button.pressed.connect(move_img_gen_button_up)
        img_gen_button.released.connect(lambda: move_img_gen_button_down(img_gen_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        img_gen_button.enterEvent = lambda event: move_img_gen_button_up()
        img_gen_button.leaveEvent = lambda event: move_img_gen_button_down(img_gen_button)

        self.setLayout(button_layout)

        # Pfad zur SVG-Datei
        icon_pathvg = 'C:\\Users\\julia\\PycharmProjects\\test23\\video-gen-img.svg'

        video_gen_button = QPushButton()

        # Icon laden und auf die gewünschte Größe skalieren
        icon_pixmap = QPixmap(icon_pathvg).scaled(70, 70)
        icon = QIcon(icon_pixmap)
        video_gen_button.setIcon(icon)

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(video_gen_button)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        video_gen_button.setGraphicsEffect(shadow_effect)
        video_gen_button.setFixedSize(75, 35)
        video_gen_button.setIconSize(QtCore.QSize(21, 21))  # Hier Größe der SVG-Datei angeben
        video_gen_button.setIconSize(QSize(21, 21))  # Hier Größe der SsVG-Datei angeben
        video_gen_button.setFont(QFont('Arial', 12, QFont.Bold))
        video_gen_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(video_gen_button)
        video_gen_button.clicked.connect(self.img_gen)

        def move_video_gen_button_up():
            video_gen_button.move(video_gen_button.x(), video_gen_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_video_gen_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        video_gen_button.pressed.connect(move_video_gen_button_up)
        video_gen_button.released.connect(lambda: move_video_gen_button_down(video_gen_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        video_gen_button.enterEvent = lambda event: move_video_gen_button_up()
        video_gen_button.leaveEvent = lambda event: move_video_gen_button_down(video_gen_button)

        self.setLayout(button_layout)

        # Pfad zur SVG-Datei
        icon_pathvg = 'C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\xcpp-img.svg'

        xcpp_button = QPushButton()

        # Icon laden und auf die gewünschte Größe skalieren
        icon_pixmap = QPixmap(icon_pathvg).scaled(70, 70)
        icon = QIcon(icon_pixmap)
        xcpp_button.setIcon(icon)

        # Hinzufügen eines Schatteneffekts zum Button
        shadow_effect = QGraphicsDropShadowEffect(xcpp_button)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(Qt.black)  # Schwarze Farbe für den Schatten
        shadow_effect.setOffset(5, 5)
        xcpp_button.setGraphicsEffect(shadow_effect)
        xcpp_button.setFixedSize(75, 35)
        xcpp_button.setIconSize(QtCore.QSize(19, 19))  # Hier Größe der SVG-Datei angeben
        xcpp_button.setIconSize(QSize(19, 19))  # Hier Größe der SsVG-Datei angeben
        xcpp_button.setFont(QFont('Arial', 12, QFont.Bold))
        xcpp_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(xcpp_button, alignment=Qt.AlignLeft)
        xcpp_button.clicked.connect(self.xcpp)

        def move_xcpp_up():
            xcpp_button.move(xcpp_button.x(), xcpp_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_xcpp_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        xcpp_button.pressed.connect(move_xcpp_up)
        xcpp_button.released.connect(lambda: move_xcpp_down(xcpp_button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        xcpp_button.enterEvent = lambda event: move_xcpp_up()
        xcpp_button.leaveEvent = lambda event: move_xcpp_down(xcpp_button)

        self.setLayout(button_layout)

        self.web_button = QPushButton()

        self.web_button.setFixedSize(30, 25)
        self.web_button.setFont(QFont('Arial', 12, QFont.Bold))
        self.web_button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(self.web_button, alignment=Qt.AlignRight)
        self.web_button.clicked.connect(self.vc)
        # Icon-Größe auf die gewünschte Größe setzen
        self.web_button.setIconSize(QtCore.QSize(25, 25))  # Hier Größe der SVG-Datei angeben
        self.web_button.setIconSize(QSize(25, 25))  # Hier Größe der SVG-Datei angeben
        self.web_button.setIcon(QIcon('web-img.svg'))

        self.setLayout(layout)

        # Event-Filter hinzufügen
        self.web_button.installEventFilter(self)

        input_layout.addLayout(text_send_layout)

        def move_web_button_up():
            self.web_button.move(self.web_button.x(), self.web_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_web_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        self.web_button.pressed.connect(move_web_button_up)
        self.web_button.released.connect(lambda: move_web_button_down(self.web_button))

        self.setLayout(button_layout)

        self.web_sec_button = QPushButton()

        self.web_sec_button.setFixedSize(30, 25)
        self.web_sec_button.setFont(QFont('Arial', 12, QFont.Bold))
        self.web_sec_button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)

        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(self.web_sec_button)
        self.web_sec_button.clicked.connect(self.seccheck)
        # Icon-Größe auf die gewünschte Größe setzen
        self.web_sec_button.setIconSize(QtCore.QSize(25, 25))  # Hier Größe der SVG-Datei angeben
        self.web_sec_button.setIconSize(QSize(25, 25))  # Hier Größe der SVG-Datei angeben
        self.web_sec_button.setIcon(QIcon('web-sec-img.svg'))

        self.setLayout(layout)

        # Event-Filter hinzufügen
        self.web_sec_button.installEventFilter(self)

        input_layout.addLayout(text_send_layout)

        def move_web_sec_button_up():
            self.web_sec_button.move(self.web_sec_button.x(), self.web_sec_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_web_sec_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        self.web_sec_button.pressed.connect(move_web_sec_button_up)
        self.web_sec_button.released.connect(lambda: move_web_sec_button_down(self.web_sec_button))

        self.setLayout(button_layout)

        self.mute_button = QPushButton()

        self.mute_button.setFixedSize(30, 25)
        self.mute_button.setFont(QFont('Arial', 12))
        self.mute_button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(self.mute_button)
        self.mute_button.clicked.connect(self.toggle_mute)
        # Icon-Größe auf die gewünschte Größe setzen
        self.mute_button.setIconSize(QtCore.QSize(27, 27))  # Hier Größe der SVG-Datei angeben
        self.mute_button.setIconSize(QSize(27, 27))  # Hier Größe der SVG-Datei angeben
        self.mute_button.setIcon(QIcon('volume-high-solid.svg'))

        self.setLayout(layout)

        # Event-Filter hinzufügen
        self.mute_button.installEventFilter(self)

        def move_mute_button_up():
            self.mute_button.move(self.mute_button.x(), self.mute_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_mute_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.

        self.mute_button.pressed.connect(move_mute_button_up)
        self.mute_button.released.connect(lambda: move_mute_button_down(self.mute_button))

        self.setLayout(button_layout)

        self.plus_button = QPushButton()

        self.plus_button.setFixedSize(30, 25)
        self.plus_button.setFont(QFont('Arial', 12))
        self.plus_button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(self.plus_button)
        self.plus_button.clicked.connect(self.plus_update)
        # Icon-Größe auf die gewünschte Größe setzen
        self.plus_button.setIconSize(QtCore.QSize(27, 27))  # Hier Größe der SVG-Datei angeben
        self.plus_button.setIconSize(QSize(27, 27))  # Hier Größe der SVG-Datei angeben
        self.plus_button.setIcon(QIcon('plus.svg'))

        self.setLayout(layout)

        # Event-Filter hinzufügen
        self.plus_button.installEventFilter(self)

        input_layout.addLayout(text_send_layout)

        def move_plus_button_up():
            self.plus_button.move(self.plus_button.x(), self.plus_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_plus_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.

        self.plus_button.pressed.connect(move_plus_button_up)
        self.plus_button.released.connect(lambda: move_plus_button_down(self.plus_button))

        self.setLayout(button_layout)

        self.setting_button = QPushButton()

        self.setting_button.setFixedSize(30, 25)
        self.setting_button.setFont(QFont('Arial', 12))
        self.setting_button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(self.setting_button)
        self.setting_button.clicked.connect(self.open_settings_window)
        # Icon-Größe auf die gewünschte Größe setzen
        self.setting_button.setIconSize(QtCore.QSize(23, 23))  # Hier Größe der SVG-Datei angeben
        self.setting_button.setIconSize(QSize(23, 23))  # Hier Größe der SVG-Datei angeben
        self.setting_button.setIcon(QIcon('settings.svg'))

        self.setLayout(layout)

        # Event-Filter hinzufügen
        self.setting_button.installEventFilter(self)

        def move_setting_button_up():
            self.setting_button.move(self.setting_button.x(), self.setting_button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_setting_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.

        self.setting_button.pressed.connect(move_setting_button_up)
        self.setting_button.released.connect(lambda: move_setting_button_down(self.setting_button))

        self.setLayout(button_layout)

        self.setting_button2 = QPushButton()

        self.setting_button2.setFixedSize(35, 35)
        self.setting_button2.setFont(QFont('Arial', 12))
        self.setting_button2.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
            QPushButton:pressed {
                color: #ffffff;
            }
        """)
        # Füge den special_char_button zum Layout hinzu mit einem Abstand von 20px oben.
        button_layout.addWidget(self.setting_button2)
        # Icon-Größe auf die gewünschte Größe setzen
        self.setting_button2.setIconSize(QtCore.QSize(30, 30))  # Hier Größe der SVG-Datei angeben
        self.setting_button2.setIconSize(QSize(30, 30))  # Hier Größe der SVG-Datei angeben
        self.setting_button2.setIcon(QIcon(''))

        input_layout.addLayout(button_layout)

        main_area_layout.addLayout(input_layout)

        main_layout.addWidget(sidebar_widget, alignment=Qt.AlignTop)
        main_layout.addLayout(main_area_layout, 1)

        self.setLayout(main_layout)

        self.chats = {}
        self.current_chat_index = 0

        self.create_new_chat()

        self.resizeEvent = self.on_resize

    def eventFilter(self, obj, event):
        buttons = {
            self.send_button: {
                QEvent.Enter: ('send-hover.svg', QSize(50, 50)),
                QEvent.Leave: ('send-nor.svg', QSize(50, 50)),
                QEvent.MouseButtonPress: ('send-pressed.svg', QSize(55, 55)),
                QEvent.MouseButtonRelease: ('send-hover.svg', QSize(50, 50))
            },
            self.web_button: {
                QEvent.Enter: ('web-img-hover.svg', QSize(25, 25)),
                QEvent.Leave: ('web-img.svg', QSize(25, 25)),
                QEvent.MouseButtonPress: ('web-img-pressed.svg', QSize(30, 30)),
                QEvent.MouseButtonRelease: ('web-img-hover.svg', QSize(25, 25))
            },
            self.web_sec_button: {
                QEvent.Enter: ('web-sec-img-hover.svg', QSize(25, 25)),
                QEvent.Leave: ('web-sec-img.svg', QSize(25, 25)),
                QEvent.MouseButtonPress: ('web-sec-img.svg', QSize(30, 30)),
                QEvent.MouseButtonRelease: ('web-sec-img.svg-hover', QSize(25, 25))
            },
            self.plus_button: {
                QEvent.Enter: ('plus-hover.svg', QSize(27, 27)),
                QEvent.Leave: ('plus.svg', QSize(27, 27)),
                QEvent.MouseButtonPress: ('plus-pressed.svg', QSize(32, 32)),
                QEvent.MouseButtonRelease: ('plus-hover.svg', QSize(27, 27))
            },
            self.setting_button: {
                QEvent.Enter: ('settings-hover.svg', QSize(23, 23)),
                QEvent.Leave: ('settings.svg', QSize(23, 23)),
                QEvent.MouseButtonPress: ('settings-pressed.svg', QSize(25, 25)),
                QEvent.MouseButtonRelease: ('settings-hover.svg', QSize(23, 23))
            }
        }

        if obj in buttons:
            if event.type() in buttons[obj]:
                icon_file, icon_size = buttons[obj][event.type()]
                obj.setIcon(QIcon(icon_file))
                obj.setIconSize(icon_size)

        if obj == self.mute_button:
            if event.type() == QEvent.Enter:
                if self.is_muted:
                    obj.setIcon(QIcon(QPixmap('volume-high-solid-muted-hover.svg')))
                else:
                    obj.setIcon(QIcon(QPixmap('volume-high-solid-hover.svg')))
                return True
            elif event.type() == QEvent.Leave:
                if self.is_muted:
                    obj.setIcon(QIcon(QPixmap('volume-high-solid-muted.svg')))
                else:
                    obj.setIcon(QIcon(QPixmap('volume-high-solid.svg')))
                return True

            if obj == self.mute_button:
                if event.type() == QEvent.MouseButtonPress:
                    self.mute_button.setIconSize(QSize(30, 30))
                elif event.type() == QEvent.MouseButtonRelease:
                    self.mute_button.setIconSize(QSize(27, 27))
            return super().eventFilter(obj, event)

        return super().eventFilter(obj, event)

    def on_resize(self, event):
        self.resize_widgets()

    def resize_widgets(self):
        height = self.height()
        width = self.width()

        sidebar_height = int(0.6 * height)
        self.chat_list.setFixedHeight(sidebar_height)
        self.text_input_box.setFixedHeight(int(0.2 * height))
        self.text_input_box.setFixedWidth(int(0.79 * width))  # Korrigiert zu setFixedWidth

        chat_area_height = int(0.7 * height)
        self.chat_scroll_area.setFixedHeight(chat_area_height)

    def load_document(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            None,
            "Open Document File",
            "",
            "All Supported Files (*.pdf *.docx *.txt *.rtf *.odt);;PDF Files (*.pdf);;Word Files (*.docx);;Text Files (*.txt);;RTF Files (*.rtf);;ODT Files (*.odt);;All Files (*)",
            options=options
        )
        if file_name:
            file_extension = os.path.splitext(file_name)[1].lower()
            if file_extension == '.pdf':
                document_text = self.extract_text_from_pdf(file_name)
            elif file_extension == '.docx':
                document_text = self.extract_text_from_docx(file_name)
            elif file_extension == '.txt':
                document_text = self.extract_text_from_txt(file_name)
            elif file_extension == '.rtf':
                document_text = self.extract_text_from_rtf(file_name)
            elif file_extension == '.odt':
                document_text = self.extract_text_from_odt(file_name)
            else:
                document_text = "Unsupported file format."
            self.text_input_box.setText(document_text)

    def extract_text_from_pdf(self, file_name):
        try:
            with open(file_name, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                pdf_text = ""
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    pdf_text += page.extract_text()
            return pdf_text
        except Exception as e:
            print(f"Error extracting text from PDF '{file_name}': {str(e)}")
    def extract_text_from_docx(self, file_path):
        doc = docx.Document(file_path)
        docx_text = ""
        for para in doc.paragraphs:
            docx_text += para.text + '\n'
        return docx_text

    def extract_text_from_txt(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            txt_text = file.read()
        return txt_text

    def extract_text_from_rtf(self, file_path):
        with open(file_path, 'r') as file:
            rtf_text = file.read()
        return rtf_to_text(rtf_text)

    def extract_text_from_odt(self, file_path):
        textdoc = load(file_path)
        paragraphs = textdoc.getElementsByType(P)
        odt_text = ""
        for paragraph in paragraphs:
            odt_text += ''.join([node.data for node in paragraph.childNodes if node.nodeType == node.TEXT_NODE]) + '\n'
        return odt_text

    def load_code(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            None,
            "Open Document File",
            "",
            "Python Files (*.py);;HTML Files (*.html *.htm);;CSS Files (*.css);;Java Files (*.java);;JavaScript Files (*.js);;All Files (*)",
            options=options
        )
        if file_name:
            file_extension = os.path.splitext(file_name)[1].lower()
            if file_extension in ['.py', '.html', '.htm', '.css', '.java', '.js']:
                document_text = self.extract_text_from_file(file_name)
            else:
                document_text = "Unsupported file format."
            self.text_input_box.setText(document_text)

    def extract_text_from_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                if file_path.endswith('.py'):
                    # Extract text for Python files
                    document_text = self.extract_text_from_python_file(f)
                elif file_path.endswith(('.html', '.htm')):
                    # Extract text for HTML files
                    document_text = self.extract_text_from_html_file(f)
                elif file_path.endswith('.css'):
                    # Extract text for CSS files
                    document_text = self.extract_text_from_css_file(f)
                elif file_path.endswith('.java'):
                    # Extract text for Java files
                    document_text = self.extract_text_from_java_file(f)
                elif file_path.endswith('.js'):
                    # Extract text for JavaScript files
                    document_text = self.extract_text_from_javascript_file(f)
                else:
                    document_text = "Unsupported file format."
            return document_text
        except Exception as e:
            print(f"Error extracting text from file '{file_path}': {str(e)}")

    def extract_text_from_python_file(self, file_obj):
        # Implement text extraction from Python file using PyPDF2 or any other method you prefer
        # Example implementation with PyPDF2:
        reader = PyPDF2.PdfFileReader(file_obj)
        pdf_text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            pdf_text += page.extractText()
        return pdf_text

    def extract_text_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            file_text = file.read()
        return file_text

    def process_input(self):
        text_input = self.text_input_box.toPlainText().strip()

        if text_input:
            text_input = self.replace_smileys_and_formulas(text_input)

            command = "ollama run llama3"
            output = self.run_command_and_get_output(command, text_input).strip()

            paragraphs = re.split(r'(\n\s*\n)', output)

            formatted_output = ""
            for para in paragraphs:
                if para.strip() == '\n':
                    formatted_output += "<br>"
                else:
                    formatted_output += html.escape(para).replace('\n', '<br>')

            print(formatted_output)
            current_time = QDateTime.currentDateTime().toString("hh:mm:ss")

            image_two = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\peharge-logo3.4.png"
            image_chatbot = f'<img src="{image_two}" width="30" height="30">'

            # HTML für Benutzer-Nachricht
            user_message = (
                f"<html><div style='text-align: right; border: 2px solid; "
                f"border-image: linear-gradient(to bottom, #ff00ff, #800080) 1; "
                f"border-radius: 10px; padding: 10px; margin: 5px; "
                f"background-color: rgb(34, 34, 34); color: #ffffff; width: max-content;'>"
                f"<font color='white' size='3'>{text_input}</font><br>"
                f"<font size='2' color='red'>{current_time}</font></div></html>"
            )
            self.append_chat_u(user_message, Qt.AlignRight)

            # HTML für Chatbot-Nachricht
            chatbot_message = (
                f'<html><body><table><tr><td>{image_chatbot}</td><td>'
                f'<font color="white" size="3">{formatted_output}</font><br>'
                f'<font size="2" color="red">{current_time}</font></td></tr></table>'
                f'<style>body {{ line-height: 1.5; }}</style></body></html>'
            )
            self.append_chat_c(chatbot_message, Qt.AlignLeft)

            current_chat_name = f"Chat {self.current_chat_index}"

            # HTML für JSON-Datei (Benutzer-Nachricht)
            html_input = (
                f"<html><div style='text-align: right; border: 2px solid; "
                f"border-image: linear-gradient(to bottom, #ff00ff, #800080) 1; "
                f"border-radius: 10px; padding: 10px; margin: 5px; "
                f"background-color: rgb(34, 34, 34); color: #ffffff; width: max-content;'>"
                f"<font color='white' size='3'>{text_input}</font><br>"
                f"<font size='2' color='red'>{current_time}</font></div></html>"
            )

            # HTML für JSON-Datei (Chatbot-Nachricht)
            html_output = (
                f'<html><body><table><tr><td>{image_chatbot}</td><td>'
                f'<font color="white" size="3">{formatted_output}</font><br>'
                f'<font size="2" color="red">{current_time}</font></td></tr></table>'
                f'<style>body {{ line-height: 1.5; }}</style></body></html>'
            )

            # Sicherstellen, dass der aktuelle Chat in der Liste ist
            if current_chat_name not in self.chats:
                self.chats[current_chat_name] = []

            # HTML-Nachrichten zur JSON-Liste hinzufügen
            self.chats[current_chat_name].append(html_input)
            self.chats[current_chat_name].append(html_output)

            # JSON-Datei speichern
            with open('chats.json', 'w') as json_file:
                json.dump(self.chats, json_file)

            self.speak_text(output)
            self.text_input_box.clear()

    def append_chat_u(self, message, alignment):
        chat_item = QListWidgetItem()
        chat_item.setTextAlignment(alignment)
        chat_item.setData(Qt.UserRole, message)
        self.chat_list_widget.addItem(chat_item)
        self.chat_list_widget.scrollToBottom()

    def replace_smileys_and_formulas(self, text):
        return text

    def run_command_and_get_output(self, command, text_input):
        return "output of command"


    def speak_text(self, text):
        if not self.is_muted:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

    def get_current_chat_messages(self):
        if self.current_chat_index in self.chats:
            return self.chats[self.current_chat_index]
        else:
            return []

    def run_command_and_get_output(self, command, text_input):
        try:
            result = subprocess.run(command, input=text_input.encode(),
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output = result.stdout.decode('utf-8')
            return output
        except Exception as e:
            return str(e)

    def speak_button_clicked(self):
        current_chat_messages = self.get_current_chat_messages()
        text_to_speak = '\n'.join(current_chat_messages)
        self.speak_text(text_to_speak)

    def toggle_mute(self):
        self.is_muted = not self.is_muted
        self.update_icon()
        if self.is_muted:
            print("Text-to-speech is muted.")
        else:
            print("Text-to-speech is no longer muted.")

    def update_icon(self):
        if self.is_muted:
            self.mute_button.setIcon(QIcon(QPixmap('volume-high-solid-muted.svg')))
        else:
            self.mute_button.setIcon(QIcon(QPixmap('volume-high-solid.svg')))
        self.mute_button.setIconSize(QSize(27, 27))

    def replace_smileys_and_formulas(self, text_input):
        smileys = {
            ':)': '😊', ':(': '☹️', ';)': '😉', ':D': '😃', 'XD': '😆'
        }
        for smiley, symbol in smileys.items():
            text_input = text_input.replace(smiley, symbol)

        math_formulas = re.findall(r'\$(.*?)\$', text_input)
        for formula in math_formulas:
            formula_result = self.evaluate_math_formula(formula)
            text_input = text_input.replace(f'${formula}$', str(formula_result))

        return text_input

    def evaluate_math_formula(self, formula):
        try:
            result = eval(formula)
            return result
        except:
            return "Error"

    def append_chat(self, message, alignment):
        label = QLabel(message)
        label.setFont(QFont('Arial', 12))
        label.setStyleSheet("background-color: rgb(34, 34, 34); color: #ffffff; padding: 10px;")
        label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        label.setWordWrap(True)

        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(alignment)
        widget.setLayout(layout)

        self.chat_layout.addWidget(widget)
        self.chat_scroll_area.verticalScrollBar().setValue(self.chat_scroll_area.verticalScrollBar().maximum())

    def append_chat_u(self, message, alignment):
        label = QLabel(message)
        label.setFont(QFont('Arial', 12))
        label.setStyleSheet("background-color: rgb(34, 34, 34); color: #ffffff; padding: 10px; border-radius: 5px;")
        label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        label.setWordWrap(True)

        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(alignment)
        widget.setLayout(layout)

        self.chat_layout.addWidget(widget)
        self.chat_scroll_area.verticalScrollBar().setValue(self.chat_scroll_area.verticalScrollBar().maximum())

    def create_new_chat(self):
        self.current_chat_index += 1
        chat_name = f"Chat {self.current_chat_index}"
        self.chats[chat_name] = []
        item = QListWidgetItem(chat_name)
        self.chat_list.addItem(item)
        self.chat_list.setCurrentItem(item)

    def delete_current_chat(self):
        current_item = self.chat_list.currentItem()
        if current_item:
            chat_name = current_item.text()
            del self.chats[chat_name]
            self.chat_list.takeItem(self.chat_list.row(current_item))
            if self.chat_list.count() == 0:
                self.create_new_chat()
            else:
                self.chat_list.setCurrentRow(0)

    def item_clicked_handler(self, item):
        chat_name = item.text()
        self.display_chat(chat_name)

    def display_chat(self, chat_name):
        for i in reversed(range(self.chat_layout.count())):
            widget = self.chat_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        if chat_name in self.chats:
            for message in self.chats[chat_name]:
                self.append_chat(message, Qt.AlignLeft)

    def append_chat_u(self, text, alignment=None):
        label = QLabel(text)
        label.setFont(QFont('Arial', 12))
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignRight | Qt.AlignTop)

        label.setStyleSheet("""
               QLabel {
                    border: 2px solid #4a4a4a;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 5px;
                    background-color: rgb(34, 34, 34);
                    color: #ffffff;
               }
           """)

        default_height = int(0.1 * self.height())
        label.setFixedHeight(default_height)

        max_width = int(0.8 * self.width())
        label.setMaximumWidth(max_width)

        label_height = label.sizeHint().height()

        if label_height > default_height:
            label.setFixedHeight(label_height)

        self.chat_layout.addWidget(label, alignment=Qt.AlignRight)

    def append_chat_c(self, text, alignment=None):
        label = QLabel(text)
        label.setFont(QFont('Arial', 12))
        label.setWordWrap(True)
        if alignment:
            label.setAlignment(alignment)
        label.setStyleSheet("""
            QLabel {
                border-radius: 0px;
                padding: 0px;
                margin: 0px;
                background-color: rgb(34, 34, 34);
                color: #ffffff;
            }
        """)

        default_height = int(0.1 * self.height())
        label.setFixedHeight(default_height)

        max_width = int(0.9 * self.width())
        label.setMaximumWidth(max_width)

        label_height = label.sizeHint().height()

        if label_height > default_height:
            label.setFixedHeight(label_height)

        self.chat_layout.addWidget(label)

    def peharge(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\start_test7-home1.bat')

    def show_special_characters(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Smilys")
        layout = QGridLayout(dialog)
        smileys = [("😊", "😊"), ("☹️", "☹️"), ("😉", "😉"), ("😃", "😃"), ("😆", "😆"), ("😄", "😄"), ("😁", "😁"), ("😅", "😅"),
                   ("😂", "😂"), ("🤣", "🤣"), ("😇", "😇"), ("😍", "😍"), ("😘", "😘"), ("😚", "😚"), ("😋", "😋"), ("😜", "😜"),
                   ("😝", "😝"), ("😌", "😌"), ("😏", "😏"), ("😒", "😒"), ("😞", "😞"), ("😔", "😔"), ("😕", "😕"), ("🙃", "🙃"),
                   ("😣", "😣"), ("😖", "😖"), ("😫", "😫"), ("😩", "😩"), ("😢", "😢"), ("😭", "😭"), ("😤", "😤"), ("😠", "😠"),
                   ("😡", "😡"), ("🤬", "🤬"), ("🤯", "🤯"), ("😳", "😳"), ("😱", "😱"), ("😨", "😨"), ("😰", "😰"), ("😥", "😥"),
                   ("😓", "😓"), ("🤗", "🤗"), ("🤔", "🤔"), ("🤭", "🤭"), ("🤫", "🤫"), ("🤥", "🤥"), ("😶", "😶"), ("😐", "😐"),
                   ("😑", "😑"), ("😬", "😬"), ("🙄", "🙄"), ("😯", "😯"), ("😦", "😦"), ("😧", "😧"), ("😮", "😮"), ("😲", "😲"),
                   ("😴", "😴"), ("🤤", "🤤"), ("😪", "😪"), ("😵", "😵"), ("🤐", "🤐"), ("🥴", "🥴"), ("🤢", "🤢"), ("🤮", "🤮"),
                   ("🤧", "🤧"), ("😷", "😷"), ("🤒", "🤒"), ("🤕", "🤕"), ("🤑", "🤑"), ("🤠", "🤠"), ("😈", "😈"), ("👿", "👿"),
                   ("👹", "👹"), ("👺", "👺"), ("🤡", "🤡"), ("💩", "💩"), ("👻", "👻"), ("💀", "💀"), ("☠️", "☠️"), ("👽", "👽"),
                   ("👾", "👾"), ("🤖", "🤖"), ("🎃", "🎃"), ("😺", "😺"), ("😸", "😸"), ("😹", "😹"), ("😻", "😻"), ("😼", "😼"),
                   ("😽", "😽"), ("🙀", "🙀"), ("😿", "😿"), ("😾", "😾"), ("👐", "👐"), ("🙌", "🙌"), ("👏", "👏"), ("🙏", "🙏"),
                   ("🤝", "🤝"), ("👍", "👍"), ("👎", "👎"), ("👊", "👊"),("✊", "✊"), ("🤛", "🤛"), ("🤜", "🤜"), ("🤞", "🤞"),
                   ("✌️", "✌️"), ("🤘", "🤘"), ("👌", "👌"), ("👈", "👈"),("👉", "👉"), ("👆", "👆"), ("👇", "👇"), ("☝️", "☝️"),
                   ("✋", "✋"), ("🤚", "🤚"), ("🖐", "🖐"), ("🖖", "🖖"), ("👋", "👋"), ("🤙", "🤙"), ("💪", "💪"), ("🖕", "🖕"),
                   ("🤟", "🤟"), ("🤲", "🤲"), ("✍️", "✍️"), ("🤳", "🤳"), ("💅", "💅"), ("🖖", "🖖"), ("💋", "💋"), ("👄", "👄"),
                   ("👅", "👅"), ("👂", "👂"), ("👃", "👃"), ("👣", "👣"), ("👁", "👁"), ("🧠", "🧠"), ("🦷", "🦷"), ("🦴", "🦴"),
                   ("👀", "👀"), ("🗣", "🗣"), ("👤", "👤"), ("👥", "👥"), ("👶", "👶"), ("👦", "👦"), ("👧", "👧"), ("👨", "👨"),
                   ("👩", "👩"), ("👱", "👱"), ("👴", "👴"), ("👵", "👵"), ("🧔", "🧔"), ("👨‍🦰", "👨‍🦰"), ("🧕", "🧕"), ("👲", "👲"),
                   ("👮", "👮"), ("👷", "👷"), ("💂", "💂"), ("🕵️", "🕵️"), ("👩‍⚕️", "👨‍⚕️"), ("👩‍🌾", "👨‍🌾"), ("👩‍🍳", "👨‍🍳"), ("👩‍🎓", "👨‍🎓"),
                   ("👩‍🎤", "👨‍🎤"), ("👩‍🏫", "👨‍🏫"), ("👩‍🏭", "👨‍🏭"), ("👩‍💻", "👨‍💻"), ("👩‍💼", "👨‍💼"), ("👩‍🔧", "👨‍🔧"), ("👩‍🔬", "👨‍🔬"), ("👩‍🎨", "👨‍🎨"),
                   ("👩‍🚒", "👨‍🚒"), ("👩‍🚀", "👨‍🚀"), ("🧟", "🧟"), ("🧛", "🧛‍♀️"), ("🧚", "🧚‍♂️")]

        row, col = 0, 0

        for symbol, code in smileys:
            button = QPushButton(symbol)
            button.setFont(QFont('Arial', 20))
            button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                border: 1px solid #4a4a4a;
                border-radius: 5px;
                padding: 10px;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 2px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 2px solid #004578;
            }
            """)
            button.clicked.connect(lambda _, s=code: self.insert_special_character(s))
            layout.addWidget(button, row, col)
            col += 1
            if col == 15:
                row += 1
                col = 0

        dialog.setLayout(layout)
        dialog.setFixedSize(1000, dialog.sizeHint().height())
        dialog.exec_()

    def show_special_characters2(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("special character")
        layout = QGridLayout(dialog)
        special_chars = [
            ("§", "§"), ("@", "@"), ("$", "$"), ("€", "€"), ("&", "&"),
            ("!", "!"), ("?", "?"), ("#", "#"), ("%", "%"), ("*", "*"),
            ("+", "+"), ("=", "="), ("/", "/"), ("\\", "\\"), ("^", "^"),
            ("~", "~"), ("_", "_"), ("|", "|"), ("`", "`"), ("´", "´"),
            (":", ":"), (";", ";"), (",", ","), (".", "."), ("'", "'"),
            ('"', '"'), ("(", "("), (")", ")"), ("[", "["), ("]", "]"),
            ("{", "{"), ("}", "}"), ("<", "<"), (">", ">"), ("÷", "÷"),
            ("×", "×"), ("∀", "∀"), ("∃", "∃"), ("∅", "∅"), ("∆", "∆"),
            ("∇", "∇"), ("∈", "∈"), ("∉", "∉"), ("∋", "∋"), ("∏", "∏"),
            ("∑", "∑"), ("−", "−"), ("√", "√"), ("∝", "∝"), ("∞", "∞"),
            ("∠", "∠"), ("∧", "∧"), ("∨", "∨"), ("∩", "∩"), ("∪", "∪"),
            ("∫", "∫"), ("≅", "≅"), ("≈", "≈"), ("≠", "≠"), ("≡", "≡"),
            ("≤", "≤"), ("≥", "≥"), ("⊂", "⊂"), ("⊃", "⊃"), ("⊆", "⊆"),
            ("⊇", "⊇"), ("⊕", "⊕"), ("⊗", "⊗"), ("⊥", "⊥"), ("⋅", "⋅"),
            ("⌈", "⌈"), ("⌉", "⌉"), ("⌊", "⌊"), ("⌋", "⌋"), ("〈", "〈"),
            ("〉", "〉"), ("←", "←"), ("→", "→"), ("↑", "↑"), ("↓", "↓"),
            ("↔", "↔"), ("↕", "↕"), ("⇒", "⇒"), ("⇔", "⇔"), ("α", "α"),
            ("β", "β"), ("γ", "γ"), ("δ", "δ"), ("ε", "ε"), ("ζ", "ζ"),
            ("η", "η"), ("θ", "θ"), ("ι", "ι"), ("κ", "κ"), ("λ", "λ"),
            ("μ", "μ"), ("ν", "ν"), ("ξ", "ξ"), ("ο", "ο"), ("π", "π"),
            ("ρ", "ρ"), ("σ", "σ"), ("τ", "τ"), ("υ", "υ"), ("φ", "φ"),
            ("χ", "χ"), ("ψ", "ψ"), ("ω", "ω"), ("Α", "Α"), ("Β", "Β"),
            ("Γ", "Γ"), ("Δ", "Δ"), ("Ε", "Ε"), ("Ζ", "Ζ"), ("Η", "Η"),
            ("Θ", "Θ"), ("Ι", "Ι"), ("Κ", "Κ"), ("Λ", "Λ"), ("Μ", "Μ"),
            ("Ν", "Ν"), ("Ξ", "Ξ"), ("Ο", "Ο"), ("Π", "Π"), ("Ρ", "Ρ"),
            ("Σ", "Σ"), ("Τ", "Τ"), ("Υ", "Υ"), ("Φ", "Φ"), ("Χ", "Χ"),
            ("Ψ", "Ψ"), ("Ω", "Ω"), ("ℵ", "ℵ"), ("ℶ", "ℶ"), ("ℷ", "ℷ"),
            ("ℸ", "ℸ"), ("∂", "∂"), ("∆", "∆"), ("∇", "∇"), ("⊗", "⊗"),
            ("⊕", "⊕"), ("√", "√"), ("ℵ", "ℵ"), ("∞", "∞"), ("∫", "∫"),
            ("≈", "≈"), ("≠", "≠"), ("≤", "≤"), ("≥", "≥"), ("↔", "↔"),
            ("←", "←"), ("↑", "↑"), ("→", "→"), ("↓", "↓")
        ]

        alphanumeric_chars = list(string.ascii_letters) + list(string.digits)
        special_chars.extend([(char, char) for char in alphanumeric_chars])

        def is_special_char(char):
            return any(char == spec_char[0] for spec_char in special_chars)

        row, col = 0, 0

        for symbol, code in special_chars:
            button = QPushButton(symbol)
            button.setFont(QFont('Arial', 14))
            button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                border: 1px solid #4a4a4a;
                border-radius: 5px;
                padding: 10px;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 2px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 2px solid #004578;
            }
            """)
            button.clicked.connect(lambda _, s=code: self.insert_special_character(s))
            layout.addWidget(button, row, col)
            col += 1
            if col == 15:
                row += 1
                col = 0

        dialog.setLayout(layout)
        dialog.setFixedSize(1000, dialog.sizeHint().height())
        dialog.exec_()

    def plus_update(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Updates")
        layout = QVBoxLayout(dialog)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        updates = [
            ("1. CHAT++ 2.0 HOME", """
                <p>Bis zu<br/>4B Paramater</p>
                <p>Größe<br/>4GB</p>
                <p>RAM<br/>4GB</p>
                <p>Content Length<br/>1K</p>
                <p>GQA<br/>X<br/></p>
                <p>Tokens<br/>X</p>
                <p>LR<br/>X</p>
                <p>Code<br/>X</p>
                <p>Commonsense Reasoning<br/>X</p>
                <p>World Knowledge<br/>X</p>
                <p>Reading Comprehension<br/>X</p>
                <p>Math<br/>X</p>
                <p>MMLU<br/>X</p>
                <p>BBH<br/>X</p>
                <p>AGI Eval<br/>X</p>

            """),
            ("2. CHAT++ 2.0 PRO", """
                <p>Bis zu<br/>7B Paramater</p>
                <p>Größe<br/>7GB</p>
                <p>RAM<br/>7GB</p><br/>
                <p>Content Length<br/>1K</p>
                <p>GQA<br/>X<br/></p>
                <p>Tokens<br/>2T</p>
                <p>LR<br/>0.0003</p>
                <p>Code<br/>14.1</p>
                <p>Commonsense Reasoning<br/>60.8</p>
                <p>World Knowledge<br/>46.2</p>
                <p>Reading Comprehension<br/>58.5</p>
                <p>Math<br/>6.95</p>
                <p>MMLU<br/>35.1</p>
                <p>BBH<br/>30.3</p>
                <p>AGI Eval<br/>23.9</p>
            """),
            ("3. CHAT++ 2.0 ULTRA", """
                <p>Bis zu<br/>13B Paramater</p>
                <p>Größe<br/>13GB</p>
                <p>RAM<br/>13GB</p>
                <p>Content Length<br/>1K</p>
                <p>GQA<br/>X<br/></p>
                <p>Tokens<br/>2T</p>
                <p>LR<br/>0.0003</p>
                <p>Code<br/>18.9</p>
                <p>Commonsense Reasoning<br/>66.1</p>
                <p>World Knowledge<br/>52.6</p>
                <p>Reading Comprehension<br/>62.3</p>
                <p>Math<br/>10.9</p>
                <p>MMLU<br/>46.9</p>
                <p>BBH<br/>37.0</p>
                <p>AGI Eval<br/>33.9</p>
            """),
            ("4. CHAT++ 3.0 HOME", """
                <p>Bis zu<br/>7B Paramater</p><br/>
                <p>Größe<br/>28GB</p><br/>
                <p>RAM<br/>28GB</p><br/>
                <p>Content Length<br/>4K</p><br/>
                <p>GQA<br/>X<br/></p><br/>
                <p>Tokens<br/>2T</p><br/>
                <p>LR<br/>0.0003</p><br/>
                <p>Code<br/>16.8</p><br/>
                <p>Commonsense Reasoning<br/>63.9</p><br/>
                <p>World Knowledge<br/>48.9</p><br/>
                <p>Reading Comprehension<br/>61.3</p><br/>
                <p>Math<br/>14.6</p><br/>
                <p>MMLU<br/>45.3</p><br/>
                <p>BBH<br/>32.6</p><br/>
                <p>AGI Eval<br/>29.3</p><br/>
            """),
            ("5. CHAT++ 3.0 PRO", """
                <p>Bis zu<br/>13B Paramater</p><br/>
                <p>Größe<br/>52GB</p><br/>
                <p>RAM<br/>52GB</p><br/>
                <p>Content Length<br/>4K</p><br/>
                <p>GQA<br/>X<br/></p><br/>
                <p>Tokens<br/>2T</p><br/>
                <p>LR<br/>0.0003</p><br/>
                <p>Code<br/>24.5</p><br/>
                <p>Commonsense Reasoning<br/>66.9</p><br/>
                <p>World Knowledge<br/>55.4</p><br/>
                <p>Reading Comprehension<br/>65.8</p><br/>
                <p>Math<br/>28.7</p><br/>
                <p>MMLU<br/>54.8</p><br/>
                <p>BBH<br/>39.4</p><br/>
                <p>AGI Eval<br/>39.1</p><br/>
            """),
            ("6. CHAT++ 3.0 ULTRA", """
                <p>Bis zu<br/>70B Paramater</p><br/>
                <p>Größe<br/>280GB</p><br/>
                <p>RAM<br/>280GB</p><br/>
                <p>Content Length<br/>4K</p><br/>
                <p>GQA<br/>✔</p><br/>
                <p>Tokens<br/>2T</p><br/>
                <p>LR<br/>0.00015</p><br/>
                <p>Code<br/>37.5</p><br/>
                <p>Commonsense Reasoning<br/>71.9</p><br/>
                <p>World Knowledge<br/>63.6</p><br/>
                <p>Reading Comprehension<br/>69.4</p><br/>
                <p>Math<br/>35.2</p><br/>
                <p>MMLU<br/>68.9</p><br/>
                <p>BBH<br/>51.2</p><br/>
                <p>AGI Eval<br/>54.2</p><br/>
            """),
            ("7. CHAT++ 4.0 HOME", "\n7. Update Beschreibung 1"),
            ("8. CHAT++ 4.0 PRO", "\n8. Update Beschreibung 2"),
            ("9. CHAT++ 4.0 ULTRA", "\n9. Update Beschreibung 3"),
            ("10. CHAT++ MINI HOME", "\n10. Update Beschreibung 1"),
            ("11. CHAT++ MINI PRO", "\n11. Update Beschreibung 2"),
            ("12. CHAT++ IMAGE RECOGNITION ASSISTANT", "\n12. Update Beschreibung 3"),
            ("13. CHAT++ FILE DISCOVERY ASSISTANT", "\n13. Update Beschreibung 3"),
            ("14. CHAT++ READING ASSISTANT", "\n14. Update Beschreibung 3"),
            ("15. CHAT++ VOICE ASSISTANT V1", "\n15. Update Beschreibung 3"),
            ("16. CHAT++ VOICE ASSISTANT V2", "\n16. Update Beschreibung 3"),
            ("17. CHAT++ VIDEO CHAT ASSISTANT", "\n17. Update Beschreibung 3"),
        ]

        for update, description in updates:
            widget = self.create_update_widget(update, description)
            scroll_layout.addWidget(widget)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)

        # Stile für die vertikale Scrollleiste
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
            }

            QScrollArea > QWidget > QWidget {
                background-color: #222222; /* Hintergrundfarbe der inneren Widgets */
            }

            QScrollArea > QWidget > QScrollBar:vertical {
                background-color: #222222; /* Hintergrundfarbe der inneren Widgets */
                width: 10px;
                border: none; /* Entfernt eventuelle Ränder */
            }

            QScrollBar::handle:vertical {
                background-color: #ffffff;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
            }

            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }
        """)

        layout.addWidget(scroll_area)
        dialog.setLayout(layout)

        # Set the dialog's size to be 800px wide and with a height limited to 700px
        dialog.setFixedSize(800, min(dialog.sizeHint().height(), 1200))
        dialog.exec_()

    def create_update_widget(self, update, description):
        widget = QWidget()
        widget_layout = QVBoxLayout(widget)

        label = QLabel(update)
        label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
            }
        """)
        widget_layout.addWidget(label)

        download_button = QPushButton("Download")
        download_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                border: 1px solid #4a4a4a;
                border-radius: 5px;
                padding: 10px;
                color: #ffffff;
                min-width: 50px;
                max-width: 50px;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 2px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 2px solid #004578;
            }
        """)
        widget_layout.addWidget(download_button)

        description_label = QLabel(description)
        description_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
        """)
        description_label.setVisible(False)
        widget_layout.addWidget(description_label)

        triangle_button = QPushButton("▼")
        triangle_button.setStyleSheet("""
            QPushButton {
                border: none;
                padding: 0;
                color: #ffffff;
                font-size: 16px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
        """)
        triangle_button.setFixedSize(20, 20)
        triangle_button.clicked.connect(lambda _, desc_label=description_label, button=triangle_button: self.toggle_description(desc_label, button))
        widget_layout.addWidget(triangle_button)

        return widget

    def toggle_description(self, description_label, triangle_button):
        if description_label.isVisible():
            description_label.setVisible(False)
            triangle_button.setText("▼")
        else:
            description_label.setVisible(True)
            triangle_button.setText("▲")

    def open_settings_window(self):
        settings_window = QDialog()
        settings_window.setWindowTitle("Settings")
        settings_window.setWindowIcon(QIcon('C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico'))  # Beispiel: Icon hinzufügen

        layout = QVBoxLayout(settings_window)
        tabs = QTabWidget()

        # Setze Größe des Dialogfensters
        settings_window.setGeometry(760, 400, 600, 400)

        # Setze Dark Mode für den Hintergrund
        settings_window.setStyleSheet("background-color: #2b2b2b; color: #000000;")

        # Allgemeine Einstellungen Tab
        general_tab = QWidget()
        general_layout = QFormLayout()

        # Benutzerdaten aus JSON lesen
        json_filename = 'accounts.json'
        accounts = self.read_json_file(json_filename)

        for user, password in accounts.items():
            name_edit = QLineEdit()
            name_edit.setText(user)
            name_edit.setReadOnly(True)
            name_edit.setStyleSheet("background-color: #363636; color: #ffffff; border: 1px solid #4a4a4a;")

            passwort_edit = QLineEdit()
            passwort_edit.setText(password)
            passwort_edit.setReadOnly(True)
            passwort_edit.setStyleSheet("background-color: #363636; color: #ffffff; border: 1px solid #4a4a4a;")

            general_layout.addRow("Benutzername:", name_edit)
            general_layout.addRow("Passwort:", passwort_edit)

        general_tab.setLayout(general_layout)
        tabs.addTab(general_tab, "Benutzer")

        # Netzwerkeinstellungen Tab
        network_tab = QWidget()
        network_layout = QFormLayout()
        ip_edit = QLineEdit()
        ip_edit.setStyleSheet("background-color: #363636; color: #ffffff; border: 1px solid #4a4a4a;")
        network_layout.addRow("IP Adresse:", ip_edit)

        port_edit = QLineEdit()
        port_edit.setStyleSheet("background-color: #363636; color: #ffffff; border: 1px solid #4a4a4a;")
        network_layout.addRow("Port:", port_edit)
        network_tab.setLayout(network_layout)
        tabs.addTab(network_tab, "Netzwerk")

        # Benutzeroberflächeneinstellungen Tab
        ui_tab = QWidget()
        ui_layout = QFormLayout()
        theme_edit = QLineEdit()
        theme_edit.setStyleSheet("background-color: #363636; color: #ffffff; border: 1px solid #4a4a4a;")
        ui_layout.addRow("Thema:", theme_edit)
        ui_tab.setLayout(ui_layout)
        tabs.addTab(ui_tab, "Benutzeroberfläche")

        layout.addWidget(tabs)

        # Schaltflächen hinzufügen
        button_layout = QHBoxLayout()
        save_button = QPushButton("Speichern")
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
                min-width: 80px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #0078d7;
                border: 3px solid #004578;
            }
            """)
        button_layout.addWidget(save_button)

        reset_button = QPushButton("Zurücksetzen")
        reset_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
                min-width: 80px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #ff4500;
            }
            QPushButton:pressed {
                background-color: #ff4500;
                border: 3px solid #b83500;
            }
            """)
        button_layout.addWidget(reset_button)

        close_button = QPushButton("Schließen")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: #ffffff;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
                min-width: 80px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 3px solid #808080;
            }
            QPushButton:pressed {
                background-color: #808080;
                border: 3px solid #404040;
            }
            """)
        close_button.clicked.connect(settings_window.close)
        button_layout.addWidget(close_button)

        layout.addLayout(button_layout)

        settings_window.setLayout(layout)
        settings_window.exec_()

    def read_json_file(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def img_re(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\start_test7-pic.bat')

    def vtv(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\start_test7-vtv.bat')

    def vc(self):
        os.system('')

    def vc_sec(self):
        os.system('')

    def ob_rec(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\start_test7-ro-rec.bat')

    def seccheck(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\start_test7-sec-check.bat')

    def img_gen(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\start_test7-img-gen.bat')

    def video_gen(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\peharge-chatpp-pro\\start_test7-img-gen.bat')

    def xcpp(self):
        os.system('C:\\Users\\julia\\PycharmProjects\\Xcpp\\run-model.bat')

    def insert_special_character(self, symbol):
        cursor = self.text_input_box.textCursor()
        cursor.insertText(symbol)
        self.text_input_box.setTextCursor(cursor)
        self.text_input_box.setFocus()

    def setup_chat_navigation(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
