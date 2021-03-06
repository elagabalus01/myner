# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/kmeans/clusters.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ClustersWidget(object):
    def setupUi(self, ClustersWidget):
        ClustersWidget.setObjectName("ClustersWidget")
        ClustersWidget.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(ClustersWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(ClustersWidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.clusters_graphics = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.clusters_graphics.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.clusters_graphics.setContentsMargins(0, 0, 0, 0)
        self.clusters_graphics.setObjectName("clusters_graphics")
        self.scroll_clusters = QtWidgets.QScrollArea(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_clusters.sizePolicy().hasHeightForWidth())
        self.scroll_clusters.setSizePolicy(sizePolicy)
        self.scroll_clusters.setWidgetResizable(True)
        self.scroll_clusters.setObjectName("scroll_clusters")
        self.scroll_grid = QtWidgets.QWidget()
        self.scroll_grid.setGeometry(QtCore.QRect(0, 0, 636, 281))
        self.scroll_grid.setObjectName("scroll_grid")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scroll_grid)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.num_clusters_in = QtWidgets.QSpinBox(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_clusters_in.sizePolicy().hasHeightForWidth())
        self.num_clusters_in.setSizePolicy(sizePolicy)
        self.num_clusters_in.setMinimum(2)
        self.num_clusters_in.setMaximum(12)
        self.num_clusters_in.setObjectName("num_clusters_in")
        self.gridLayout_2.addWidget(self.num_clusters_in, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.feature_z_box = QtWidgets.QComboBox(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_z_box.sizePolicy().hasHeightForWidth())
        self.feature_z_box.setSizePolicy(sizePolicy)
        self.feature_z_box.setObjectName("feature_z_box")
        self.gridLayout_2.addWidget(self.feature_z_box, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.feature_x_box = QtWidgets.QComboBox(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_x_box.sizePolicy().hasHeightForWidth())
        self.feature_x_box.setSizePolicy(sizePolicy)
        self.feature_x_box.setObjectName("feature_x_box")
        self.gridLayout_2.addWidget(self.feature_x_box, 2, 0, 1, 1)
        self.feature_y_box = QtWidgets.QComboBox(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_y_box.sizePolicy().hasHeightForWidth())
        self.feature_y_box.setSizePolicy(sizePolicy)
        self.feature_y_box.setObjectName("feature_y_box")
        self.gridLayout_2.addWidget(self.feature_y_box, 2, 1, 1, 1)
        self.btn_elbow = QtWidgets.QCommandLinkButton(self.scroll_grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_elbow.sizePolicy().hasHeightForWidth())
        self.btn_elbow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/arrow_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_elbow.setIcon(icon)
        self.btn_elbow.setObjectName("btn_elbow")
        self.gridLayout_2.addWidget(self.btn_elbow, 4, 0, 1, 1)
        self.graph_grid = QtWidgets.QGridLayout()
        self.graph_grid.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.graph_grid.setContentsMargins(5, 5, 5, 5)
        self.graph_grid.setObjectName("graph_grid")
        self.gridLayout_2.addLayout(self.graph_grid, 3, 0, 1, 3)
        self.scroll_clusters.setWidget(self.scroll_grid)
        self.clusters_graphics.addWidget(self.scroll_clusters, 2, 0, 1, 2)
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.clusters_desc = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.clusters_desc.setContentsMargins(5, 5, 5, 5)
        self.clusters_desc.setObjectName("clusters_desc")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.clusters_desc.addWidget(self.label_5, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.centroides_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centroides_table.sizePolicy().hasHeightForWidth())
        self.centroides_table.setSizePolicy(sizePolicy)
        self.centroides_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.centroides_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.centroides_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.centroides_table.setAutoScrollMargin(0)
        self.centroides_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.centroides_table.setTabKeyNavigation(False)
        self.centroides_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.centroides_table.setTextElideMode(QtCore.Qt.ElideNone)
        self.centroides_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.centroides_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.centroides_table.setObjectName("centroides_table")
        self.centroides_table.setColumnCount(0)
        self.centroides_table.setRowCount(0)
        self.clusters_desc.addWidget(self.centroides_table, 1, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)

        self.retranslateUi(ClustersWidget)
        QtCore.QMetaObject.connectSlotsByName(ClustersWidget)

    def retranslateUi(self, ClustersWidget):
        _translate = QtCore.QCoreApplication.translate
        ClustersWidget.setWindowTitle(_translate("ClustersWidget", "Form"))
        self.label_2.setText(_translate("ClustersWidget", "Caracter??stica en Y"))
        self.label_4.setText(_translate("ClustersWidget", "N??mero de clusters"))
        self.label.setText(_translate("ClustersWidget", "Caracter??stica en X"))
        self.label_3.setText(_translate("ClustersWidget", "Caracter??stica en Z"))
        self.btn_elbow.setText(_translate("ClustersWidget", "Regresar a elbow method"))
        self.label_5.setText(_translate("ClustersWidget", "Descripci??n de los centroides"))
        self.centroides_table.setSortingEnabled(True)
from res import res_rc
