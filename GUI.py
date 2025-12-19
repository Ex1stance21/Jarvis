import sys, threading
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from main import start_jarvis, stop_jarvis

class JarvisGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.jarvis_thread = None
        self.jarvis_running = False

        self.ui.start_button.clicked.connect(self.toggle_jarvis)
        self.ui.exit_button.clicked.connect(self.close)

    def toggle_jarvis(self):
        if not self.jarvis_running:
            self.jarvis_running = True
            self.ui.start_button.setText("STOP")
            self.jarvis_thread = threading.Thread(target=start_jarvis, daemon=True)
            self.jarvis_thread.start()
        else:
            self.jarvis_running = False
            self.ui.start_button.setText("START")
            stop_jarvis()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisGui()
    window.show()
    sys.exit(app.exec())
