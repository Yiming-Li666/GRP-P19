# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentInfo_frame1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(690, 520)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(40, 30, 30, 40)
        self.gridLayout.setObjectName("gridLayout")
        self.attendance_listView = QtWidgets.QListView(Frame)
        self.attendance_listView.setObjectName("attendance_listView")
        self.gridLayout.addWidget(self.attendance_listView, 3, 0, 1, 1)
        self.summary_textBrowser = QtWidgets.QTextBrowser(Frame)
        self.summary_textBrowser.setObjectName("summary_textBrowser")
        self.gridLayout.addWidget(self.summary_textBrowser, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(Frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(Frame)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(Frame)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_3.addWidget(self.dateEdit_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.comboBox_5 = QtWidgets.QComboBox(Frame)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_5)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.frameName_TBS = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frameName_TBS.setFont(font)
        self.frameName_TBS.setObjectName("frameName_TBS")
        self.gridLayout.addWidget(self.frameName_TBS, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.comboBox.setItemText(0, _translate("Frame", "Module Name"))
        self.comboBox_2.setItemText(0, _translate("Frame", "Session Type"))
        self.comboBox_2.setItemText(1, _translate("Frame", "Lecture"))
        self.comboBox_2.setItemText(2, _translate("Frame", "Tutorial"))
        self.comboBox_2.setItemText(3, _translate("Frame", "Lab/Seminar"))
        self.label.setText(_translate("Frame", "From:"))
        self.label_2.setText(_translate("Frame", "To:"))
        self.comboBox_5.setItemText(0, _translate("Frame", "Absent"))
        self.comboBox_5.setItemText(1, _translate("Frame", "Attended"))
        self.frameName_TBS.setText(_translate("Frame", "Search Result:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())