import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtCore import Qt
import torch
from diffusers import StableDiffusionPipeline
import numpy as np
import sys
from PyQt5.QtGui import QFont, QColor

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QListWidget, QListWidgetItem, QScrollArea, QDialog, QGridLayout, QFrame
import pyttsx3
from PyQt5.QtGui import QPixmap, QIcon, QPainter

from PyQt5.QtWidgets import QFileDialog, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMainWindow

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI image generator")
        self.setGeometry(100, 100, 800, 800)

        self.setWindowIcon(QtGui.QIcon(
            'C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6'))

        myappid = u'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        background_color = QColor(255, 255, 255)
        self.setStyleSheet(f"background-color: rgb({background_color.red()},{background_color.green()},{background_color.blue()})")

        glass_frame = QFrame(self)
        glass_frame.setGeometry(200, 200, 800, 600)
        glass_frame.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            color: #ffffff;
            border-radius: 10px;
        """)

        icon_path = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico"
        self.setWindowIcon(QIcon(icon_path))

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Layout erstellen
        layout = QVBoxLayout()

        # Label für das Bild
        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        # Textfeld für die Beschreibung
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Enter description")
        self.description_input.setStyleSheet("""
        
            QLineEdit { 
                height: 30px; 
                border: 2px solid #4a4a4a; 
                color: #black; 
                border-radius: 5px;
            }
        
        """)  # Setzen der Höhe auf 200px
        layout.addWidget(self.description_input)

        # Layout für die Buttons
        button_layout = QHBoxLayout()

        # Button erstellen und konfigurieren
        generate_button = QPushButton('Generate image')
        generate_button.setFixedSize(130, 30)

        generate_button.setFont(QFont('Arial', 10, QFont.Bold))

        # Stylesheet für den Button setzen
        generate_button.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #black;
                border-radius: 5px;
                border: 2px solid #4a4a4a;
            }
            QPushButton:hover {
                background-color: #ffffff;
                border: 3px solid #0078d7;
            }
            QPushButton:pressed {
                background-color: #ffffff;
                border: 3px solid #004578;
            }
        """)

        # Button dem Layout hinzufügen und mit Methode verbinden
        button_layout.addWidget(generate_button)
        generate_button.clicked.connect(self.generate_image)

        # Container-Widget
        container = QWidget()
        container.setLayout(layout)

        # Layout für Hauptfenster setzen
        main_layout = QVBoxLayout()
        main_layout.addWidget(container)
        main_layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Laden des KI-Modells
        self.pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32)
        self.pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

        # Platzhalter für QPixmap
        self.pixmap = None

    def generate_image(self):
        prompt = self.description_input.text()
        if prompt.strip() == "":
            prompt = "Ein wunderschöner Sonnenuntergang am Strand"  # Fallback, falls keine Eingabe erfolgt
        image = self.pipeline(prompt).images[0]
        self.display_image(image)

    def display_image(self, image):
        # Convert PIL image to numpy array
        image_np = np.array(image.convert("RGB"))

        # Convert numpy array to QImage
        height, width, channel = image_np.shape
        qimage = QImage(image_np.data, width, height, width * channel, QImage.Format_RGB888)

        # Display QImage in QLabel
        self.pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setScaledContents(True)

# Hauptanwendung
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
