# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/Regression/Regression.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegressionWidget(object):
    def setupUi(self, RegressionWidget):
        RegressionWidget.setObjectName("RegressionWidget")
        RegressionWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(RegressionWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(RegressionWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 298))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_list = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.widget_list.setObjectName("widget_list")
        self.gridLayout_2.addWidget(self.widget_list, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(RegressionWidget)
        self.widget_list.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(RegressionWidget)

    def retranslateUi(self, RegressionWidget):
        _translate = QtCore.QCoreApplication.translate
        RegressionWidget.setWindowTitle(_translate("RegressionWidget", "Form"))
