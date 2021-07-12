# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/EDA/eda.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EDA(object):
    def setupUi(self, EDA):
        EDA.setObjectName("EDA")
        EDA.resize(896, 492)
        self.verticalLayout = QtWidgets.QVBoxLayout(EDA)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scroll_analisis = QtWidgets.QScrollArea(EDA)
        self.scroll_analisis.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_analisis.sizePolicy().hasHeightForWidth())
        self.scroll_analisis.setSizePolicy(sizePolicy)
        self.scroll_analisis.setMaximumSize(QtCore.QSize(10000, 10000))
        self.scroll_analisis.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_analisis.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll_analisis.setWidgetResizable(True)
        self.scroll_analisis.setAlignment(QtCore.Qt.AlignCenter)
        self.scroll_analisis.setObjectName("scroll_analisis")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 877, 490))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.preview_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_label.sizePolicy().hasHeightForWidth())
        self.preview_label.setSizePolicy(sizePolicy)
        self.preview_label.setObjectName("preview_label")
        self.gridLayout_3.addWidget(self.preview_label, 0, 0, 1, 1)
        self.graficas = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graficas.sizePolicy().hasHeightForWidth())
        self.graficas.setSizePolicy(sizePolicy)
        self.graficas.setObjectName("graficas")
        self.graph_layout = QtWidgets.QGridLayout(self.graficas)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.feature_label = QtWidgets.QLabel(self.graficas)
        self.feature_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.feature_label.setObjectName("feature_label")
        self.graph_layout.addWidget(self.feature_label, 0, 0, 1, 1)
        self.features_box = QtWidgets.QComboBox(self.graficas)
        self.features_box.setObjectName("features_box")
        self.graph_layout.addWidget(self.features_box, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.graficas, 6, 0, 1, 2)
        self.estruct_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estruct_label.sizePolicy().hasHeightForWidth())
        self.estruct_label.setSizePolicy(sizePolicy)
        self.estruct_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.estruct_label.setObjectName("estruct_label")
        self.gridLayout_3.addWidget(self.estruct_label, 4, 0, 1, 1)
        self.estruct_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estruct_table.sizePolicy().hasHeightForWidth())
        self.estruct_table.setSizePolicy(sizePolicy)
        self.estruct_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.estruct_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.estruct_table.setTabKeyNavigation(False)
        self.estruct_table.setProperty("showDropIndicator", False)
        self.estruct_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.estruct_table.setObjectName("estruct_table")
        self.estruct_table.setColumnCount(0)
        self.estruct_table.setRowCount(0)
        self.estruct_table.verticalHeader().setHighlightSections(False)
        self.gridLayout_3.addWidget(self.estruct_table, 5, 0, 1, 1)
        self.faltantes_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faltantes_label.sizePolicy().hasHeightForWidth())
        self.faltantes_label.setSizePolicy(sizePolicy)
        self.faltantes_label.setObjectName("faltantes_label")
        self.gridLayout_3.addWidget(self.faltantes_label, 4, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.preview_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.preview_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_table.sizePolicy().hasHeightForWidth())
        self.preview_table.setSizePolicy(sizePolicy)
        self.preview_table.setMinimumSize(QtCore.QSize(256, 0))
        self.preview_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.preview_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.preview_table.setAutoScroll(False)
        self.preview_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.preview_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.preview_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.preview_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.preview_table.setObjectName("preview_table")
        self.preview_table.setColumnCount(0)
        self.preview_table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.preview_table, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 2)
        self.missed_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.missed_table.sizePolicy().hasHeightForWidth())
        self.missed_table.setSizePolicy(sizePolicy)
        self.missed_table.setObjectName("missed_table")
        self.missed_table.setColumnCount(0)
        self.missed_table.setRowCount(0)
        self.gridLayout_3.addWidget(self.missed_table, 5, 1, 1, 1)
        self.object_plot = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.object_plot.setObjectName("object_plot")
        self.object_plot_grid = QtWidgets.QGridLayout(self.object_plot)
        self.object_plot_grid.setContentsMargins(9, 9, 9, 9)
        self.object_plot_grid.setObjectName("object_plot_grid")
        self.label = QtWidgets.QLabel(self.object_plot)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.object_plot_grid.addWidget(self.label, 0, 0, 1, 1)
        self.object_feature_box = QtWidgets.QComboBox(self.object_plot)
        self.object_feature_box.setObjectName("object_feature_box")
        self.object_plot_grid.addWidget(self.object_feature_box, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.object_plot, 7, 0, 1, 2)
        self.scroll_analisis.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scroll_analisis)

        self.retranslateUi(EDA)
        QtCore.QMetaObject.connectSlotsByName(EDA)
        EDA.setTabOrder(self.scroll_analisis, self.estruct_table)
        EDA.setTabOrder(self.estruct_table, self.missed_table)

    def retranslateUi(self, EDA):
        _translate = QtCore.QCoreApplication.translate
        EDA.setWindowTitle(_translate("EDA", "Form"))
        self.preview_label.setText(_translate("EDA", "Preview"))
        self.feature_label.setText(_translate("EDA", "Característica"))
        self.estruct_label.setText(_translate("EDA", "Estructura"))
        self.faltantes_label.setText(_translate("EDA", "Datos faltantes"))
        self.missed_table.setSortingEnabled(True)
        self.label.setText(_translate("EDA", "Característica"))
