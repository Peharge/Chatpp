import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QAction, QMenu, QSystemTrayIcon
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Fenstergröße und Titel setzen
        self.setWindowTitle('PyQt5 System Tray Icon Beispiel')
        self.setGeometry(100, 100, 300, 200)

        # Icon für das Fenster setzen (oben links)
        self.setWindowIcon(QIcon('peharge-logo3.6.ico'))

        # Buttons erstellen
        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2', self)
        button3 = QPushButton('Button 3', self)
        button4 = QPushButton('Button 4', self)

        # Layout erstellen und Buttons hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)

        # Layout für das Hauptfenster setzen
        self.setLayout(layout)

        # System Tray Icon erstellen
        self.createTrayIcon()

        # Hauptfenster anzeigen
        self.show()

    def createTrayIcon(self):
        self.tray_icon = QSystemTrayIcon(self)

        # Icon für das System Tray Icon setzen
        icon_path = "peharge-logo3.6.ico"
        icon = QIcon(icon_path)

        # Prüfen, ob das Icon gültig geladen wurde
        if icon.isNull():
            print("Fehler beim Laden des Icons:", icon_path)
        else:
            self.tray_icon.setIcon(icon)
            self.tray_icon.setVisible(True)

            # Kontextmenü für das System Tray Icon erstellen
            tray_menu = QMenu(self)
            action_quit = QAction('Beenden', self)
            action_quit.triggered.connect(self.closeEvent)
            tray_menu.addAction(action_quit)

            self.tray_icon.setContextMenu(tray_menu)

    def closeEvent(self, event):
        # System Tray Icon ausblenden, wenn Fenster geschlossen wird
        self.tray_icon.setVisible(False)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()

    # Um die Anwendung im System Tray zu halten (Windows-spezifisch)
    if sys.platform == 'win32':
        import ctypes
        app_id = 'MyApp'  # Beliebiger String
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    sys.exit(app.exec_())
