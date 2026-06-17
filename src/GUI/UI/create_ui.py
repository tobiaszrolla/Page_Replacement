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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Create(object):
    def setupUi(self, Create):
        if not Create.objectName():
            Create.setObjectName(u"Create")
        Create.resize(838, 757)
        self.gridLayout = QGridLayout(Create)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Create)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Create)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SpinBox_ContextChangeProb = QDoubleSpinBox(self.widget_2)
        self.SpinBox_ContextChangeProb.setObjectName(u"SpinBox_ContextChangeProb")
        self.SpinBox_ContextChangeProb.setMaximum(1.000000000000000)
        self.SpinBox_ContextChangeProb.setValue(0.500000000000000)

        self.verticalLayout.addWidget(self.SpinBox_ContextChangeProb)

        self.SpinBox = QSpinBox(self.widget_2)
        self.SpinBox.setObjectName(u"SpinBox")
        self.SpinBox.setMinimum(1)
        self.SpinBox.setMaximum(100000)
        self.SpinBox.setValue(1000)

        self.verticalLayout.addWidget(self.SpinBox)

        self.SpinBox_ContextSize = QSpinBox(self.widget_2)
        self.SpinBox_ContextSize.setObjectName(u"SpinBox_ContextSize")
        self.SpinBox_ContextSize.setMinimum(1)
        self.SpinBox_ContextSize.setMaximum(100000)
        self.SpinBox_ContextSize.setValue(100)

        self.verticalLayout.addWidget(self.SpinBox_ContextSize)

        self.SpinBox_ContextSize_2 = QSpinBox(self.widget_2)
        self.SpinBox_ContextSize_2.setObjectName(u"SpinBox_ContextSize_2")
        self.SpinBox_ContextSize_2.setMinimum(1)
        self.SpinBox_ContextSize_2.setMaximum(100000)
        self.SpinBox_ContextSize_2.setValue(100)

        self.verticalLayout.addWidget(self.SpinBox_ContextSize_2)

        self.SpinBox_PageNumber = QSpinBox(self.widget_2)
        self.SpinBox_PageNumber.setObjectName(u"SpinBox_PageNumber")
        self.SpinBox_PageNumber.setMinimum(1)
        self.SpinBox_PageNumber.setMaximum(100000)
        self.SpinBox_PageNumber.setValue(100)

        self.verticalLayout.addWidget(self.SpinBox_PageNumber)

        self.SpinBox_WorkingSetSize = QSpinBox(self.widget_2)
        self.SpinBox_WorkingSetSize.setObjectName(u"SpinBox_WorkingSetSize")
        self.SpinBox_WorkingSetSize.setMinimum(1)
        self.SpinBox_WorkingSetSize.setMaximum(100000)
        self.SpinBox_WorkingSetSize.setValue(100)

        self.verticalLayout.addWidget(self.SpinBox_WorkingSetSize)

        self.SpinBox_PageReuseProbability = QDoubleSpinBox(self.widget_2)
        self.SpinBox_PageReuseProbability.setObjectName(u"SpinBox_PageReuseProbability")
        self.SpinBox_PageReuseProbability.setMinimum(0.010000000000000)
        self.SpinBox_PageReuseProbability.setMaximum(1.000000000000000)

        self.verticalLayout.addWidget(self.SpinBox_PageReuseProbability)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

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
        self.label_6.setText(QCoreApplication.translate("Create", u"Working Set Size", None))
        self.label_7.setText(QCoreApplication.translate("Create", u"Page reuse probability", None))
        self.PushButton_CreateAndSave.setText(QCoreApplication.translate("Create", u"Create and Save", None))
    # retranslateUi

