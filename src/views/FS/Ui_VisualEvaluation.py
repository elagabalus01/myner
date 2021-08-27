# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/FS/VisualEvaluation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VisualEvaluation(object):
    def setupUi(self, VisualEvaluation):
        VisualEvaluation.setObjectName("VisualEvaluation")
        VisualEvaluation.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(VisualEvaluation)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(VisualEvaluation)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 638, 478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scroll_grid.setContentsMargins(5, 5, 5, 5)
        self.scroll_grid.setObjectName("scroll_grid")
        self.eje_x_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.eje_x_box.setObjectName("eje_x_box")
        self.scroll_grid.addWidget(self.eje_x_box, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.scroll_grid.addWidget(self.label, 0, 0, 1, 1)
        self.eje_y_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.eje_y_box.setObjectName("eje_y_box")
        self.scroll_grid.addWidget(self.eje_y_box, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.scroll_grid.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.scroll_grid.addWidget(self.label_3, 0, 4, 1, 1)
        self.dependiente_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.dependiente_box.setObjectName("dependiente_box")
        self.scroll_grid.addWidget(self.dependiente_box, 0, 5, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(VisualEvaluation)
        QtCore.QMetaObject.connectSlotsByName(VisualEvaluation)

    def retranslateUi(self, VisualEvaluation):
        _translate = QtCore.QCoreApplication.translate
        VisualEvaluation.setWindowTitle(_translate("VisualEvaluation", "Form"))
        self.label.setText(_translate("VisualEvaluation", "Eje x"))
        self.label_2.setText(_translate("VisualEvaluation", "Eje y"))
        self.label_3.setText(_translate("VisualEvaluation", "Variable dependiente"))
