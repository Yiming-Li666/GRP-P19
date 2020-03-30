from recordDialog_View import recordDialog_View
from upcomingEvent_Model import upcomingEvent_Model
import ModulePage_Ctr
import datetime
# TBC
class sessionPage_ctr():

    def setCtr(self, sessionPageView, mainwindow):
        self.sessionPageView = sessionPageView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.sessionPageView.recordDialog_Signal.connect(self.recordDialog)
        self.sessionPageView.recordedSession_Signal.connect(self.Recorded)

    def recordDialog(self):
        self.dialog = recordDialog_View()
        self.dialog.setSessionWindow(self.mainwindow)
        self.dialog.show()
    
    def Recorded(self):
        self.upcomingModel = upcomingEvent_Model()
        for session in ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData:
            r = session.split()
            r[2] = r[2].replace('-','')
            r[3] = r[3].replace(':','').replace('.','')
            timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
            timer = timer.split()
            timer[0] = timer[0].replace('-','')
            timer[1] = timer[1].replace(':','').replace('.','')
            start = str(int(r[3]) + 2000000)
            if len(start) <= 7 :
                start = "0" + start
            if r[2] == timer[0] and start >= timer[1] :
                s = session.split()
                self.upcomingModel.listItemData.append(s[0] + "   " + s[1] + "\n" + s[2] + "\n" + s[3])
        if len(self.upcomingModel.listItemData) == 0:
            self.upcomingModel.listItemData = ["Today has no upcoming event!\n"]
        print(self.upcomingModel.listItemData)
        self.sessionPageView.logCtr.recordedSessionPage_View.upcomingFrame.listView.setModel(self.upcomingModel)
        self.mainwindow.stackedWidget.setCurrentIndex(7)