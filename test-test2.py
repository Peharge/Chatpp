import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QComboBox
from PyQt6.QtGui import QTextCursor, QFont
from PyQt6.QtCore import QThread, pyqtSignal, QDateTime, Qt
import ollama
import html
import json
import re
import pyttsx3
import subprocess

class OllamaWorker(QThread):
    response_signal = pyqtSignal(str)

    def __init__(self, model, conversation):
        super().__init__()
        self.model = model
        self.conversation = conversation

    def run(self):
        try:
            response_stream = ollama.chat(model=self.model, messages=self.conversation, stream=True)
            response_content = ""
            for chunk in response_stream:
                content = chunk['message']['content']
                response_content += content
                self.response_signal.emit(content)
                time.sleep(0.05)  # Kontrolliert die Geschwindigkeit des Datenstroms
            self.conversation.append({'role': 'assistant', 'content': response_content})
        except Exception as e:
            self.response_signal.emit(f"Ein Fehler ist aufgetreten: {e}")

class Terminal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.conversation = []
        self.chats = {}
        self.is_muted = False
        self.current_chat_index = 0

    def initUI(self):
        self.setWindowTitle("Chat++ Terminal")
        self.setGeometry(100, 100, 1000, 700)
        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: black; color: white;")
        self.output.setFont(QFont("Courier", 12))
        layout.addWidget(self.output)

        self.model_selector = QComboBox()
        self.model_selector.addItems(["Gamma", "Llama3", "Mistral", "Gemma2"])
        self.model_selector.setStyleSheet("background-color: #1e1e1e; color: #ffffff; border-radius: 5px; padding: 5px;")
        layout.addWidget(self.model_selector)

        self.input = QLineEdit()
        self.input.setStyleSheet(
            "background-color: #2d2d2d; color: #ffffff; border-radius: 5px; padding: 10px;"
            "border: 1px solid #3c3c3c; font-size: 14px;"
        )
        self.input.returnPressed.connect(self.on_enter)
        self.input.setFont(QFont("Courier", 12))
        self.input.setPlaceholderText("Gib hier deine Nachricht ein...")

        layout.addWidget(self.input)

        self.setLayout(layout)
        self.append_banner()
        self.append_welcome_message()

    def append_banner(self):
        banner_text = (
            "##############################################\n"
            "#                                            #\n"
            "#           Willkommen bei Chat++            #\n"
            "#                                            #\n"
            "##############################################\n"
        )
        self.output.append(banner_text)

    def append_welcome_message(self):
        welcome_text = (
            "\nMicrosoft Windows [Version 10.0.22631.3810]\n"
            "(c) Microsoft Corporation. Alle Rechte vorbehalten.\n"
        )
        self.output.append(welcome_text)

    def on_enter(self):
        user_input = self.input.text().strip()
        if not user_input:
            return

        if user_input.lower() == 'exit':
            self.close()
            return

        self.append_user_input(user_input)
        self.conversation.append({'role': 'user', 'content': user_input})
        self.input.clear()

        selected_model = self.model_selector.currentText().lower()
        self.worker = OllamaWorker(model=selected_model, conversation=self.conversation)
        self.worker.response_signal.connect(self.update_output)
        self.worker.start()

    def append_user_input(self, user_input):
        self.output.append(f"root@julian:~$ {user_input}\n\n")

    def update_output(self, content):
        self.output.moveCursor(QTextCursor.MoveOperation.End)
        self.output.insertPlainText(content)
        self.output.moveCursor(QTextCursor.MoveOperation.End)

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

    def speak_text(self, text):
        if not self.is_muted:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

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

    def append_chat_c(self, message, alignment):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    terminal = Terminal()
    terminal.show()
    sys.exit(app.exec())
