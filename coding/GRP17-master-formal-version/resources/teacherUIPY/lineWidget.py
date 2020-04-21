# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lineWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(872, 300)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.lineDispaly_widget = QtWidgets.QWidget(Form)
        self.lineDispaly_widget.setGeometry(QtCore.QRect(90, 110, 621, 50))
        self.lineDispaly_widget.setObjectName("lineDispaly_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.lineDispaly_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.lineDispaly_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.toolButton_8 = QtWidgets.QToolButton(self.lineDispaly_widget)
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout_6.addWidget(self.toolButton_8)
        self.toolButton_9 = QtWidgets.QToolButton(self.lineDispaly_widget)
        self.toolButton_9.setObjectName("toolButton_9")
        self.horizontalLayout_6.addWidget(self.toolButton_9)
        self.toolButton_10 = QtWidgets.QToolButton(self.lineDispaly_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_10.sizePolicy().hasHeightForWidth())
        self.toolButton_10.setSizePolicy(sizePolicy)
        self.toolButton_10.setMinimumSize(QtCore.QSize(30, 20))
        self.toolButton_10.setMaximumSize(QtCore.QSize(31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton_10.setFont(font)
        self.toolButton_10.setObjectName("toolButton_10")
        self.horizontalLayout_6.addWidget(self.toolButton_10)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.retranslateUi(Form)
        self.toolButton_8.clicked.connect(Form.modifyItem)
        self.toolButton_9.clicked.connect(Form.deleteItem)
        self.toolButton_10.clicked.connect(Form.starItem)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton_8.setText(_translate("Form", "M"))
        self.toolButton_9.setText(_translate("Form", "-"))
        self.toolButton_10.setText(_translate("Form", "⭐"))
