from oneStudentPage_View import oneStudentPage_View
from oneStudentFrame_Model import oneStudentFrame_model
from searchStudentFrame_Model import searchStudentFrame_model
from upcomingEvent_Model import upcomingEvent_Model
from basicMainWindow_Ctr import basicMainWindow_Ctr
import dbController
import ModulePage_Ctr
import datetime

class searchResult_Ctr():
    def setCtr(self, searchResultView, mainwindow):
        self.searchResultView = searchResultView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.searchResultView.OneStudentInfo_Signal.connect(self.OneStudentInfo)
    
    def OneStudentInfo(self, rowNum):
        # print("One Student")
        # set model for view in oneStudentPage_View
        self.upcomingModel = upcomingEvent_Model()
        self.loadUpcoming()
        self.searchResultView.logCtr.oneStudentPage_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.studentAttendanceModel = oneStudentFrame_model()
        # student info
        IdName = basicMainWindow_Ctr.searchResultModel.listItemData[int(rowNum)]
        IdName = IdName.split('   ',1)
        studentDetail = dbController.GetStudentInfo(IdName[0])
        '''
            s[0]: lessonId
            s[1]: studentId
            s[2]: Attended or not /boolean
            s[3]: attend time
        '''
        for s in studentDetail:
            if s[2] == 1:
                self.studentAttendanceModel.listItemData.append(s[0] + "  " + str(s[3]))
            else:
                self.studentAttendanceModel.listItemData.append(s[0] + "  absent")

        self.searchResultView.logCtr.oneStudentPage_View.Frame1.attendance_listView.setModel(self.studentAttendanceModel)
        self.mainwindow.stackedWidget.setCurrentIndex(4)

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
