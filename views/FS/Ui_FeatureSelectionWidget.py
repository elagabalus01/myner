# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/FS/FeatureSelectionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FeatureSelectionWidget(object):
    def setupUi(self, FeatureSelectionWidget):
        FeatureSelectionWidget.setObjectName("FeatureSelectionWidget")
        FeatureSelectionWidget.resize(695, 501)
        self.gridLayout_3 = QtWidgets.QGridLayout(FeatureSelectionWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setBaseSize(QtCore.QSize(0, 0))
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.method_box = QtWidgets.QComboBox(self.widget)
        self.method_box.setObjectName("method_box")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.gridLayout.addWidget(self.method_box, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.method = QtWidgets.QStackedWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method.sizePolicy().hasHeightForWidth())
        self.method.setSizePolicy(sizePolicy)
        self.method.setObjectName("method")
        self.gridLayout.addWidget(self.method, 2, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(5, 6, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.featuresGroup = QtWidgets.QGroupBox(self.widget_2)
        self.featuresGroup.setObjectName("featuresGroup")
        self.feature_grid = QtWidgets.QGridLayout(self.featuresGroup)
        self.feature_grid.setContentsMargins(5, 5, 5, 5)
        self.feature_grid.setObjectName("feature_grid")
        self.gridLayout_2.addWidget(self.featuresGroup, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(FeatureSelectionWidget)
        self.method.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(FeatureSelectionWidget)

    def retranslateUi(self, FeatureSelectionWidget):
        _translate = QtCore.QCoreApplication.translate
        FeatureSelectionWidget.setWindowTitle(_translate("FeatureSelectionWidget", "Form"))
        self.method_box.setItemText(0, _translate("FeatureSelectionWidget", "Evaluación visual"))
        self.method_box.setItemText(1, _translate("FeatureSelectionWidget", "Relación entre variables"))
        self.method_box.setItemText(2, _translate("FeatureSelectionWidget", "Análisis de componentes principales"))
        self.label.setText(_translate("FeatureSelectionWidget", "Herramientas para la toma de decisiones"))
        self.featuresGroup.setTitle(_translate("FeatureSelectionWidget", "Selección de características"))
