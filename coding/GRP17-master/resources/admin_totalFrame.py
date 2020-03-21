# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_totalFrame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1120, 573)
        self.gridLayout_3 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_3.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 22)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navigator_label = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigator_label.sizePolicy().hasHeightForWidth())
        self.navigator_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.navigator_label.setFont(font)
        self.navigator_label.setAlignment(QtCore.Qt.AlignCenter)
        self.navigator_label.setObjectName("navigator_label")
        self.verticalLayout.addWidget(self.navigator_label)
        self.account_pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_pushButton.sizePolicy().hasHeightForWidth())
        self.account_pushButton.setSizePolicy(sizePolicy)
        self.account_pushButton.setObjectName("account_pushButton")
        self.verticalLayout.addWidget(self.account_pushButton)
        self.student_pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_pushButton.sizePolicy().hasHeightForWidth())
        self.student_pushButton.setSizePolicy(sizePolicy)
        self.student_pushButton.setObjectName("student_pushButton")
        self.verticalLayout.addWidget(self.student_pushButton)
        self.teacher_pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teacher_pushButton.sizePolicy().hasHeightForWidth())
        self.teacher_pushButton.setSizePolicy(sizePolicy)
        self.teacher_pushButton.setObjectName("teacher_pushButton")
        self.verticalLayout.addWidget(self.teacher_pushButton)
        self.module_pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.module_pushButton.sizePolicy().hasHeightForWidth())
        self.module_pushButton.setSizePolicy(sizePolicy)
        self.module_pushButton.setObjectName("module_pushButton")
        self.verticalLayout.addWidget(self.module_pushButton)
        self.attendance_pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attendance_pushButton.sizePolicy().hasHeightForWidth())
        self.attendance_pushButton.setSizePolicy(sizePolicy)
        self.attendance_pushButton.setObjectName("attendance_pushButton")
        self.verticalLayout.addWidget(self.attendance_pushButton)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(Frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.page_5)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AC_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AC_label.setFont(font)
        self.AC_label.setObjectName("AC_label")
        self.verticalLayout_2.addWidget(self.AC_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ACcomboBox1 = QtWidgets.QComboBox(self.frame_5)
        self.ACcomboBox1.setObjectName("ACcomboBox1")
        self.ACcomboBox1.addItem("")
        self.horizontalLayout.addWidget(self.ACcomboBox1)
        self.ACcomboBox2 = QtWidgets.QComboBox(self.frame_5)
        self.ACcomboBox2.setObjectName("ACcomboBox2")
        self.ACcomboBox2.addItem("")
        self.horizontalLayout.addWidget(self.ACcomboBox2)
        self.ACcomboBox3 = QtWidgets.QComboBox(self.frame_5)
        self.ACcomboBox3.setObjectName("ACcomboBox3")
        self.ACcomboBox3.addItem("")
        self.horizontalLayout.addWidget(self.ACcomboBox3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ACsearch_lineEdit = QtWidgets.QLineEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ACsearch_lineEdit.sizePolicy().hasHeightForWidth())
        self.ACsearch_lineEdit.setSizePolicy(sizePolicy)
        self.ACsearch_lineEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.ACsearch_lineEdit.setObjectName("ACsearch_lineEdit")
        self.horizontalLayout_10.addWidget(self.ACsearch_lineEdit)
        self.ACsearch_toolButton = QtWidgets.QToolButton(self.frame_5)
        self.ACsearch_toolButton.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.ACsearch_toolButton.setText("")
        self.ACsearch_toolButton.setObjectName("ACsearch_toolButton")
        self.horizontalLayout_10.addWidget(self.ACsearch_toolButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_10)
        self.ACmodify_toolButton = QtWidgets.QToolButton(self.frame_5)
        self.ACmodify_toolButton.setObjectName("ACmodify_toolButton")
        self.horizontalLayout.addWidget(self.ACmodify_toolButton)
        self.ACdelete_toolButton = QtWidgets.QToolButton(self.frame_5)
        self.ACdelete_toolButton.setObjectName("ACdelete_toolButton")
        self.horizontalLayout.addWidget(self.ACdelete_toolButton)
        self.ACadd_toolButton = QtWidgets.QToolButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ACadd_toolButton.sizePolicy().hasHeightForWidth())
        self.ACadd_toolButton.setSizePolicy(sizePolicy)
        self.ACadd_toolButton.setMinimumSize(QtCore.QSize(30, 20))
        self.ACadd_toolButton.setMaximumSize(QtCore.QSize(31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ACadd_toolButton.setFont(font)
        self.ACadd_toolButton.setObjectName("ACadd_toolButton")
        self.horizontalLayout.addWidget(self.ACadd_toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.frame_5)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 15)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.page)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Stu_label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Stu_label.setFont(font)
        self.Stu_label.setObjectName("Stu_label")
        self.verticalLayout_3.addWidget(self.Stu_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Stu_comboBox1 = QtWidgets.QComboBox(self.frame_6)
        self.Stu_comboBox1.setObjectName("Stu_comboBox1")
        self.Stu_comboBox1.addItem("")
        self.horizontalLayout_2.addWidget(self.Stu_comboBox1)
        self.Stu_comboBox2 = QtWidgets.QComboBox(self.frame_6)
        self.Stu_comboBox2.setObjectName("Stu_comboBox2")
        self.Stu_comboBox2.addItem("")
        self.horizontalLayout_2.addWidget(self.Stu_comboBox2)
        self.Stu_comboBox3 = QtWidgets.QComboBox(self.frame_6)
        self.Stu_comboBox3.setObjectName("Stu_comboBox3")
        self.Stu_comboBox3.addItem("")
        self.horizontalLayout_2.addWidget(self.Stu_comboBox3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Stu_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stu_lineEdit.sizePolicy().hasHeightForWidth())
        self.Stu_lineEdit.setSizePolicy(sizePolicy)
        self.Stu_lineEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.Stu_lineEdit.setObjectName("Stu_lineEdit")
        self.horizontalLayout_11.addWidget(self.Stu_lineEdit)
        self.Stu_toolButton = QtWidgets.QToolButton(self.frame_6)
        self.Stu_toolButton.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.Stu_toolButton.setText("")
        self.Stu_toolButton.setObjectName("Stu_toolButton")
        self.horizontalLayout_11.addWidget(self.Stu_toolButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_11)
        self.STUModify_toolButton = QtWidgets.QToolButton(self.frame_6)
        self.STUModify_toolButton.setObjectName("STUModify_toolButton")
        self.horizontalLayout_2.addWidget(self.STUModify_toolButton)
        self.STUdelete_toolButton = QtWidgets.QToolButton(self.frame_6)
        self.STUdelete_toolButton.setObjectName("STUdelete_toolButton")
        self.horizontalLayout_2.addWidget(self.STUdelete_toolButton)
        self.STUadd_toolButton = QtWidgets.QToolButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STUadd_toolButton.sizePolicy().hasHeightForWidth())
        self.STUadd_toolButton.setSizePolicy(sizePolicy)
        self.STUadd_toolButton.setMinimumSize(QtCore.QSize(30, 20))
        self.STUadd_toolButton.setMaximumSize(QtCore.QSize(31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.STUadd_toolButton.setFont(font)
        self.STUadd_toolButton.setObjectName("STUadd_toolButton")
        self.horizontalLayout_2.addWidget(self.STUadd_toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tableView_2 = QtWidgets.QTableView(self.frame_6)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_3.addWidget(self.tableView_2)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 15)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.teacher_label = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teacher_label.setFont(font)
        self.teacher_label.setObjectName("teacher_label")
        self.verticalLayout_4.addWidget(self.teacher_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Tea_comboBox1 = QtWidgets.QComboBox(self.frame_7)
        self.Tea_comboBox1.setObjectName("Tea_comboBox1")
        self.Tea_comboBox1.addItem("")
        self.horizontalLayout_3.addWidget(self.Tea_comboBox1)
        self.Tea_comboBox2 = QtWidgets.QComboBox(self.frame_7)
        self.Tea_comboBox2.setObjectName("Tea_comboBox2")
        self.Tea_comboBox2.addItem("")
        self.horizontalLayout_3.addWidget(self.Tea_comboBox2)
        self.Tea_comboBox3 = QtWidgets.QComboBox(self.frame_7)
        self.Tea_comboBox3.setObjectName("Tea_comboBox3")
        self.Tea_comboBox3.addItem("")
        self.horizontalLayout_3.addWidget(self.Tea_comboBox3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.TEAsearch_lineEdit = QtWidgets.QLineEdit(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TEAsearch_lineEdit.sizePolicy().hasHeightForWidth())
        self.TEAsearch_lineEdit.setSizePolicy(sizePolicy)
        self.TEAsearch_lineEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.TEAsearch_lineEdit.setObjectName("TEAsearch_lineEdit")
        self.horizontalLayout_12.addWidget(self.TEAsearch_lineEdit)
        self.TEAsearch_toolButton = QtWidgets.QToolButton(self.frame_7)
        self.TEAsearch_toolButton.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.TEAsearch_toolButton.setText("")
        self.TEAsearch_toolButton.setObjectName("TEAsearch_toolButton")
        self.horizontalLayout_12.addWidget(self.TEAsearch_toolButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_12)
        self.TEAmodify_toolButton = QtWidgets.QToolButton(self.frame_7)
        self.TEAmodify_toolButton.setObjectName("TEAmodify_toolButton")
        self.horizontalLayout_3.addWidget(self.TEAmodify_toolButton)
        self.TEAdelete_toolButton = QtWidgets.QToolButton(self.frame_7)
        self.TEAdelete_toolButton.setObjectName("TEAdelete_toolButton")
        self.horizontalLayout_3.addWidget(self.TEAdelete_toolButton)
        self.TEAadd_toolButton = QtWidgets.QToolButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TEAadd_toolButton.sizePolicy().hasHeightForWidth())
        self.TEAadd_toolButton.setSizePolicy(sizePolicy)
        self.TEAadd_toolButton.setMinimumSize(QtCore.QSize(30, 20))
        self.TEAadd_toolButton.setMaximumSize(QtCore.QSize(31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TEAadd_toolButton.setFont(font)
        self.TEAadd_toolButton.setObjectName("TEAadd_toolButton")
        self.horizontalLayout_3.addWidget(self.TEAadd_toolButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tableView_3 = QtWidgets.QTableView(self.frame_7)
        self.tableView_3.setObjectName("tableView_3")
        self.verticalLayout_4.addWidget(self.tableView_3)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 15)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.module_label = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.module_label.setFont(font)
        self.module_label.setObjectName("module_label")
        self.verticalLayout_5.addWidget(self.module_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Module_comboBox1 = QtWidgets.QComboBox(self.frame_8)
        self.Module_comboBox1.setObjectName("Module_comboBox1")
        self.Module_comboBox1.addItem("")
        self.horizontalLayout_4.addWidget(self.Module_comboBox1)
        self.Module_comboBox2 = QtWidgets.QComboBox(self.frame_8)
        self.Module_comboBox2.setObjectName("Module_comboBox2")
        self.Module_comboBox2.addItem("")
        self.horizontalLayout_4.addWidget(self.Module_comboBox2)
        self.Module_comboBox3 = QtWidgets.QComboBox(self.frame_8)
        self.Module_comboBox3.setObjectName("Module_comboBox3")
        self.Module_comboBox3.addItem("")
        self.horizontalLayout_4.addWidget(self.Module_comboBox3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.TEAsearch_lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TEAsearch_lineEdit_2.sizePolicy().hasHeightForWidth())
        self.TEAsearch_lineEdit_2.setSizePolicy(sizePolicy)
        self.TEAsearch_lineEdit_2.setMinimumSize(QtCore.QSize(30, 30))
        self.TEAsearch_lineEdit_2.setObjectName("TEAsearch_lineEdit_2")
        self.horizontalLayout_13.addWidget(self.TEAsearch_lineEdit_2)
        self.TEAsearch_toolButton_2 = QtWidgets.QToolButton(self.frame_8)
        self.TEAsearch_toolButton_2.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.TEAsearch_toolButton_2.setText("")
        self.TEAsearch_toolButton_2.setObjectName("TEAsearch_toolButton_2")
        self.horizontalLayout_13.addWidget(self.TEAsearch_toolButton_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_13)
        self.TEAmodify_toolButton_2 = QtWidgets.QToolButton(self.frame_8)
        self.TEAmodify_toolButton_2.setObjectName("TEAmodify_toolButton_2")
        self.horizontalLayout_4.addWidget(self.TEAmodify_toolButton_2)
        self.TEAdelete_toolButton_2 = QtWidgets.QToolButton(self.frame_8)
        self.TEAdelete_toolButton_2.setObjectName("TEAdelete_toolButton_2")
        self.horizontalLayout_4.addWidget(self.TEAdelete_toolButton_2)
        self.TEAadd_toolButton_2 = QtWidgets.QToolButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TEAadd_toolButton_2.sizePolicy().hasHeightForWidth())
        self.TEAadd_toolButton_2.setSizePolicy(sizePolicy)
        self.TEAadd_toolButton_2.setMinimumSize(QtCore.QSize(30, 20))
        self.TEAadd_toolButton_2.setMaximumSize(QtCore.QSize(31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TEAadd_toolButton_2.setFont(font)
        self.TEAadd_toolButton_2.setObjectName("TEAadd_toolButton_2")
        self.horizontalLayout_4.addWidget(self.TEAadd_toolButton_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tableView_4 = QtWidgets.QTableView(self.frame_8)
        self.tableView_4.setObjectName("tableView_4")
        self.verticalLayout_5.addWidget(self.tableView_4)
        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 15)
        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_9 = QtWidgets.QFrame(self.page_4)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.attendence_label = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.attendence_label.setFont(font)
        self.attendence_label.setObjectName("attendence_label")
        self.verticalLayout_6.addWidget(self.attendence_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Att_comboBox1 = QtWidgets.QComboBox(self.frame_9)
        self.Att_comboBox1.setObjectName("Att_comboBox1")
        self.Att_comboBox1.addItem("")
        self.horizontalLayout_5.addWidget(self.Att_comboBox1)
        self.Att_comboBox2 = QtWidgets.QComboBox(self.frame_9)
        self.Att_comboBox2.setObjectName("Att_comboBox2")
        self.Att_comboBox2.addItem("")
        self.horizontalLayout_5.addWidget(self.Att_comboBox2)
        self.Att_comboBox3 = QtWidgets.QComboBox(self.frame_9)
        self.Att_comboBox3.setObjectName("Att_comboBox3")
        self.Att_comboBox3.addItem("")
        self.horizontalLayout_5.addWidget(self.Att_comboBox3)
        self.Att_comboBox4 = QtWidgets.QComboBox(self.frame_9)
        self.Att_comboBox4.setObjectName("Att_comboBox4")
        self.Att_comboBox4.addItem("")
        self.horizontalLayout_5.addWidget(self.Att_comboBox4)
        self.Att_comboBox5 = QtWidgets.QComboBox(self.frame_9)
        self.Att_comboBox5.setObjectName("Att_comboBox5")
        self.Att_comboBox5.addItem("")
        self.horizontalLayout_5.addWidget(self.Att_comboBox5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.att_dateEdit1 = QtWidgets.QDateEdit(self.frame_9)
        self.att_dateEdit1.setObjectName("att_dateEdit1")
        self.horizontalLayout_6.addWidget(self.att_dateEdit1)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.Att_dateEdit2 = QtWidgets.QDateEdit(self.frame_9)
        self.Att_dateEdit2.setObjectName("Att_dateEdit2")
        self.horizontalLayout_7.addWidget(self.Att_dateEdit2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.ATTsearch_lineEdit = QtWidgets.QLineEdit(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ATTsearch_lineEdit.sizePolicy().hasHeightForWidth())
        self.ATTsearch_lineEdit.setSizePolicy(sizePolicy)
        self.ATTsearch_lineEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.ATTsearch_lineEdit.setObjectName("ATTsearch_lineEdit")
        self.horizontalLayout_15.addWidget(self.ATTsearch_lineEdit)
        self.Attsearch_toolButton = QtWidgets.QToolButton(self.frame_9)
        self.Attsearch_toolButton.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.Attsearch_toolButton.setText("")
        self.Attsearch_toolButton.setObjectName("Attsearch_toolButton")
        self.horizontalLayout_15.addWidget(self.Attsearch_toolButton)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_15)
        self.ATTmodify_toolButton = QtWidgets.QToolButton(self.frame_9)
        self.ATTmodify_toolButton.setObjectName("ATTmodify_toolButton")
        self.horizontalLayout_8.addWidget(self.ATTmodify_toolButton)
        self.ATTdelete_toolButton = QtWidgets.QToolButton(self.frame_9)
        self.ATTdelete_toolButton.setObjectName("ATTdelete_toolButton")
        self.horizontalLayout_8.addWidget(self.ATTdelete_toolButton)
        self.ATTadd_toolButton = QtWidgets.QToolButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ATTadd_toolButton.sizePolicy().hasHeightForWidth())
        self.ATTadd_toolButton.setSizePolicy(sizePolicy)
        self.ATTadd_toolButton.setMinimumSize(QtCore.QSize(30, 20))
        self.ATTadd_toolButton.setMaximumSize(QtCore.QSize(31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ATTadd_toolButton.setFont(font)
        self.ATTadd_toolButton.setObjectName("ATTadd_toolButton")
        self.horizontalLayout_8.addWidget(self.ATTadd_toolButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.tableView_5 = QtWidgets.QTableView(self.frame_9)
        self.tableView_5.setObjectName("tableView_5")
        self.verticalLayout_6.addWidget(self.tableView_5)
        self.verticalLayout_6.setStretch(0, 5)
        self.verticalLayout_6.setStretch(1, 2)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 50)
        self.gridLayout_10.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.frame_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.retranslateUi(Frame)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.navigator_label.setText(_translate("Frame", "Navigator"))
        self.account_pushButton.setText(_translate("Frame", "Account Management"))
        self.student_pushButton.setText(_translate("Frame", "Student Management"))
        self.teacher_pushButton.setText(_translate("Frame", "Teacher Management"))
        self.module_pushButton.setText(_translate("Frame", "Module Management"))
        self.attendance_pushButton.setText(_translate("Frame", "Attendance Management"))
        self.AC_label.setText(_translate("Frame", "Account"))
        self.ACcomboBox1.setItemText(0, _translate("Frame", "UserType"))
        self.ACcomboBox2.setItemText(0, _translate("Frame", "Faculty"))
        self.ACcomboBox3.setItemText(0, _translate("Frame", "School"))
        self.ACmodify_toolButton.setText(_translate("Frame", "M"))
        self.ACdelete_toolButton.setText(_translate("Frame", "-"))
        self.ACadd_toolButton.setText(_translate("Frame", "+"))
        self.Stu_label.setText(_translate("Frame", "Student"))
        self.Stu_comboBox1.setItemText(0, _translate("Frame", "Faculty"))
        self.Stu_comboBox2.setItemText(0, _translate("Frame", "School"))
        self.Stu_comboBox3.setItemText(0, _translate("Frame", "Year"))
        self.STUModify_toolButton.setText(_translate("Frame", "M"))
        self.STUdelete_toolButton.setText(_translate("Frame", "-"))
        self.STUadd_toolButton.setText(_translate("Frame", "+"))
        self.teacher_label.setText(_translate("Frame", "Teacher"))
        self.Tea_comboBox1.setItemText(0, _translate("Frame", "Faculty"))
        self.Tea_comboBox2.setItemText(0, _translate("Frame", "School"))
        self.Tea_comboBox3.setItemText(0, _translate("Frame", "Type"))
        self.TEAmodify_toolButton.setText(_translate("Frame", "M"))
        self.TEAdelete_toolButton.setText(_translate("Frame", "-"))
        self.TEAadd_toolButton.setText(_translate("Frame", "+"))
        self.module_label.setText(_translate("Frame", "Module"))
        self.Module_comboBox1.setItemText(0, _translate("Frame", "Faculty"))
        self.Module_comboBox2.setItemText(0, _translate("Frame", "School"))
        self.Module_comboBox3.setItemText(0, _translate("Frame", "Year"))
        self.TEAmodify_toolButton_2.setText(_translate("Frame", "M"))
        self.TEAdelete_toolButton_2.setText(_translate("Frame", "-"))
        self.TEAadd_toolButton_2.setText(_translate("Frame", "+"))
        self.attendence_label.setText(_translate("Frame", "Attendance"))
        self.Att_comboBox1.setItemText(0, _translate("Frame", "Faculty"))
        self.Att_comboBox2.setItemText(0, _translate("Frame", "School"))
        self.Att_comboBox3.setItemText(0, _translate("Frame", "Year"))
        self.Att_comboBox4.setItemText(0, _translate("Frame", "Course"))
        self.Att_comboBox5.setItemText(0, _translate("Frame", "SessionType"))
        self.label_6.setText(_translate("Frame", "Start Time:"))
        self.label_7.setText(_translate("Frame", "End Time:"))
        self.ATTmodify_toolButton.setText(_translate("Frame", "M"))
        self.ATTdelete_toolButton.setText(_translate("Frame", "-"))
        self.ATTadd_toolButton.setText(_translate("Frame", "+"))
import resources.images_rc
