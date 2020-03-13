from PyQt5.QtWidgets import QDialog

from printDialog_View import printDialog_view
from upcomingEvent_Model import upcomingEvent_Model

class basicMainWindow_Ctr():

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
        self.bmView.teacherInfo_Sig.connect(self.clickTeacherInfo)
        self.bmView.print_Sig.connect(self.printInfo)

    def backTo(self):
        if self.bmView.stackedWidget.currentIndex() == 1: #session to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        elif self.bmView.stackedWidget.currentIndex() == 2: #recoridng to session
            self.bmView.stackedWidget.setCurrentIndex(1)
        elif self.bmView.stackedWidget.currentIndex() == 4: #one student to general result
            self.bmView.stackedWidget.setCurrentIndex(3)
        elif self.bmView.stackedWidget.currentIndex() == 3: #general result to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        elif self.bmView.stackedWidget.currentIndex() == 5: #teacher info to module
            self.bmView.stackedWidget.setCurrentIndex(0)
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
        print("search student") 

        '''
        load student list View and model here
        self.logCtr.searchResult_View.Frame1.listView
        '''
        # TODO: write the code when connect to the database

        self.upcomingModel = upcomingEvent_Model()
        self.logCtr.searchResult_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.bmView.stackedWidget.setCurrentIndex(3)
        

        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def clickTeacherInfo(self):
        print("Teacher Info")
        '''
        load teacher info here OR load in Login_ctr when set the page
        '''
        self.upcomingModel = upcomingEvent_Model()
        self.logCtr.teacherInfoPage_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.bmView.stackedWidget.setCurrentIndex(5)
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def printInfo(self):
        print("print")
        self.printDialog = printDialog_view()
        self.printDialog.show()

        







