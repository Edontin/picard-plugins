# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/fix_metadata_encoding_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FixMetadataEncodingDialog(object):
    def setupUi(self, FixMetadataEncodingDialog):
        FixMetadataEncodingDialog.setObjectName("FixMetadataEncodingDialog")
        FixMetadataEncodingDialog.resize(400, 423)
        self.gridLayout = QtWidgets.QGridLayout(FixMetadataEncodingDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(FixMetadataEncodingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(374, 72))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.appliedEncodingLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.appliedEncodingLineEdit.setObjectName("appliedEncodingLineEdit")
        self.verticalLayout_2.addWidget(self.appliedEncodingLineEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(FixMetadataEncodingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.metadataFieldsTreeView = QtWidgets.QTreeWidget(self.groupBox_2)
        self.metadataFieldsTreeView.setObjectName("metadataFieldsTreeView")
        self.gridLayout_3.addWidget(self.metadataFieldsTreeView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(FixMetadataEncodingDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(FixMetadataEncodingDialog)
        self.buttonBox.accepted.connect(FixMetadataEncodingDialog.accept)
        self.buttonBox.rejected.connect(FixMetadataEncodingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FixMetadataEncodingDialog)

    def retranslateUi(self, FixMetadataEncodingDialog):
        _translate = QtCore.QCoreApplication.translate
        FixMetadataEncodingDialog.setWindowTitle(_translate("FixMetadataEncodingDialog", "Dialog"))
        self.groupBox.setTitle(_translate("FixMetadataEncodingDialog", "Encoding configuration"))
        self.label_2.setText(_translate("FixMetadataEncodingDialog", "Actual encoding:"))
        self.groupBox_2.setTitle(_translate("FixMetadataEncodingDialog", "Metadata fields"))
        self.metadataFieldsTreeView.headerItem().setText(0, _translate("FixMetadataEncodingDialog", "Field Name"))

