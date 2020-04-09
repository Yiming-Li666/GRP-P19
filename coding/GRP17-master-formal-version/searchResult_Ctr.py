#from oneStudentPage_View import oneStudentPage_View
from oneStudentFrame_Model import oneStudentFrame_model
from searchStudentFrame_Model import searchStudentFrame_model
from upcomingEvent_Model import upcomingEvent_Model
from basicMainWindow_Ctr import basicMainWindow_Ctr
import dbController
import ModulePage_Ctr
import datetime

class searchResult_Ctr():
    IdName = []
    studentAttend = []
    def setCtr(self, searchResultView, mainwindow):
        self.searchResultView = searchResultView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.searchResultView.OneStudentInfo_Signal.connect(self.OneStudentInfo)
    
    def OneStudentInfo(self, rowNum):
        #print(self.searchResultView.logCtr.oneStudentPage_View.Frame1.comboBox_5.currentText())
        # set model for view in oneStudentPage_View
        self.upcomingModel = upcomingEvent_Model()
        self.loadUpcoming()
        self.searchResultView.logCtr.oneStudentPage_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.studentAttendanceModel = oneStudentFrame_model()
        self.studentAttend.clear()
        # student info
        #print(basicMainWindow_Ctr.searchResultList)
        IN = basicMainWindow_Ctr.searchResultList[int(rowNum)]
        IN = IN.split('   ',1)
        self.IdName.append(IN[0])
        self.IdName.append(IN[1])
        studentDetail = dbController.GetStudentInfo(self.IdName[0])
        isAttend = 0
        isAbsent = 0
        totalNum = len(studentDetail)
        '''
            s[0]: ModuleId
            s[1]: lessonId
            s[2]: studentId
            s[3]: Attended or not /boolean
            s[4]: attend time
        '''
        for s in studentDetail:
            self.studentAttend.append(s)
            if s[3] == 1:
                self.studentAttendanceModel.listItemData.append(s[0] + "  " + s[1] + "  " + str(s[4]))
                isAttend = isAttend + 1
            else:
                self.studentAttendanceModel.listItemData.append(s[0] + "  " + s[1] + "  absent")
                isAbsent = isAbsent + 1
        # search result list
        self.searchResultView.logCtr.oneStudentPage_View.Frame1.attendance_listView.setModel(self.studentAttendanceModel)
        # search result summary
        attendanceInfo = dbController.GetAttendanceInfo(self.IdName[0])
        attendedInfo = dbController.GetAttendedInfo(self.IdName[0])
        sum = "Student name:  " + self.IdName[1] + "\nStudent Id:  " + self.IdName[0]
        '''
        attendanceInfo[a][0]: session number
        attendanceInfo[a][1]: module name
        attendedInfo[a][0]: attended session number
        '''
        for a in range(len(attendanceInfo)):
            self.searchResultView.logCtr.oneStudentPage_View.Frame1.comboBox.addItem(attendanceInfo[a][1])
            sum = sum + "\n" + attendanceInfo[a][1] + "  attended:  " + str(attendedInfo[a][0]) + "/" + str(attendanceInfo[a][0])
        sum = sum + "\nTotal attendence:  " + str(isAttend) + "/" + str(totalNum) + "\nTotal absent:  " + str(isAbsent)
        self.searchResultView.logCtr.oneStudentPage_View.Frame1.summary_textBrowser.setText(sum)
        self.searchResultView.logCtr.oneStudentPage_View.Frame1.refresh()
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
