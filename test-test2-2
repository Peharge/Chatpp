import sys
import time
import re
import html
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QComboBox
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, Qt
import ollama

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
        self.current_chat_index = 1

    def initUI(self):
        self.setWindowTitle("Chat++ Terminal")
        self.setGeometry(100, 100, 1000, 700)  # Größeres Fenster
        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: black; color: white;")
        self.output.setFont(QFont("Courier", 12))  # Größere Schriftgröße für bessere Lesbarkeit
        layout.addWidget(self.output)

        self.model_selector = QComboBox()
        self.model_selector.addItems(["Gamma", "Llama3", "Mistral", "phi3:14b"])
        self.model_selector.setStyleSheet("background-color: #1e1e1e; color: #ffffff; border-radius: 5px; padding: 5px;")  # Bessere Stilgestaltung
        layout.addWidget(self.model_selector)

        self.input = QLineEdit()
        self.input.setStyleSheet(
            "background-color: #2d2d2d; color: #ffffff; border-radius: 5px; padding: 10px;"
            "border: 1px solid #3c3c3c; font-size: 14px;"
        )  # Größere und schönere Eingabebox
        self.input.returnPressed.connect(self.on_enter)
        self.input.setFont(QFont("Courier", 12))  # Größere Schriftgröße für bessere Lesbarkeit
        self.input.setPlaceholderText("Gib hier deine Nachricht ein...")  # Platzhaltertext für das Eingabefeld

        layout.addWidget(self.input)  # Direktes Hinzufügen des Eingabefeldes zum Layout

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
        text_input = self.input.text().strip()  # Entfernt überflüssige Leerzeichen
        if not text_input:
            return  # Verhindert leere Eingaben

        if text_input.lower() == 'exit':
            self.close()
            return

        self.process_input(text_input)
        self.input.clear()

    def process_input(self, text_input):
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
            f"{image_chatbot}<br>"
            f"<font size='2' color='red'>{current_time}</font></div></html>"
        )
        self.append_chat_u(user_message, Qt.AlignRight)

        self.conversation.append({'role': 'user', 'content': text_input})

        selected_model = self.model_selector.currentText().lower()
        self.worker = OllamaWorker(model=selected_model, conversation=self.conversation)
        self.worker.response_signal.connect(self.update_output)
        self.worker.start()

    def append_chat_u(self, message, alignment):
        self.output.append(message)

    def append_chat_c(self, message, alignment):
        self.output.append(message)

    def update_output(self, content):
        self.output.moveCursor(QTextCursor.MoveOperation.End)
        self.output.insertPlainText(content)
        self.output.moveCursor(QTextCursor.MoveOperation.End)

        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")

        image_two = "C:\\Users\\julia\\OneDrive - Gewerbeschule Lörrach\\Pictures\\peharge-logo3.4.png"
        image_chatbot = f'<img src="{image_two}" width="30" height="30">'

        paragraphs = re.split(r'(\n\s*\n)', content)
        formatted_output = ""
        for para in paragraphs:
            if para.strip() == '':
                formatted_output += ""
            else:
                formatted_output += html.escape(para).replace('', '')

        # HTML für Chatbot-Nachricht
        chatbot_message = (
            f'<html><font color="white" size="3">{formatted_output}</font><br>'
            f'<style>body {{ line-height: 1.5; }}</style></body></html>'
        )
        self.append_chat_c(chatbot_message, Qt.AlignLeft)

        current_chat_name = f"Chat {self.current_chat_index}"

        if len(self.conversation) >= 2:
            # HTML für JSON-Datei (Benutzer-Nachricht)
            html_input = (
                f"<html><div style='text-align: right; border: 2px solid; "
                f"border-image: linear-gradient(to bottom, #ff00ff, #800080) 1; "
                f"border-radius: 10px; padding: 10px; margin: 5px; "
                f"background-color: rgb(34, 34, 34); color: #ffffff; width: max-content;'>"
                f"<font color='white' size='3'>{self.conversation[-2]['content']}</font><br>"
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    terminal = Terminal()
    terminal.show()
    sys.exit(app.exec())
