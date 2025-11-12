from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(399, 595)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #232526, stop: 1 #414345);\n"
"font-family: ARIAL;")
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
        self.start_text.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"    stop: 0 #b0b3b8,\n"
"    stop: 1 #3e3e3e);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font-weight: bold;\n"
"color: rgba(0, 0, 0, 180);")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(120, 320, 161, 41))
        font1 = QFont()
        font1.setFamilies([u"ARIAL"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.start_button.setFont(font1)
        self.start_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(0, 0, 0, 90);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(0, 0, 0, 100)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 170)\n"
"}")
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(270, 540, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"ARIAL"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.exit_button.setFont(font2)
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(0, 0, 0, 90);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(0, 0, 0, 100)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 170)\n"
"}")
        self.gpt_mode = QPushButton(self.centralwidget)
        self.gpt_mode.setObjectName(u"gpt_mode")
        self.gpt_mode.setGeometry(QRect(120, 390, 161, 41))
        self.gpt_mode.setFont(font1)
        self.gpt_mode.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(0, 0, 0, 90);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(0, 0, 0, 100)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 170)\n"
"}")
        self.defalut_mode = QPushButton(self.centralwidget)
        self.defalut_mode.setObjectName(u"defalut_mode")
        self.defalut_mode.setGeometry(QRect(120, 460, 161, 41))
        self.defalut_mode.setFont(font1)
        self.defalut_mode.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(0, 0, 0, 90);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(0, 0, 0, 100)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 170)\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jarvis", None))
        self.start_text.setText(QCoreApplication.translate("MainWindow", u"JARVIS", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.gpt_mode.setText(QCoreApplication.translate("MainWindow", u"GPT MODE", None))
        self.defalut_mode.setText(QCoreApplication.translate("MainWindow", u"DEFAULT MODE", None))
    # retranslateUi

