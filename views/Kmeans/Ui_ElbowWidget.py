# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/kmeans/Elbow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ElbowWidget(object):
    def setupUi(self, ElbowWidget):
        ElbowWidget.setObjectName("ElbowWidget")
        ElbowWidget.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(ElbowWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(ElbowWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 620, 460))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(581, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.btn_calcular = QtWidgets.QCommandLinkButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calcular.sizePolicy().hasHeightForWidth())
        self.btn_calcular.setSizePolicy(sizePolicy)
        self.btn_calcular.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_calcular.setObjectName("btn_calcular")
        self.gridLayout_2.addWidget(self.btn_calcular, 2, 1, 1, 1)
        self.title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1)
        self.graph_grid = QtWidgets.QGridLayout()
        self.graph_grid.setObjectName("graph_grid")
        self.gridLayout_2.addLayout(self.graph_grid, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.retranslateUi(ElbowWidget)
        QtCore.QMetaObject.connectSlotsByName(ElbowWidget)

    def retranslateUi(self, ElbowWidget):
        _translate = QtCore.QCoreApplication.translate
        ElbowWidget.setWindowTitle(_translate("ElbowWidget", "Form"))
        self.btn_calcular.setText(_translate("ElbowWidget", "Calcular k-means"))
        self.title.setText(_translate("ElbowWidget", "Metodo del codo"))
