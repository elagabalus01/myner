# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/FS/Correlation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Correlation(object):
    def setupUi(self, Correlation):
        Correlation.setObjectName("Correlation")
        Correlation.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(Correlation)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Correlation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 638, 478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.correlation_grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.correlation_grid.setObjectName("correlation_grid")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.correlation_grid.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Correlation)
        QtCore.QMetaObject.connectSlotsByName(Correlation)

    def retranslateUi(self, Correlation):
        _translate = QtCore.QCoreApplication.translate
        Correlation.setWindowTitle(_translate("Correlation", "Form"))
        self.label.setText(_translate("Correlation", "Mapa de calor"))
