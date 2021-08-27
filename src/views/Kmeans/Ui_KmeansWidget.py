# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/kmeans/kmeans.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KmeansWidget(object):
    def setupUi(self, KmeansWidget):
        KmeansWidget.setObjectName("KmeansWidget")
        KmeansWidget.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(KmeansWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(KmeansWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 638, 478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_list = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.widget_list.setObjectName("widget_list")
        self.verticalLayout_2.addWidget(self.widget_list)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(KmeansWidget)
        QtCore.QMetaObject.connectSlotsByName(KmeansWidget)

    def retranslateUi(self, KmeansWidget):
        _translate = QtCore.QCoreApplication.translate
        KmeansWidget.setWindowTitle(_translate("KmeansWidget", "Form"))
