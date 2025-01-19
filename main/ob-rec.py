import sys
import torch
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QFont, QIcon, QColor

import sys
from PyQt5 import QtGui, QtWidgets
import ctypes
from ctypes import wintypes

# Laden des YOLOv5-Modells
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.eval()

class CameraWidget(QWidget):
    def __init__(self, camera_index):
        super().__init__()
        self.initUI()

        self.setWindowTitle('Chat++ mini Pro')
        self.setGeometry(400, 400, 600, 500)

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

        # Zugriff auf die Kamera
        self.capture = cv2.VideoCapture(camera_index)
        if not self.capture.isOpened():
            print(f"Kamera mit Index {camera_index} konnte nicht geöffnet werden.")
            sys.exit()

        # Timer für regelmäßiges Frame-Update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30 ms

    def initUI(self):
        self.layout = QVBoxLayout()

        # Label zum Anzeigen des Kamerabilds
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.setLayout(self.layout)
        self.setWindowTitle('PC Kamera mit YOLOv5 Objekterkennung')
        self.show()

    def update_frame(self):
        ret, frame = self.capture.read()
        if not ret:
            print("Frame konnte nicht gelesen werden.")
            return

        # YOLOv5 Objekterkennung
        results = model(frame)
        detections = results.pandas().xyxy[0]

        # Zeichne die Bounding-Boxes und Labels
        for _, row in detections.iterrows():
            x1, y1, x2, y2, confidence, class_id, name = row
            if confidence >= 0.5:  # Nur Objekte mit hoher Sicherheit anzeigen
                frame = cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                frame = cv2.putText(frame, f"{name} {confidence:.2f}", (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Anzeige des Bildes in der PyQt5 Oberfläche
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_img))

    def closeEvent(self, event):
        self.capture.release()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Verwenden Sie hier den richtigen Kameraindex
    ex = CameraWidget(camera_index=0)
    sys.exit(app.exec_())
