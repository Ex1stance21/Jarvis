import sys, threading
from PySide6.QtWidgets import QApplication, QMainWindow
from main import start_Jarvis
from ui_main import Ui_MainWindow
import main

class JarvisGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start_button_clicked)

    def start_button_clicked(self):
        threading.Thread(target=start_Jarvis, daemon=True).start()
        self.ui.start_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisGui()
    window.show()
    sys.exit(app.exec_())