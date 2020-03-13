from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from resources.teacherUIPY.basicStructure_mainWindow import MainWindow_Structure
import sys


class basicMainWindow_view(QMainWindow,  MainWindow_Structure):

    # signals sent tp controller for operation
    backTo_Sig = pyqtSignal()
    home_Sig = pyqtSignal()
    searchStudent_Sig = pyqtSignal()
    teacherInfo_Sig = pyqtSignal()
    print_Sig = pyqtSignal()

    #TODO: implementation of status bar

    def __init__(self):
        super(basicMainWindow_view, self).__init__()
        self.setupUi(self)

    # back to last page
    def backTo(self):
        self.backTo_Sig.emit()

    # back to home page
    def home(self):
        self.home_Sig.emit()

    # search student
    def searchStudent(self):
        self.searchStudent_Sig.emit()

    # teacher info button
    def clickTeacherInfo(self):
        self.teacherInfo_Sig.emit()
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet
    
    def printInfo(self):
        self.print_Sig.emit()


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = basicMainWindow_view()
    mainWindow.show()
    sys.exit(app.exec_())