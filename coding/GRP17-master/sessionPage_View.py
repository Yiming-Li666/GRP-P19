from sessionFrame1_View import sessionFrame1_View
from sessionFrame1_Model import sessionFrame1_model
from sessionFrame1_Delegate import sessionFrame_delegate
from upcomingEvent_View import upcomingEvent_view
from sessionPage_ctr import sessionPage_ctr
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal


class sessionPage_View(QMainWindow):
    recordDialog_Signal = pyqtSignal()

    def __init__(self):
        super(sessionPage_View, self).__init__()
        self.window = None

        #connect with Ctr
        self.sessionPageCtr = sessionPage_ctr()
        self.sessionPageCtr.setCtr(self)
    
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()

    def setMainWindow(self, mainWindow):
        self.window = mainWindow
        self.setupMyUI()

    def setupMyUI(self):
        self.upcomingFrame = upcomingEvent_view()
        self.Frame1 = sessionFrame1_View()
        sessionModel = sessionFrame1_model()
        sessionDelegate = sessionFrame_delegate()

        # connect signal of frame to this page
        self.Frame1.enterRecordingPage_SignalToPage.connect(self.recordDialog)

        # set model and delegate for views
        self.Frame1.setupUi(self.window.frame1)
        self.Frame1.listView.setModel(sessionModel)
        self.Frame1.listView.setItemDelegate(sessionDelegate)
        self.Frame1.refresh()

        self.upcomingFrame.setupUi(self.window.frame_2)
    
    def recordDialog(self):
        print("dialog")
        self.recordDialog_Signal.emit()
