import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

# the line Widget
class lineWidget(QWidget):

    def __init__(self, parent = None):
        super(lineWidget, self).__init__(parent)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.toolButton_8 = QtWidgets.QToolButton(self)
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout_6.addWidget(self.toolButton_8)
        self.toolButton_9 = QtWidgets.QToolButton(self)
        self.toolButton_9.setObjectName("toolButton_9")
        self.horizontalLayout_6.addWidget(self.toolButton_9)
        self.toolButton_10 = QtWidgets.QToolButton(self)
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
        spacerItem = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)

        self.toolButton_8.setText("M")
        self.toolButton_9.setText("-")
        self.toolButton_10.setText("⭐")

# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.resize(400,300)
    test = lineWidget(window)
    test.setGeometry(10,10,300,150)
    window.show()
    sys.exit(app.exec_())