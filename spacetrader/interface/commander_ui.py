# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commander.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(160, 160)
        MainWindow.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        icon = QIcon()
        icon.addFile(u"../images/App.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(20, 20))
        MainWindow.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 110, 14, 14))
        self.pushButton.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u"../images/increase_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(14, 14))
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 70, 14, 14))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(14, 14))
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 90, 14, 14))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(14, 14))
        self.pushButton_3.setFlat(True)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 50, 14, 14))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(14, 14))
        self.pushButton_4.setFlat(True)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(55, 45, 14, 14))
        self.pushButton_5.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"../images/decrease_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(14, 14))
        self.pushButton_5.setFlat(True)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(55, 110, 14, 14))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(14, 14))
        self.pushButton_6.setFlat(True)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(55, 85, 14, 14))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(14, 14))
        self.pushButton_7.setFlat(True)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(50, 65, 14, 14))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(14, 14))
        self.pushButton_8.setFlat(True)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(45, 130, 80, 25))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(72, 10, 76, 25))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 9, 161, 151))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Space Trader", None))
        MainWindow.setWindowFilePath("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

