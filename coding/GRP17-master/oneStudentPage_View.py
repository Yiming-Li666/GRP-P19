from oneStudentFrame_View import oneStudentFrame_view
from upcomingEvent_View import upcomingEvent_view
from PyQt5.QtWidgets import QApplication, QMainWindow
from upcomingEvent_Model import upcomingEvent_Model
import sys

class oneStudentPage_View(QMainWindow):

    def __init__(self):
        super(oneStudentPage_View, self).__init__()
        
        ##connect with Ctr
        
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
    
    def setMainWindow(self, mainWindow):
        self.window = mainWindow
        self.setupMyUI()
    
    def setupMyUI(self):
        #build view
        self.Frame1 = oneStudentFrame_view()
        self.upcomingFrame = upcomingEvent_view()

        #setUp view
        self.Frame1.setupUi(self.window.oneStudentFrame1)
        self.upcomingFrame.setupUi(self.window.oneStudentFrame2)