# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacherModule.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import resources.images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1101, 45))
        self.widget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.toolButton.setStyleSheet("border-image: url(:/all/images/backIcon.png);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.widget)
        self.toolButton_2.setGeometry(QtCore.QRect(70, 10, 25, 25))
        self.toolButton_2.setStyleSheet("border-image: url(:/all/images/homeIcon.png)")
        self.toolButton_2.setText("")
        self.toolButton_2.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.widget)
        self.toolButton_3.setGeometry(QtCore.QRect(590, 10, 25, 25))
        self.toolButton_3.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(630, 10, 255, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(960, 10, 100, 25))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 1111, 581))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1109, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(20, 30, 691, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(35, 70, 90, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 250, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.listView = QtWidgets.QListView(self.frame)
        self.listView.setGeometry(QtCore.QRect(30, 120, 641, 341))
        self.listView.setObjectName("listView")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 480, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 480, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(610, 480, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(650, 480, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setObjectName("label_6")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(420, 70, 25, 25))
        self.toolButton_4.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 119, 641, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setGeometry(QtCore.QRect(760, 30, 271, 521))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.listView_2 = QtWidgets.QListView(self.frame_2)
        self.listView_2.setGeometry(QtCore.QRect(10, 60, 255, 401))
        self.listView_2.setObjectName("listView_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 480, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 480, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(220, 480, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(250, 480, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setObjectName("label_9")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setGeometry(QtCore.QRect(471, 197, 169, 54))
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TeacherName"))
        self.label.setText(_translate("MainWindow", "Module"))
        self.comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox.setItemText(1, _translate("MainWindow", "In Progress"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Future"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Past"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Starred"))
        self.label_4.setText(_translate("MainWindow", "Show"))
        self.lineEdit_2.setText(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "<"))
        self.label_6.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "Upcoming Events"))
        self.label_7.setText(_translate("MainWindow", "Show"))
        self.lineEdit_3.setText(_translate("MainWindow", "5"))
        self.label_8.setText(_translate("MainWindow", "<"))
        self.label_9.setText(_translate("MainWindow", ">"))
        self.menuFile.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
