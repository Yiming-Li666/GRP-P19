from searchStudentFrame_View import searchStudentFrame_View
from upcomingEvent_View import upcomingEvent_view
from PyQt5.QtWidgets import QApplication, QMainWindow
from upcomingEvent_Model import upcomingEvent_Model
from searchResult_Ctr import searchResult_Ctr
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets

class searchResult_View(QMainWindow):
    OneStudentInfo_Signal = pyqtSignal()

    def __init__(self):
        super(searchResult_View, self).__init__()
        
        ##connect with Ctr
        self.searchResultCtr = searchResult_Ctr()
        self.searchResultCtr.setCtr(self)
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
    
    def setMainWindow(self, mainWindow):
        self.window = mainWindow
        self.setupMyUI()
    
    def setupMyUI(self):
        #build view
        self.Frame1 = searchStudentFrame_View()
        self.upcomingFrame = upcomingEvent_view()
        upcomingModel = upcomingEvent_Model()

        #set Model
        self.Frame1.setupUi(self.window.frame1)
        self.upcomingFrame.setupUi(self.window.frame_2)
        self.upcomingFrame.listView.setModel(upcomingModel)
    
        #Test Button
        self.btn = QtWidgets.QPushButton(self.window)
        self.btn.setText("StudentName       123456")
        self.btn.setGeometry(40,300,650,50)
        self.btn.clicked.connect(self.goStudentInfo)

    def goStudentInfo(self):
        self.OneStudentInfo_Signal.emit()
        



