# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/derrickyu/Downloads/GRP17-master/resources/UI_resources/studentRecord_frame1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class studentRecord_frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(582, 479)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(50, 30, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sessionInfo_label = QtWidgets.QLabel(Frame)
        self.sessionInfo_label.setObjectName("sessionInfo_label")
        self.horizontalLayout.addWidget(self.sessionInfo_label)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.studentName_label = QtWidgets.QLabel(Frame)
        self.studentName_label.setObjectName("studentName_label")
        self.horizontalLayout_2.addWidget(self.studentName_label)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.studentId_label = QtWidgets.QLabel(Frame)
        self.studentId_label.setObjectName("studentId_label")
        self.horizontalLayout_3.addWidget(self.studentId_label)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.attdanceState_label = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attdanceState_label.sizePolicy().hasHeightForWidth())
        self.attdanceState_label.setSizePolicy(sizePolicy)
        self.attdanceState_label.setObjectName("attdanceState_label")
        self.horizontalLayout_7.addWidget(self.attdanceState_label)
        self.modifyState_toolButton = QtWidgets.QToolButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyState_toolButton.sizePolicy().hasHeightForWidth())
        self.modifyState_toolButton.setSizePolicy(sizePolicy)
        self.modifyState_toolButton.setMaximumSize(QtCore.QSize(30, 30))
        self.modifyState_toolButton.setObjectName("modifyState_toolButton")
        self.horizontalLayout_7.addWidget(self.modifyState_toolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.signInTime_label = QtWidgets.QLabel(Frame)
        self.signInTime_label.setObjectName("signInTime_label")
        self.horizontalLayout_5.addWidget(self.signInTime_label)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.signOutTime_label = QtWidgets.QLabel(Frame)
        self.signOutTime_label.setObjectName("signOutTime_label")
        self.horizontalLayout_6.addWidget(self.signOutTime_label)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        self.modifyState_toolButton.clicked.connect(self.modifyState)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Session Information:"))
        self.sessionInfo_label.setText(_translate("Frame", "TextLabel"))
        self.label_2.setText(_translate("Frame", "Student Name:"))
        self.studentName_label.setText(_translate("Frame", "TextLabel"))
        self.label_4.setText(_translate("Frame", "Student ID:"))
        self.studentId_label.setText(_translate("Frame", "TextLabel"))
        self.label_3.setText(_translate("Frame", "Attendance State:"))
        self.attdanceState_label.setText(_translate("Frame", "TextLabel"))
        self.modifyState_toolButton.setText(_translate("Frame", "M"))
        self.label_5.setText(_translate("Frame", "Sign-in Time:"))
        self.signInTime_label.setText(_translate("Frame", "TextLabel"))
        self.label_6.setText(_translate("Frame", "Sign-out Time:"))
        self.signOutTime_label.setText(_translate("Frame", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())