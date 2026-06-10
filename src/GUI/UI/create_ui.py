# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Create(object):
    def setupUi(self, Create):
        if not Create.objectName():
            Create.setObjectName(u"Create")
        Create.resize(838, 757)
        self.gridLayout = QGridLayout(Create)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Create)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(Create)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(Create)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(Create)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(Create)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SpinBox_ContextChangeProb = QDoubleSpinBox(Create)
        self.SpinBox_ContextChangeProb.setObjectName(u"SpinBox_ContextChangeProb")
        self.SpinBox_ContextChangeProb.setMaximum(1.000000000000000)
        self.SpinBox_ContextChangeProb.setValue(0.500000000000000)

        self.verticalLayout.addWidget(self.SpinBox_ContextChangeProb)

        self.SpinBox = QSpinBox(Create)
        self.SpinBox.setObjectName(u"SpinBox")
        self.SpinBox.setMinimum(1)
        self.SpinBox.setMaximum(100000)
        self.SpinBox.setValue(1000)

        self.verticalLayout.addWidget(self.SpinBox)

        self.SpinBox_ContextSize = QSpinBox(Create)
        self.SpinBox_ContextSize.setObjectName(u"SpinBox_ContextSize")
        self.SpinBox_ContextSize.setMinimum(1)
        self.SpinBox_ContextSize.setMaximum(100000)
        self.SpinBox_ContextSize.setValue(100)

        self.verticalLayout.addWidget(self.SpinBox_ContextSize)

        self.SpinBox_ContextSize_2 = QSpinBox(Create)
        self.SpinBox_ContextSize_2.setObjectName(u"SpinBox_ContextSize_2")
        self.SpinBox_ContextSize_2.setMinimum(1)
        self.SpinBox_ContextSize_2.setMaximum(100000)
        self.SpinBox_ContextSize_2.setValue(100)

        self.verticalLayout.addWidget(self.SpinBox_ContextSize_2)

        self.SpinBox_PageNumber = QSpinBox(Create)
        self.SpinBox_PageNumber.setObjectName(u"SpinBox_PageNumber")
        self.SpinBox_PageNumber.setMinimum(1)
        self.SpinBox_PageNumber.setMaximum(100000)
        self.SpinBox_PageNumber.setValue(100)

        self.verticalLayout.addWidget(self.SpinBox_PageNumber)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.PushButton_CreateAndSave = QPushButton(Create)
        self.PushButton_CreateAndSave.setObjectName(u"PushButton_CreateAndSave")

        self.gridLayout.addWidget(self.PushButton_CreateAndSave, 1, 0, 1, 2)


        self.retranslateUi(Create)

        QMetaObject.connectSlotsByName(Create)
    # setupUi

    def retranslateUi(self, Create):
        Create.setWindowTitle(QCoreApplication.translate("Create", u"Form", None))
        self.label.setText(QCoreApplication.translate("Create", u"Context change probability", None))
        self.label_2.setText(QCoreApplication.translate("Create", u"Lenght", None))
        self.label_3.setText(QCoreApplication.translate("Create", u"Context Size", None))
        self.label_4.setText(QCoreApplication.translate("Create", u"Number of Processes", None))
        self.label_5.setText(QCoreApplication.translate("Create", u"Number of Pages", None))
        self.PushButton_CreateAndSave.setText(QCoreApplication.translate("Create", u"Create and Save", None))
    # retranslateUi

