from sessionFrame1_Model import sessionFrame1_model
from sessionFrame1_Delegate import sessionFrame_delegate
from upcomingEvent_Model import upcomingEvent_Model
import dbController
import Login_View
import ModulePage_Ctr
import datetime

class ModulePage_ctr():
    sessionModel = sessionFrame1_model()
    def __init__(self):
        self.modulePageView = None

    def setCtr(self, modulePageView, mainwindow):
        self.modulePageView = modulePageView
        self.mainwindow = mainwindow
        self.connectSlot()

    def connectSlot(self):
        self.modulePageView.enterSessionPage_Signal.connect(self.enterSessionPage)

    def enterSessionPage(self):

        #print("to session")
        #load related session Model
        # self.sessionModel = sessionFrame1_model()
        # add the list
        self.sessionDelegate = sessionFrame_delegate()
        self.modulePageView.logCtr.sessionView.Frame1.listView.setModel(self.sessionModel)
        self.modulePageView.logCtr.sessionView.Frame1.listView.setItemDelegate(self.sessionDelegate)

        self.upcomingModel = upcomingEvent_Model()
        self.loadUpcoming()
        self.modulePageView.logCtr.sessionView.upcomingFrame.listView.setModel(self.upcomingModel)
        
        #change page
        self.mainwindow.stackedWidget.setCurrentIndex(1)

    def loadUpcoming(self):    
        print(ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData)
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
            print(start)
            if r[2] == timer[0] and start >= timer[1] :
                s = session.split()
                self.upcomingModel.listItemData.append(s[0] + "   " + s[1] + "\n" + s[2] + "\n" + s[3])
        if len(self.upcomingModel.listItemData) == 0:
            self.upcomingModel.listItemData = ["Today has    no     upcoming event!\n"]
        print(self.upcomingModel.listItemData)