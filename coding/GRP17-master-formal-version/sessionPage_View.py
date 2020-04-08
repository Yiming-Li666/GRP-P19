from sessionFrame1_View import sessionFrame1_View
from sessionFrame1_Model import sessionFrame1_model
from sessionFrame1_Delegate import sessionFrame_delegate
from upcomingEvent_View import upcomingEvent_view
from sessionPage_ctr import sessionPage_ctr
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal, QModelIndex
import ModuleFrame1_View
import Login_View
import Login_ctr
import dbController
import datetime

class sessionPage_View(QMainWindow):
    recordDialog_Signal = pyqtSignal()
    recordedSession_Signal = pyqtSignal()
    def __init__(self,):
        super(sessionPage_View, self).__init__()
        self.window = None

    
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()

    def setMainWindow(self, mainWindow, logCtr):
        self.window = mainWindow
        self.logCtr = logCtr
        self.setupMyUI()

    def setupMyUI(self):
        #connect with Ctr
        self.sessionPageCtr = sessionPage_ctr()
        self.sessionPageCtr.setCtr(self,self.window)

        self.upcomingFrame = upcomingEvent_view()
        self.Frame1 = sessionFrame1_View()

        '''
        Add different sig for passed and future session
        '''
        # connect signal of frame to this page
        self.Frame1.enterRecordingPage_SignalToPage.connect(self.dialogORrecord)
        #self.Frame1.enterRecordingPage_SignalToPage.connect(self.recordedSession)
        
        self.Frame1.setupUi(self.window.sessionFrame1)
        
        self.Frame1.refresh()

        self.upcomingFrame.setupUi(self.window.sessionFrame2)
        self.upcomingFrame.connectToRecord(self.window)


    def dialogORrecord(self, rowNum):
        # if the session has started for two hours
        #print(ModuleFrame1_View.moduleFrame1_view.DateTime)
        endTime = str(int(ModuleFrame1_View.moduleFrame1_view.DateTime[int(rowNum)])+2000000)
        timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
        timer = timer.replace(' ','').replace('-','').replace(':','').replace('.','')
        # if the session is ended or not
        if endTime > timer:
            # dialog info
            self.recordDialog_Signal.emit()
        else:
            # label
            self.fillInfo()
            
            self.recordedSession_Signal.emit()

    def fillInfo(self):
        teacherInformation = dbController.GetTeacherInfo(Login_View.userId)
        self.logCtr.recordedSessionPage_View.Frame1.teacherName_label.setText(teacherInformation[0][1])
        self.logCtr.recordedSessionPage_View.Frame1.sessionName_label.setText(self.Frame1.info[1] + "  " + self.Frame1.info[0])
        self.logCtr.recordedSessionPage_View.Frame1.teachingVenue_label.setText(self.Frame1.info[4] + "  "  + self.Frame1.info[2] + "  "  + self.Frame1.info[3])
        self.logCtr.recordedSessionPage_View.Frame1.attendance_label.setText("Attended")
        self.logCtr.recordedSessionPage_View.Frame1.absentStudent_textBrowser.setText("  aaa\n  bbb\n  ccc\n")
