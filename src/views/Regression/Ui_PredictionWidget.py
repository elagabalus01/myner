# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/Regression/Prediction.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PredictionWidget(object):
    def setupUi(self, PredictionWidget):
        PredictionWidget.setObjectName("PredictionWidget")
        PredictionWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(PredictionWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll = QtWidgets.QScrollArea(PredictionWidget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 388, 288))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lab_prediction = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_prediction.sizePolicy().hasHeightForWidth())
        self.lab_prediction.setSizePolicy(sizePolicy)
        self.lab_prediction.setObjectName("lab_prediction")
        self.gridLayout_2.addWidget(self.lab_prediction, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.btn_prediction = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_prediction.setObjectName("btn_prediction")
        self.gridLayout_2.addWidget(self.btn_prediction, 1, 1, 1, 1)
        self.btn_conf = QtWidgets.QCommandLinkButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_conf.sizePolicy().hasHeightForWidth())
        self.btn_conf.setSizePolicy(sizePolicy)
        self.btn_conf.setObjectName("btn_conf")
        self.gridLayout_2.addWidget(self.btn_conf, 3, 1, 1, 1)
        self.entradas_grid = QtWidgets.QGridLayout()
        self.entradas_grid.setObjectName("entradas_grid")
        self.gridLayout_2.addLayout(self.entradas_grid, 0, 1, 1, 1)
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scroll, 0, 0, 1, 1)

        self.retranslateUi(PredictionWidget)
        QtCore.QMetaObject.connectSlotsByName(PredictionWidget)

    def retranslateUi(self, PredictionWidget):
        _translate = QtCore.QCoreApplication.translate
        PredictionWidget.setWindowTitle(_translate("PredictionWidget", "Form"))
        self.lab_prediction.setText(_translate("PredictionWidget", "Label: etiqueta"))
        self.btn_prediction.setText(_translate("PredictionWidget", "Predecir"))
        self.btn_conf.setText(_translate("PredictionWidget", "Configuración"))
