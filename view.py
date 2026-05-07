# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_resultLabel(object):
    def setupUi(self, resultLabel):
        if not resultLabel.objectName():
            resultLabel.setObjectName(u"resultLabel")
        resultLabel.resize(613, 383)
        self.centralwidget = QWidget(resultLabel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 0, 151, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 130, 91, 21))
        self.temperatureInput = QLineEdit(self.centralwidget)
        self.temperatureInput.setObjectName(u"temperatureInput")
        self.temperatureInput.setGeometry(QRect(200, 129, 321, 21))
        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setGeometry(QRect(170, 200, 75, 23))
        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(380, 200, 75, 23))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 270, 141, 21))
        resultLabel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(resultLabel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 613, 21))
        resultLabel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(resultLabel)
        self.statusbar.setObjectName(u"statusbar")
        resultLabel.setStatusBar(self.statusbar)

        self.retranslateUi(resultLabel)

        QMetaObject.connectSlotsByName(resultLabel)
    # setupUi

    def retranslateUi(self, resultLabel):
        resultLabel.setWindowTitle(QCoreApplication.translate("resultLabel", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("resultLabel", u"Fahrenheit to Celsius Converter", None))
        self.label_2.setText(QCoreApplication.translate("resultLabel", u"Enter Fahrenheit:", None))
        self.convertButton.setText(QCoreApplication.translate("resultLabel", u"Convert", None))
        self.clearButton.setText(QCoreApplication.translate("resultLabel", u"Clear", None))
        self.label_3.setText(QCoreApplication.translate("resultLabel", u"Result will appear here:", None))
    # retranslateUi

