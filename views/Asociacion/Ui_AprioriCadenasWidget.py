# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/Asociacion/apriori_cadenas.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AprioriCadenasWidget(object):
    def setupUi(self, AprioriCadenasWidget):
        AprioriCadenasWidget.setObjectName("AprioriCadenasWidget")
        AprioriCadenasWidget.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(AprioriCadenasWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.reglas = QtWidgets.QListWidget(AprioriCadenasWidget)
        self.reglas.setObjectName("reglas")
        self.gridLayout.addWidget(self.reglas, 0, 0, 1, 1)

        self.retranslateUi(AprioriCadenasWidget)
        QtCore.QMetaObject.connectSlotsByName(AprioriCadenasWidget)

    def retranslateUi(self, AprioriCadenasWidget):
        _translate = QtCore.QCoreApplication.translate
        AprioriCadenasWidget.setWindowTitle(_translate("AprioriCadenasWidget", "Form"))
