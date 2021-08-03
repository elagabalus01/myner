# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/Regression/RegressionConf.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegressionConfWidget(object):
    def setupUi(self, RegressionConfWidget):
        RegressionConfWidget.setObjectName("RegressionConfWidget")
        RegressionConfWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(RegressionConfWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll = QtWidgets.QScrollArea(RegressionConfWidget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 298))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.test_percentage = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_percentage.sizePolicy().hasHeightForWidth())
        self.test_percentage.setSizePolicy(sizePolicy)
        self.test_percentage.setMinimum(5)
        self.test_percentage.setMaximum(100)
        self.test_percentage.setObjectName("test_percentage")
        self.gridLayout_2.addWidget(self.test_percentage, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.features_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.features_box.setObjectName("features_box")
        self.gridLayout_2.addWidget(self.features_box, 1, 1, 1, 1)
        self.btn_calcular = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btn_calcular.setObjectName("btn_calcular")
        self.gridLayout_2.addWidget(self.btn_calcular, 2, 1, 1, 1)
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scroll, 0, 0, 1, 1)

        self.retranslateUi(RegressionConfWidget)
        QtCore.QMetaObject.connectSlotsByName(RegressionConfWidget)

    def retranslateUi(self, RegressionConfWidget):
        _translate = QtCore.QCoreApplication.translate
        RegressionConfWidget.setWindowTitle(_translate("RegressionConfWidget", "Form"))
        self.label_2.setText(_translate("RegressionConfWidget", "Característica a predecir"))
        self.label.setText(_translate("RegressionConfWidget", "Proporcion para prueba %"))
        self.btn_calcular.setText(_translate("RegressionConfWidget", "Generar modelo"))
