# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/derrickyu/Desktop/GRP17-master/resources/UI_resources/searchStudent_frame1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(788, 598)
        self.verticalLayoutWidget = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 150, 641, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(Frame)
        self.comboBox.setGeometry(QtCore.QRect(46, 101, 90, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frameName_TBS = QtWidgets.QLabel(Frame)
        self.frameName_TBS.setGeometry(QtCore.QRect(41, 51, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.frameName_TBS.setFont(font)
        self.frameName_TBS.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frameName_TBS.setObjectName("frameName_TBS")
        self.toolButton_4 = QtWidgets.QToolButton(Frame)
        self.toolButton_4.setGeometry(QtCore.QRect(160, 100, 25, 25))
        self.toolButton_4.setStyleSheet("border-image:url(:/all/images/printIcon.png)")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.comboBox.setItemText(0, _translate("Frame", "Sort"))
        self.comboBox.setItemText(1, _translate("Frame", "ID"))
        self.comboBox.setItemText(2, _translate("Frame", "Name"))
        self.frameName_TBS.setText(_translate("Frame", "Student Name"))
import resources.images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
