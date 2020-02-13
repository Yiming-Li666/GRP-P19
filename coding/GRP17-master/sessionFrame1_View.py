from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.basicStructure_frame1 import Ui_Frame
import sys


class sessionFrame1_View(QFrame,Ui_Frame):

    # send signal to module page
    enterRecordingPage_SignalToPage = pyqtSignal()

    def __init__(self):
        # setup UI
        super(sessionFrame1_View, self).__init__()
        self.setupUi(self)
        # self.refresh()
        
    def refresh(self):
        self.frameName_TBS.setText("Teaching Session")
        self.setSlot()

    def setSlot(self):
        self.search_toolButton.clicked.connect(self.searchSession)
        self.search_lineEdit.returnPressed.connect(self.searchSession)
        self.addButton.clicked.connect(self.addSession)
        self.listView.doubleClicked.connect(self.doubleClicked)
        self.listView.clicked.connect(self.goSession)

    def goSession(self, qModelIndex):
        # TODO: jump to the page
        print("go to " + str(qModelIndex.row()))
        self.enterRecordingPage_SignalToPage.emit()

    def doubleClicked(self, qModelIndex):
        print("you choosed " + str(qModelIndex.row()))

    def searchSession(self):
        print("search Session")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def print(self):
        print("print recording")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def addSession(self):
        print("add Session")
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

    test = sessionFrame1_View()

    test.show()
    sys.exit(app.exec_())