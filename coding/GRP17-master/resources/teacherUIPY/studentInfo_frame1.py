# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/derrickyu/Desktop/GRP17-master/resources/UI_resources/studentInfo_frame1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.tableView = QtWidgets.QTableView(Frame)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.frameName_TBS = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frameName_TBS.setFont(font)
        self.frameName_TBS.setObjectName("frameName_TBS")
        self.gridLayout.addWidget(self.frameName_TBS, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
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
        self.comboBox_3 = QtWidgets.QComboBox(Frame)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(Frame)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_4)
        self.comboBox_5 = QtWidgets.QComboBox(Frame)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_5)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.listView = QtWidgets.QListView(Frame)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 3, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.frameName_TBS.setText(_translate("Frame", "Search Result:"))
        self.comboBox.setItemText(0, _translate("Frame", "Module Name"))
        self.comboBox_2.setItemText(0, _translate("Frame", "Session Type"))
        self.comboBox_2.setItemText(1, _translate("Frame", "Lecture"))
        self.comboBox_2.setItemText(2, _translate("Frame", "Tutorial"))
        self.comboBox_2.setItemText(3, _translate("Frame", "Lab/Seminar"))
        self.comboBox_3.setItemText(0, _translate("Frame", "Month"))
        self.comboBox_4.setItemText(0, _translate("Frame", "Day"))
        self.comboBox_5.setItemText(0, _translate("Frame", "Absent"))
        self.comboBox_5.setItemText(1, _translate("Frame", "Attended"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
