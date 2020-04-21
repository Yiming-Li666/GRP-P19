# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modulePrint_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 419)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 350, 591, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 200, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 240, 284, 74))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 0, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 1, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 0, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 80, 269, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget2)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget2)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout_2.addWidget(self.dateEdit_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))
        self.pushButton.setText(_translate("Dialog", "Print"))
        self.label.setText(_translate("Dialog", "Record Category:"))
        self.label_2.setText(_translate("Dialog", "Record Timeval:"))
        self.checkBox_5.setText(_translate("Dialog", "Lecture"))
        self.checkBox_8.setText(_translate("Dialog", "Tutorial"))
        self.checkBox_7.setText(_translate("Dialog", "Lab/Seminar"))
        self.checkBox_6.setText(_translate("Dialog", "All"))
        self.label_3.setText(_translate("Dialog", "From"))
        self.label_4.setText(_translate("Dialog", "To"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())