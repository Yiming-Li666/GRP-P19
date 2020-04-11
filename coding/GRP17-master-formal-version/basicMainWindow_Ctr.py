from PyQt5.QtWidgets import QDialog
from printDialog_View import printDialog_view
from upcomingEvent_Model import upcomingEvent_Model
from basicMainWindow_View import basicMainWindow_view
from upcomingEvent_View import upcomingEvent_view
from sessionFrame1_Model import sessionFrame1_model
from sessionFrame1_Delegate import sessionFrame_delegate
from accountDialog_View import accountDialog_view
from searchStudentFrame_Model import searchStudentFrame_model
from PyQt5.Qt import *
from PyQt5 import QtCore
import ModulePage_Ctr
import datetime
import dbController
import Login_ctr
import Login_View

class basicMainWindow_Ctr():
    searchResultList = []
    def __init__(self):
        self.bind()

    def bind(self):
        self.bmView = None
        # TODO: bind model
        # self.NameModel =

    def setView(self, bmView, logCtr):
        self.bmView = bmView
        #to get searchResult_View in logCtr
        self.logCtr = logCtr
        self.connectSlot()

    def setWindow(self, window):
        self.window = window

    def connectSlot(self):
        self.bmView.backTo_Sig.connect(self.backTo)
        self.bmView.home_Sig.connect(self.home)
        self.bmView.searchStudent_Sig.connect(self.searchStudent)
        self.bmView.lineEdit_4.returnPressed.connect(self.searchStudent)
        self.bmView.teacherInfo_Sig.connect(self.clickTeacherInfo)
        self.bmView.print_Sig.connect(self.printInfo)

    def backTo(self):
        if self.bmView.stackedWidget.currentIndex() == 1: #session to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        elif self.bmView.stackedWidget.currentIndex() == 2: #recoridng to session
            #防止一开始从module界面的upcoming直接record, 返回时session界面为空
            #self.sessionModel = sessionFrame1_model()
            #self.sessionDelegate = sessionFrame_delegate()
            #self.logCtr.sessionView.Frame1.listView.setModel(self.sessionModel)
            #self.logCtr.sessionView.Frame1.listView.setItemDelegate(self.sessionDelegate)
            #self.upcomingModel = upcomingEvent_Model()
            #self.logCtr.sessionView.upcomingFrame.listView.setModel(self.upcomingModel)

            self.bmView.stackedWidget.setCurrentIndex(1)
        elif self.bmView.stackedWidget.currentIndex() == 4: #one student to general result
            self.bmView.stackedWidget.setCurrentIndex(3)
        elif self.bmView.stackedWidget.currentIndex() == 3: #general result to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        elif self.bmView.stackedWidget.currentIndex() == 5: #teacher info to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        elif self.bmView.stackedWidget.currentIndex() == 6: #Student Record to one student
            self.bmView.stackedWidget.setCurrentIndex(4)
        elif self.bmView.stackedWidget.currentIndex() == 7: #recorded session to session list
            self.bmView.stackedWidget.setCurrentIndex(1)
        
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def home(self):
        print("go home")
        self.bmView.stackedWidget.setCurrentIndex(0)
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def searchStudent(self):
        # read from text box
        searchResultModel = searchStudentFrame_model()
        searchResultModel.listItemData = []
        self.searchResultList.clear()
        if self.bmView.lineEdit_4.text() == '':
            searchResultModel.listItemData.append("No result!")
            self.searchResultList.append("No result!")
        else:
            students = dbController.SearchStudentByName(self.bmView.lineEdit_4.text())
            if len(students) != 0:
                for r in students:
                    searchResultModel.listItemData.append(r[0] + "   " + r[1])
                    self.searchResultList.append(r[0] + "   " + r[1])
                #print(students[0][0])
            else:
                searchResultModel.listItemData.append("No result!")
                self.searchResultList.append("No result!")
        self.logCtr.searchResult_View.Frame1.listView.setModel(searchResultModel)
        #self.logCtr.searchResult_View.Frame1.listView.setAlternatingRowColors(True)
        #print(searchResultModel.listItemData) 
        #print("111")
        #print(self.searchResultList)

        self.upcomingModel = upcomingEvent_Model()
        self.loadUpcoming()
        self.logCtr.searchResult_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.bmView.stackedWidget.setCurrentIndex(3)
        

        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def clickTeacherInfo(self):
        print("Teacher Info")
        # create a dialog to give teacher information
        self.dl = accountDialog_view()
        # dl.setWindowTitle('Teacher information')
        # dl.resize(300,200)
        # get userId from the login page
        # link to database ask for teacher information
        teacherInformation = dbController.GetTeacherInfo(Login_View.userId)
        # teacherInformation is a 2D array
        # get teacher name
        self.dl.teacherName_label.setText(teacherInformation[0][1])
        # set position
        # dl.name.setGeometry(QtCore.QRect(50, 20, 250, 50))
        # get all the module name
        str = ""
        for r in teacherInformation:
            str = str + r[2] + "\n"
        self.dl.module_label.setText(str)
        # set position
        # dl.module.setGeometry(QtCore.QRect(50, 60, 250, 100))
        # create a button to close the window
        self.dl.logout_pushButton.clicked.connect(self.close)
        # lock the parent window
        # self.dl.setWindowModality(Qt. WindowModal)
        self.dl.show()
        # dl.exec_()

    def close(self):
        self.dl.close()
        # TODO: user logout

    def printInfo(self):
        print("print")
        self.printDialog = printDialog_view()
        # load listview
        self.printDialog.show()

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
        







