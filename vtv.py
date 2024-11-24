import os
from pydub import AudioSegment

ffmpeg_path = "C:\\Users\\julia\\anaconda3\\envs\\peharge_chatpp\\Library\\bin\\ffmpeg.exe"
AudioSegment.converter = ffmpeg_path

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFrame
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QMovie, QColor
import sounddevice as sd
import numpy as np
import subprocess
import whisper
import os
import datetime
from TTS.api import TTS
import pygame
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play
import ctypes
from ctypes import wintypes
from PyQt5 import QtGui
import sys
from PyQt5 import QtGui, QtWidgets
import ctypes
from ctypes import wintypes
import ctypes
from ctypes import wintypes
from PyQt5 import QtGui
import sys
from PyQt5 import QtGui, QtWidgets
import ctypes
from ctypes import wintypes
import pygame
import logging
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

class AudioThread(QThread):
    audio_signal = pyqtSignal(np.ndarray)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        fs = 16000
        duration = 5
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
        sd.wait()
        self.audio_signal.emit(np.squeeze(recording))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Voice to Voice Application")
        self.setFixedSize(800, 600)

        self.setWindowIcon(QtGui.QIcon(
            'C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6'))

        myappid = u'mycompany.myproduct.subproduct.version'  # Arbritary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        icon_path = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\software\\peharge-logo3.6.ico"
        self.setWindowIcon(QIcon(icon_path))

        background_color = QColor(18,19,35,255)
        self.setStyleSheet("background-color: rgb({},{},{})".format(
            background_color.red(), background_color.green(),
            background_color.blue()))

        self.setWindowOpacity(0.9)

        glass_frame = QFrame(self)
        glass_frame.setGeometry(0, 0, 500, 400)
        glass_frame.setStyleSheet("""
            background-color: rgba(11,12,29,255)
            border-radius: 10px;
            color: #ffffff;
        """)

        self.label = QLabel("Press the button and speak", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #ffffff;")
        self.label.setGeometry(300, 525, 200, 50)

        self.animation_label = QLabel(self)
        self.movie = QMovie("peharge-speak.gif")
        self.animation_label.setMovie(self.movie)
        self.movie.start()
        self.animation_label.setGeometry(0, 0, 500, 284)
        self.animation_label.hide()
        self.animation_label.setFixedSize(800, 600)

        button_layout = QHBoxLayout()

        self.button = QPushButton("Start Listening", self)
        self.button.setStyleSheet("""
            QPushButton {
                background: rgba(0, 0, 0, 0);
                color: #ffffff;
                border-radius: 10px;
                border: none;
                border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #ff00ff, stop: 1 #800080);
            }
            QPushButton:hover {
                border: 3px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #ff00ff, stop: 1 #800080);
            }
            QPushButton:pressed {
                border: 4px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #ff00ff, stop: 1 #800080);
            }
        """)
        self.button.setGeometry(350, 475, 100, 50)
        self.button.clicked.connect(self.start_listening)

        # Definiere eine Funktion, um den Button um 10px nach oben zu verschieben.
        def move_button_up():
            self.button.move(self.button.x(), self.button.y() - 5)

        # Definiere eine Funktion, um den Button um 10px nach unten zu verschieben.
        def move_button_down(button):
            if not button.isChecked():
                button.move(button.x(), button.y() + 5)

        # Verbinde die Funktionen mit den entsprechenden Signalen.
        self.button.pressed.connect(move_button_up)
        self.button.released.connect(lambda: move_button_down(self.button))

        # Verbinde die enterEvent und leaveEvent mit den Funktionen.
        self.button.enterEvent = lambda event: move_button_up()
        self.button.leaveEvent = lambda event: move_button_down(self.button)

        self.setLayout(button_layout)

        self.result_label = QLabel("", self)
        self.result_label.setStyleSheet("color: #ffffff;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("background-color: none")
        self.result_label.setGeometry(300, 525, 200, 50)

    def start_listening(self):
        try:
            self.label.setText("Listening...")
            self.animation_label.show()

            self.audio_thread = AudioThread()
            self.audio_thread.audio_signal.connect(self.process_audio)
            self.audio_thread.start()
        except Exception as e:
            print("An exception occurred:", e)

    def process_audio(self, audio):
        try:
            self.label.setText("Transcribing with Whisper...")

            result = model.transcribe(audio, fp16=False)
            text = result["text"]

            self.label.setText("Processing with Chatpp...")
            llama3_output = run_command_and_get_output("ollama run llava:7b", text)
            self.result_label.setText(llama3_output.strip())

            self.process_with_professional_tool(llama3_output.strip())
            # Aktivieren Sie den Button erneut
            self.button.setEnabled(True)
        except Exception as e:
            print("An exception occurred:", e)

    def process_with_professional_tool(self, text_output, language="de"):
        try:
            if language == "de":
                model_name = "tts_models/de/thorsten/tacotron2-DCA"
            elif language == "en":
                model_name = "path/to/english/tts/model"

            tts = TTS(model_name=model_name, progress_bar=False, gpu=False)
            current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            output_filename = f"output_{current_time}.wav"
            tts.tts_to_file(text=text_output, file_path=output_filename)

            # Xtts-Modell verwenden
            config = XttsConfig()
            config.load_json(os.path.join("C:/Users/julia/Downloads/xtts-v2", "config.json"))
            xtts_model = Xtts(config)
            xtts_model.load_checkpoint(config, checkpoint_dir="C:/Users/julia/Downloads/xtts-v2", eval=True)

            speaker_wav_path = os.path.join("C:\\Users\\julia\\Downloads\\xtts-v2\\sample\\de_sample.wav")

            if not os.path.exists(speaker_wav_path):
                raise FileNotFoundError(
                    f"Die Datei {speaker_wav_path} existiert nicht. Bitte überprüfen Sie den Pfad und versuchen Sie es erneut.")

            outputs = xtts_model.synthesize(
                text_output,
                config,
                speaker_wav=speaker_wav_path,
                gpt_cond_len=3,
                language="de",
            )

            output_file = f"output_{current_time}_xtts.wav"
            if "wav" in outputs.keys():
                sample_rate = config.audio['sample_rate']
                with sf.SoundFile(output_file, "w", samplerate=sample_rate, channels=1) as file:
                    file.write(outputs["wav"])
                print(f"Die Audiodatei wurde erfolgreich gespeichert unter: {output_file}")

                # Audiowiedergabe mit pygame
                pygame.mixer.init()
                pygame.mixer.music.load(output_file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

            else:
                raise KeyError("Output dictionary does not contain 'wav'")

            # Löschen der temporären Dateien
            if os.path.exists(output_filename):
                os.remove(output_filename)

            if os.path.exists(output_file):
                os.remove(output_file)

        except FileNotFoundError as e:
            print("FileNotFoundError:", e)
        except KeyError as e:
            print("KeyError:", e)
        except Exception as e:
            print("An exception occurred:", e)


def run_command_and_get_output(command, text_input):
    try:
        result = subprocess.run(command, input=text_input, shell=True, check=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, encoding='utf-8')
        return result.stdout
    except subprocess.CalledProcessError as e:
        return "Fehler beim Ausführen des Befehls: " + str(e)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        model = whisper.load_model("base")
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("An exception occurred:", e)
