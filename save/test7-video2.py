import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QProgressBar
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2
import ctypes
from ctypes import wintypes
from PyQt5 import QtGui
import sys
from PyQt5 import QtGui, QtWidgets
import ctypes
from ctypes import wintypes


class VideoPlayerApp(QMainWindow):
    def __init__(self, video_path, target_fps=60):
        super().__init__()
        self.video_path = video_path
        self.target_fps = target_fps

        self.video_width = 800
        self.video_height = 450  # Entspricht 16:9 Seitenverhältnis

        self.setWindowIcon(QtGui.QIcon(
            'C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6'))

        myappid = u'mycompany.myproduct.subproduct.version'  # Arbritary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        icon_path = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico"
        self.setWindowIcon(QIcon(icon_path))

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel()
        self.layout.addWidget(self.label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        self.layout.addWidget(self.progress_bar)

        # Setze die Position des Fortschrittsbalkens relativ zum Video
        progress_bar_height = 10
        progress_bar_margin_bottom = int(self.video_height * 0.2)
        self.progress_bar.setGeometry(0, self.video_height - progress_bar_margin_bottom,
                                       self.video_width, progress_bar_height)

        self.total_frames = self.get_total_frames()
        self.current_frame = 0

        self.cap = cv2.VideoCapture(self.video_path)
        self.show_frame()

    def get_total_frames(self):
        cap = cv2.VideoCapture(self.video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.release()
        return total_frames

    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.current_frame += 1
            progress = int(self.current_frame / self.total_frames * 100)
            self.progress_bar.setValue(progress)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (self.video_width, self.video_height))
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QPixmap.fromImage(QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888))
            self.label.setPixmap(q_img.scaled(self.video_width, self.video_height, Qt.KeepAspectRatio))

            delay = int(1000 / self.target_fps)
            QTimer.singleShot(delay, self.show_frame)
        else:
            self.cap.release()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayerApp("C:\\Users\\julia\\Videos\\peharge-intro4.5.2.mp4", target_fps=60)
    window.setWindowTitle("Peharge")
    window.show()
    sys.exit(app.exec_())
