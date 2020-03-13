from searchStudentFrame_View import searchStudentFrame_view
from searchStudentFrame_Model import searchStudentFrame_model
from upcomingEvent_View import upcomingEvent_view
from PyQt5.QtWidgets import QMainWindow, QApplication
from searchResult_Ctr import searchResult_Ctr
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets

class searchResult_view(QMainWindow):
    OneStudentInfo_Signal = pyqtSignal()

    def __init__(self):
        super(searchResult_view, self).__init__()
        
        
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
    
    def setMainWindow(self, mainWindow, logCtr):
        self.window = mainWindow
        #to get View in class logCtr
        self.logCtr = logCtr
        self.setupMyUI()
    
    def setupMyUI(self):
        ##connect with Ctr
        self.searchResultCtr = searchResult_Ctr()
        self.searchResultCtr.setCtr(self, self.window)

        #build view and model
        self.Frame1 = searchStudentFrame_view()
        self.searchResultModel = searchStudentFrame_model()
        self.upcomingFrame = upcomingEvent_view()

        # connect signal of frame to this page
        self.Frame1. enterStudentPage_SignalToPage.connect(self.goStudentInfo)

        #set Model for views when enter the page
        self.Frame1.setupUi(self.window.resultFrame1)
        self.Frame1.listView.setModel(self.searchResultModel)
        self.Frame1.refresh()

        self.upcomingFrame.setupUi(self.window.resultFrame2)

    def goStudentInfo(self):
        self.OneStudentInfo_Signal.emit()


