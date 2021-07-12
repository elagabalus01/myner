# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/Asociacion/apriori.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AprioriWidget(object):
    def setupUi(self, AprioriWidget):
        AprioriWidget.setObjectName("AprioriWidget")
        AprioriWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(AprioriWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_gen_rules = QtWidgets.QPushButton(AprioriWidget)
        self.btn_gen_rules.setObjectName("btn_gen_rules")
        self.gridLayout.addWidget(self.btn_gen_rules, 0, 2, 1, 1)
        self.feature2_box = QtWidgets.QComboBox(AprioriWidget)
        self.feature2_box.setObjectName("feature2_box")
        self.gridLayout.addWidget(self.feature2_box, 0, 1, 1, 1)
        self.feature1_box = QtWidgets.QComboBox(AprioriWidget)
        self.feature1_box.setObjectName("feature1_box")
        self.gridLayout.addWidget(self.feature1_box, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(AprioriWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)

        self.retranslateUi(AprioriWidget)
        QtCore.QMetaObject.connectSlotsByName(AprioriWidget)

    def retranslateUi(self, AprioriWidget):
        _translate = QtCore.QCoreApplication.translate
        AprioriWidget.setWindowTitle(_translate("AprioriWidget", "Form"))
        self.btn_gen_rules.setText(_translate("AprioriWidget", "Buscar"))
