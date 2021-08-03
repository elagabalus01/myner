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
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll = QtWidgets.QScrollArea(PredictionWidget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 298))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.btn_conf = QtWidgets.QCommandLinkButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_conf.sizePolicy().hasHeightForWidth())
        self.btn_conf.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/arrow_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_conf.setIcon(icon)
        self.btn_conf.setObjectName("btn_conf")
        self.gridLayout_2.addWidget(self.btn_conf, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.entradas_grid = QtWidgets.QGridLayout()
        self.entradas_grid.setObjectName("entradas_grid")
        self.gridLayout_2.addLayout(self.entradas_grid, 0, 1, 1, 3)
        self.lab_variable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_variable.sizePolicy().hasHeightForWidth())
        self.lab_variable.setSizePolicy(sizePolicy)
        self.lab_variable.setObjectName("lab_variable")
        self.gridLayout_2.addWidget(self.lab_variable, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.btn_prediction = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_prediction.setObjectName("btn_prediction")
        self.gridLayout_2.addWidget(self.btn_prediction, 1, 3, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lab_resultado = QtWidgets.QLabel(self.frame)
        self.lab_resultado.setTextFormat(QtCore.Qt.AutoText)
        self.lab_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_resultado.setObjectName("lab_resultado")
        self.gridLayout_3.addWidget(self.lab_resultado, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.frame, 2, 3, 1, 1)
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scroll, 0, 0, 1, 1)

        self.retranslateUi(PredictionWidget)
        QtCore.QMetaObject.connectSlotsByName(PredictionWidget)

    def retranslateUi(self, PredictionWidget):
        _translate = QtCore.QCoreApplication.translate
        PredictionWidget.setWindowTitle(_translate("PredictionWidget", "Form"))
        self.btn_conf.setText(_translate("PredictionWidget", "Configuración"))
        self.lab_variable.setText(_translate("PredictionWidget", "Variable:"))
        self.btn_prediction.setText(_translate("PredictionWidget", "Predecir"))
        self.lab_resultado.setText(_translate("PredictionWidget", "RESULTADO"))
from res import res_rc
