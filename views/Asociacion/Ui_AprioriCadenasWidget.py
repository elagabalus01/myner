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
        self.btn_gen_reglas = QtWidgets.QPushButton(AprioriCadenasWidget)
        self.btn_gen_reglas.setObjectName("btn_gen_reglas")
        self.gridLayout.addWidget(self.btn_gen_reglas, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(AprioriCadenasWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.soporte_in = QtWidgets.QDoubleSpinBox(AprioriCadenasWidget)
        self.soporte_in.setDecimals(4)
        self.soporte_in.setMinimum(0.01)
        self.soporte_in.setMaximum(1.0)
        self.soporte_in.setSingleStep(0.1)
        self.soporte_in.setObjectName("soporte_in")
        self.gridLayout.addWidget(self.soporte_in, 1, 0, 1, 1)
        self.rule_table = QtWidgets.QTableWidget(AprioriCadenasWidget)
        self.rule_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.rule_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rule_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.rule_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.rule_table.setTabKeyNavigation(False)
        self.rule_table.setProperty("showDropIndicator", False)
        self.rule_table.setDragEnabled(False)
        self.rule_table.setDragDropOverwriteMode(False)
        self.rule_table.setAlternatingRowColors(False)
        self.rule_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.rule_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.rule_table.setRowCount(0)
        self.rule_table.setColumnCount(4)
        self.rule_table.setObjectName("rule_table")
        self.rule_table.horizontalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.rule_table, 2, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(AprioriCadenasWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.confianza_in = QtWidgets.QDoubleSpinBox(AprioriCadenasWidget)
        self.confianza_in.setDecimals(4)
        self.confianza_in.setMinimum(0.01)
        self.confianza_in.setMaximum(1.0)
        self.confianza_in.setSingleStep(0.1)
        self.confianza_in.setObjectName("confianza_in")
        self.gridLayout.addWidget(self.confianza_in, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(AprioriCadenasWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lift_in = QtWidgets.QDoubleSpinBox(AprioriCadenasWidget)
        self.lift_in.setDecimals(4)
        self.lift_in.setMinimum(1.0)
        self.lift_in.setMaximum(10.0)
        self.lift_in.setSingleStep(0.1)
        self.lift_in.setObjectName("lift_in")
        self.gridLayout.addWidget(self.lift_in, 1, 2, 1, 1)

        self.retranslateUi(AprioriCadenasWidget)
        QtCore.QMetaObject.connectSlotsByName(AprioriCadenasWidget)

    def retranslateUi(self, AprioriCadenasWidget):
        _translate = QtCore.QCoreApplication.translate
        AprioriCadenasWidget.setWindowTitle(_translate("AprioriCadenasWidget", "Form"))
        self.btn_gen_reglas.setText(_translate("AprioriCadenasWidget", "Buscar"))
        self.label.setText(_translate("AprioriCadenasWidget", "Lift"))
        self.rule_table.setSortingEnabled(True)
        self.label_2.setText(_translate("AprioriCadenasWidget", "Confianza"))
        self.label_3.setText(_translate("AprioriCadenasWidget", "Soporte"))
