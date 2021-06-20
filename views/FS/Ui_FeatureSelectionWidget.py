# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_src/FS/FeatureSelectionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FeatureSelectionWidget(object):
    def setupUi(self, FeatureSelectionWidget):
        FeatureSelectionWidget.setObjectName("FeatureSelectionWidget")
        FeatureSelectionWidget.resize(695, 501)
        self.verticalLayout = QtWidgets.QVBoxLayout(FeatureSelectionWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(FeatureSelectionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 693, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.method_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.method_box.setObjectName("method_box")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.gridLayout_2.addWidget(self.method_box, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 2)
        self.method = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method.sizePolicy().hasHeightForWidth())
        self.method.setSizePolicy(sizePolicy)
        self.method.setObjectName("method")
        self.gridLayout_2.addWidget(self.method, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(FeatureSelectionWidget)
        self.method.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(FeatureSelectionWidget)

    def retranslateUi(self, FeatureSelectionWidget):
        _translate = QtCore.QCoreApplication.translate
        FeatureSelectionWidget.setWindowTitle(_translate("FeatureSelectionWidget", "Form"))
        self.label.setText(_translate("FeatureSelectionWidget", "Herramientas para la toma de decisiones"))
        self.method_box.setItemText(0, _translate("FeatureSelectionWidget", "Evaluación visual"))
        self.method_box.setItemText(1, _translate("FeatureSelectionWidget", "Relación entre variables"))
        self.method_box.setItemText(2, _translate("FeatureSelectionWidget", "Análisis de componentes principales"))
        self.groupBox.setTitle(_translate("FeatureSelectionWidget", "Selección de características"))
        self.checkBox.setText(_translate("FeatureSelectionWidget", "CheckBox"))
