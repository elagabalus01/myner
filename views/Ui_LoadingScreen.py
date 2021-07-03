# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/loading_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadingScreen(object):
    def setupUi(self, LoadingScreen):
        LoadingScreen.setObjectName("LoadingScreen")
        LoadingScreen.resize(600, 300)
        self.gridLayout = QtWidgets.QGridLayout(LoadingScreen)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(187, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.loading_bar = QtWidgets.QProgressBar(LoadingScreen)
        self.loading_bar.setProperty("value", 0)
        self.loading_bar.setObjectName("loading_bar")
        self.gridLayout.addWidget(self.loading_bar, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(187, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(LoadingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoadingScreen)

    def retranslateUi(self, LoadingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoadingScreen.setWindowTitle(_translate("LoadingScreen", "Dialog"))
