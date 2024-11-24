import sys
import os
import logging
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QTimer, Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

# Logging-Konfiguration
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class VideoPlayer(QMainWindow):
    def __init__(self, video_path, audio_path):
        super().__init__()
        self.video_path = video_path
        self.audio_path = audio_path
        self.video_capture = cv2.VideoCapture(self.video_path)
        self.setup_ui()
        self.setup_media_players()
        self.setup_timers()

    def setup_ui(self):
        self.setWindowTitle("Video Player")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showFullScreen()
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        icon_path = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            logging.error(f"Icon file not found at: {icon_path}")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.video_label = QLabel(self)
        self.video_label.setGeometry(self.rect())
        self.video_label.show()

        # Create an additional label for animation, initially hidden
        self.animation_label = QLabel(self)
        self.animation_label.setGeometry(self.rect())
        self.animation_label.setVisible(False)

    def setup_media_players(self):
        # Setup for video playback
        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_path)))

        # Setup for additional audio playback
        self.video_sound_player = self.create_media_player(self.audio_path)

    def create_media_player(self, file_path):
        player = QMediaPlayer()
        if os.path.exists(file_path):
            player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        else:
            logging.error(f"Media file not found at: {file_path}")
        return player

    def setup_timers(self):
        # Timer to start video and animation 2 seconds after audio starts
        self.start_delay_timer = QTimer()
        self.start_delay_timer.setSingleShot(True)
        self.start_delay_timer.timeout.connect(self.start_video_and_animation)

        # Timer to close the application after 20 seconds
        self.close_timer = QTimer()
        self.close_timer.timeout.connect(self.close)
        self.close_timer.start(20000)  # Close after 20 seconds

        # Start audio and set up timer to start video and animation
        self.video_sound_player.play()
        self.start_delay_timer.start(2000)  # 2000 ms = 2 seconds delay

    def start_video_and_animation(self):
        # Start video playback
        self.media_player.play()

        # Start showing the animation (or text)
        self.animation_label.setVisible(True)
        # Here you could add more functionality to update the animation or text

        # Setup a frame timer to update video frames
        self.frame_timer = QTimer()
        self.frame_timer.timeout.connect(self.update_frame)
        self.frame_timer.start(30)  # Update every 30 ms

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            screen_size = self.size()
            height, width, _ = frame.shape
            aspect_ratio = width / height
            new_width = screen_size.width()
            new_height = int(new_width / aspect_ratio)
            frame = cv2.resize(frame, (new_width, new_height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, _ = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.video_label.setPixmap(
                pixmap.scaled(self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.video_capture.release()
            self.frame_timer.stop()
            self.video_label.setVisible(False)
            self.close_timer.start(2000)  # Adjust the delay if needed


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_path = "C:\\Users\\julia\\Videos\\peharge-intro4.5.2.mp4"
    audio_path = "C:/Users/julia/PycharmProjects/peharge-chatpp-pro/aggressive-huge-hit-logo-139134.mp3"
    if not os.path.exists(video_path):
        logging.error(f"Video file not found at: {video_path}")
        sys.exit(1)
    if not os.path.exists(audio_path):
        logging.error(f"Audio file not found at: {audio_path}")
        sys.exit(1)
    player = VideoPlayer(video_path, audio_path)
    player.show()
    sys.exit(app.exec_())
