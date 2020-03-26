# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upcomingEvents_frame2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class upcomingEvents_frame2(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(394, 556)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.listView = QtWidgets.QListView(Frame)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_3.setText(_translate("Frame", "Upcoming Events"))
