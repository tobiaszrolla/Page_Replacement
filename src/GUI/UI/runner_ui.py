# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runner.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_runner(object):
    def setupUi(self, runner):
        if not runner.objectName():
            runner.setObjectName(u"runner")
        runner.resize(819, 545)
        self.gridLayout = QGridLayout(runner)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(runner)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(1000000)

        self.verticalLayout.addWidget(self.spinBox)

        self.spinBox_MemorySize = QSpinBox(self.widget)
        self.spinBox_MemorySize.setObjectName(u"spinBox_MemorySize")
        self.spinBox_MemorySize.setMaximum(1000000)

        self.verticalLayout.addWidget(self.spinBox_MemorySize)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(runner)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PushButton_SelectFile = QPushButton(runner)
        self.PushButton_SelectFile.setObjectName(u"PushButton_SelectFile")

        self.horizontalLayout.addWidget(self.PushButton_SelectFile)

        self.PushButton_Run = QPushButton(runner)
        self.PushButton_Run.setObjectName(u"PushButton_Run")

        self.horizontalLayout.addWidget(self.PushButton_Run)

        self.PushButton_Save = QPushButton(runner)
        self.PushButton_Save.setObjectName(u"PushButton_Save")

        self.horizontalLayout.addWidget(self.PushButton_Save)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)


        self.retranslateUi(runner)

        QMetaObject.connectSlotsByName(runner)
    # setupUi

    def retranslateUi(self, runner):
        runner.setWindowTitle(QCoreApplication.translate("runner", u"Form", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("runner", u"FIFO", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("runner", u"LRU", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("runner", u"LFU", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("runner", u"MFU", None))

        self.label_2.setText(QCoreApplication.translate("runner", u"Algorithm", None))
        self.label.setText(QCoreApplication.translate("runner", u"Max Time", None))
        self.label_3.setText(QCoreApplication.translate("runner", u"Memory Size", None))
        self.PushButton_SelectFile.setText(QCoreApplication.translate("runner", u"Select File", None))
        self.PushButton_Run.setText(QCoreApplication.translate("runner", u"Run", None))
        self.PushButton_Save.setText(QCoreApplication.translate("runner", u"Save", None))
    # retranslateUi

