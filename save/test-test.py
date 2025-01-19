import sys
import ollama
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal


class ChatWorker(QThread):
    text_received = pyqtSignal(str)

    def __init__(self, conversation, parent=None):
        super().__init__(parent)
        self.conversation = conversation
        self.running = True

    def run(self):
        try:
            response_stream = ollama.chat(model='llama3', messages=self.conversation, stream=True)
            response_content = ""

            # Sende das Präfix einmal, bevor der Text empfangen wird
            self.text_received.emit("\n\nchat++:\n")  # Präfix nur einmal senden

            for chunk in response_stream:
                if not self.running:
                    break
                content = chunk['message']['content']
                response_content += content
                # Verarbeite den Text, Wort für Wort
                words = content.split()
                for word in words:
                    self.text_received.emit(word)
                    time.sleep(0.05)  # Kleines Delay für einen "schreibenden" Effekt

            # Füge den gesamten Text zum Log hinzu, falls er noch nicht angezeigt wurde
            if response_content:
                self.text_received.emit("\n")  # Zeilenumbruch für bessere Lesbarkeit
                self.conversation.append({'role': 'assistant', 'content': response_content})

        except Exception as e:
            self.text_received.emit(f"Ein Fehler ist aufgetreten: {e}")

    def stop(self):
        self.running = False


class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.conversation = []
        self.worker = None

    def initUI(self):
        self.setWindowTitle('Chat mit Ollama')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.chat_log = QTextEdit(self)
        self.chat_log.setReadOnly(True)
        layout.addWidget(self.chat_log)

        self.user_input = QTextEdit(self)
        self.user_input.setPlaceholderText("Gib hier deine Nachricht ein...")
        layout.addWidget(self.user_input)

        self.send_button = QPushButton('Senden', self)
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_message(self):
        user_input = self.user_input.toPlainText().strip()
        if not user_input:
            return

        self.user_input.clear()
        self.chat_log.append(f"Du: {user_input}")

        self.conversation.append({'role': 'user', 'content': user_input})

        if self.worker:
            self.worker.stop()
            self.worker.wait()

        self.worker = ChatWorker(conversation=self.conversation)
        self.worker.text_received.connect(self.update_chat_log)
        self.worker.start()

    def update_chat_log(self, text):
        self.chat_log.moveCursor(self.chat_log.textCursor().End)
        self.chat_log.insertPlainText(text)
        self.chat_log.ensureCursorVisible()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChatApp()
    ex.show()
    sys.exit(app.exec_())
