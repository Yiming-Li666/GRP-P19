from upcomingEvent_Model import upcomingEvent_Model
import ModulePage_Ctr
import datetime

class oneStudentPage_Ctr():
    def __init__(self):
        self.oneStudentPageView = None
        self.mainwindow = None

    def setCtr(self, oneStudentPageView, mainwindow):
        self.oneStudentPageView = oneStudentPageView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.oneStudentPageView.studentRecord_Sig.connect(self.enterStudentRecordPage)

    def enterStudentRecordPage(self):
        self.upcomingModel = upcomingEvent_Model()
        self.loadUpcoming()
        self.oneStudentPageView.logCtr.studentRecordPage_View.upcomingFrame.listView.setModel(self.upcomingModel)
        self.mainwindow.stackedWidget.setCurrentIndex(6)

    def loadUpcoming(self):    
        #print(ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData)
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
            #print(start)
            if r[2] == timer[0] and start >= timer[1] :
                s = session.split()
                self.upcomingModel.listItemData.append(s[0] + "   " + s[1] + "\n" + s[2] + "\n" + s[3])
        if len(self.upcomingModel.listItemData) == 0:
            self.upcomingModel.listItemData = ["Today has no upcoming event!\n"]
        #print(self.upcomingModel.listItemData)