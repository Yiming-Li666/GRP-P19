from PyQt5 import QtCore

from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.basicStructure_frame1 import Ui_Frame
import sys


class studentFrame1_View(QFrame,Ui_Frame):

    def __init__(self):
        # setup UI
        super(studentFrame1_View, self).__init__()
        self.setupUi(self)
        # self.refresh()

    def refresh(self):
        self.search_lineEdit.hide()
        self.search_toolButton.hide()
        self.addButton.hide()
        self.setStudentName()


    def setStudentName(self):
        self.frameName_TBS.setText("Student Name")
        """
            Require the searching student name
        """
        # TODO: not implemented yet


    def print(self):
        print("print recording")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def showNum(self):
        print("edit show Num")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def leftPage(self):
        print("left page")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def rightPage(self):
        print("right page")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sort(self):
        print("sort")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

# test code

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.resize(800, 600)

    frame1 = QFrame(mainWindow)
    frame1.setGeometry(QtCore.QRect(0, 0, 300, 300))

    test = studentFrame1_View()

    test.show()
    sys.exit(app.exec_())