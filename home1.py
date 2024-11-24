
from PyQt5.QtCore import QSize, Qt
import ctypes
import sys
from PyQt5.QtGui import QFont, QColor

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QListWidget, QListWidgetItem, QScrollArea, QDialog, QGridLayout, QFrame
import pyttsx3
from PyQt5.QtGui import QPixmap, QIcon, QPainter
from PyQt5.QtSvg import QSvgRenderer
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

class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chat++ mini Pro')
        self.setGeometry(660, 200, 800, 600)

        self.setWindowIcon(QtGui.QIcon(
            'C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6'))

        myappid = u'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        background_color = QColor(34, 34, 34)
        self.setStyleSheet(f"background-color: rgb({background_color.red()},{background_color.green()},{background_color.blue()})")
        self.setWindowOpacity(0.9)

        glass_frame = QFrame(self)
        glass_frame.setGeometry(200, 200, 800, 600)
        glass_frame.setStyleSheet("""
            background-color: rgb(34, 34, 34);
            color: #ffffff;
            border-radius: 10px;
        """)

        icon_path = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico"
        self.setWindowIcon(QIcon(icon_path))

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(50, 50, 700, 200)
        pixmap = QPixmap('C:/Users/julia/OneDrive - Gewerbeschule Lörrach/Pictures/software/peharge-logo3.62.png')
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        self.background_label.setPixmap(pixmap)
        self.background_label.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)

        button_container = QWidget()
        button_layout = QVBoxLayout(button_container)

        svg_paths = [
            'C:/Users/julia/PycharmProjects/test23/microsoft.svg',
            'C:/Users/julia/PycharmProjects/test23/apple.svg',
            'C:/Users/julia/PycharmProjects/test23/google.svg',
            'C:/Users/julia/PycharmProjects/test23/youtube.svg',
            'C:/Users/julia/PycharmProjects/test23/facebook.svg',
            'C:/Users/julia/PycharmProjects/test23/linkin.svg',
            'C:/Users/julia/PycharmProjects/test23/tiktok.svg',
            'C:/Users/julia/PycharmProjects/test23/instagram.svg',
            'C:/Users/julia/PycharmProjects/test23/linux.svg',
            'C:/Users/julia/PycharmProjects/test23/ubuntu.svg',
            'C:/Users/julia/PycharmProjects/test23/debian.svg',
            'C:/Users/julia/PycharmProjects/test23/anaconda.svg',
            'C:/Users/julia/PycharmProjects/test23/python.svg',
            'C:/Users/julia/PycharmProjects/test23/meta.svg',
            'C:/Users/julia/PycharmProjects/test23/llama.svg',
            'C:/Users/julia/PycharmProjects/test23/pytorch.svg',
            'C:/Users/julia/PycharmProjects/test23/tensorflow.svg',
            'C:/Users/julia/PycharmProjects/test23/keras.svg',
            'C:/Users/julia/PycharmProjects/test23/openai.svg',
            'C:/Users/julia/PycharmProjects/test23/pycharm.svg',
            'C:/Users/julia/PycharmProjects/test23/jupyter.svg',
            'C:/Users/julia/PycharmProjects/test23/qt-img.svg',
            'C:/Users/julia/PycharmProjects/test23/huggingface-img.svg',
            'C:/Users/julia/PycharmProjects/test23/github-img.svg',
            'C:/Users/julia/PycharmProjects/test23/Googledrive-img.svg',
            'C:/Users/julia/PycharmProjects/test23/pandas-img.svg',
            'C:/Users/julia/PycharmProjects/test23/git-img.svg',
            'C:/Users/julia/PycharmProjects/test23/conda-img.svg',
        ]

        row_layout = None
        for i, svg_path in enumerate(svg_paths):
            if i % 7 == 0:
                row_layout = QHBoxLayout()
                button_layout.addLayout(row_layout)

            button = QPushButton()
            renderer = QSvgRenderer(svg_path)
            pixmap = QPixmap(renderer.defaultSize())
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            icon = QIcon(pixmap)
            shadow_effect = QGraphicsDropShadowEffect(self)
            shadow_effect.setBlurRadius(10)
            shadow_effect.setColor(Qt.black)
            shadow_effect.setOffset(5, 5)
            button.setGraphicsEffect(shadow_effect)
            button.setIcon(icon)
            button.setIconSize(QSize(30, 30))
            button.setFixedSize(70, 40)
            button.setFont(QFont('Arial', 12))
            button.setStyleSheet("""
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
            row_layout.addWidget(button)

        main_layout.addWidget(self.background_label)
        main_layout.addWidget(button_container)
        self.setLayout(main_layout)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())
