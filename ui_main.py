from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QMainWindow, QPushButton, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(399, 595)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #232526, stop: 1 #414345);\n"
            "font-family: ARIAL;"
        )

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.start_text = QLabel(self.centralwidget)
        self.start_text.setObjectName(u"start_text")
        self.start_text.setGeometry(QRect(60, 90, 271, 61))
        font = QFont()
        font.setFamilies([u"ARIAL"])
        font.setPointSize(48)
        font.setBold(True)
        self.start_text.setFont(font)
        self.start_text.setMouseTracking(False)
        self.start_text.setStyleSheet(
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
            "    stop: 0 #b0b3b8,\n"
            "    stop: 1 #3e3e3e);\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 15px;\n"
            "font-weight: bold;\n"
            "color: rgba(0, 0, 0, 180);"
        )

        font_btn = QFont()
        font_btn.setFamilies([u"ARIAL"])
        font_btn.setPointSize(14)
        font_btn.setBold(True)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(120, 320, 161, 41))
        self.start_button.setFont(font_btn)
        self.start_button.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgba(0, 0, 0, 90);\n"
            "border: 1px solid rgb(255, 255, 255);\n"
            "border-radius: 15px\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color:rgba(0, 0, 0, 100)\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(0, 0, 0, 170)\n"
            "}"
        )

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(120, 380, 161, 41))
        self.exit_button.setFont(font_btn)
        self.exit_button.setStyleSheet(
            "QPushButton {\n"
            "background-color: rgba(0, 0, 0, 90);\n"
            "border: 1px solid rgb(255, 255, 255);\n"
            "border-radius: 15px\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color:rgba(0, 0, 0, 100)\n"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(0, 0, 0, 170)\n"
            "}"
        )

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jarvis", None))
        self.start_text.setText(QCoreApplication.translate("MainWindow", u"JARVIS", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))


