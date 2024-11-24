import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie, QColor, QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets

class GIFDisplayWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Security Peharge")
        self.setFixedSize(400, 400)  # Fenstergröße festlegen

        self.setWindowIcon(QtGui.QIcon(
            'C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6'))

        self.setWindowOpacity(0.75)

        # Hintergrundfarbe des Fensters auf Schwarz setzen
        self.setStyleSheet("background-color: black;")

        # QLabel erstellen, um das GIF anzuzeigen
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignCenter)

        # Text "Security Peharge" in Neon Grün anzeigen
        self.label_text = QLabel("YOU ARE SAFE!!!", self)
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_text.setStyleSheet("color: rgb(0, 255, 0); font-size: 20px; font-weight: bold;")

        # GIF laden und anzeigen
        self.movie = QMovie('sec-check.gif')
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        # Layout einrichten
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_text)
        layout.addWidget(self.gif_label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GIFDisplayWidget()
    window.show()
    sys.exit(app.exec_())
