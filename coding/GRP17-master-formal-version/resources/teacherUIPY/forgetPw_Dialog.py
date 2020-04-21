# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgetPw_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class forgetPw_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.title_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tele_label = QtWidgets.QLabel(Dialog)
        self.tele_label.setObjectName("tele_label")
        self.horizontalLayout.addWidget(self.tele_label)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.emial_label = QtWidgets.QLabel(Dialog)
        self.emial_label.setObjectName("emial_label")
        self.horizontalLayout_2.addWidget(self.emial_label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.tele_label_2 = QtWidgets.QLabel(Dialog)
        self.tele_label_2.setObjectName("tele_label_2")
        self.horizontalLayout_3.addWidget(self.tele_label_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "Please contact the administrator!"))
        self.label.setText(_translate("Dialog", "Tele:"))
        self.tele_label.setText(_translate("Dialog", "+86 574 88180009"))
        self.emial_label.setText(_translate("Dialog", "Email:"))
        self.label_2.setText(_translate("Dialog", "itservicedesk@Nottingham.edu.cn"))
        self.label_3.setText(_translate("Dialog", "Wechat:"))
        self.tele_label_2.setText(_translate("Dialog", "unncit"))
