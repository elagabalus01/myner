# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/FS/Componentes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCA(object):
    def setupUi(self, PCA):
        PCA.setObjectName("PCA")
        PCA.resize(794, 434)
        self.gridLayout = QtWidgets.QGridLayout(PCA)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(PCA)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 792, 432))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.features_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.features_box.setObjectName("features_box")
        self.features_box.addItem("")
        self.gridLayout_2.addWidget(self.features_box, 0, 1, 1, 1)
        self.btn_calcular = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calcular.sizePolicy().hasHeightForWidth())
        self.btn_calcular.setSizePolicy(sizePolicy)
        self.btn_calcular.setObjectName("btn_calcular")
        self.gridLayout_2.addWidget(self.btn_calcular, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cargas_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cargas_table.sizePolicy().hasHeightForWidth())
        self.cargas_table.setSizePolicy(sizePolicy)
        self.cargas_table.setMinimumSize(QtCore.QSize(256, 0))
        self.cargas_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.cargas_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.cargas_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.cargas_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cargas_table.setTabKeyNavigation(False)
        self.cargas_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.cargas_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cargas_table.setTextElideMode(QtCore.Qt.ElideNone)
        self.cargas_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.cargas_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.cargas_table.setObjectName("cargas_table")
        self.cargas_table.setColumnCount(0)
        self.cargas_table.setRowCount(0)
        self.cargas_table.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout.addWidget(self.cargas_table, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(PCA)
        QtCore.QMetaObject.connectSlotsByName(PCA)

    def retranslateUi(self, PCA):
        _translate = QtCore.QCoreApplication.translate
        PCA.setWindowTitle(_translate("PCA", "Form"))
        self.label.setText(_translate("PCA", "Variable dependiente"))
        self.features_box.setItemText(0, _translate("PCA", "Ninguna"))
        self.btn_calcular.setText(_translate("PCA", "Calcular"))
