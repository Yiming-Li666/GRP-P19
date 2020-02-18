from basicMainWindow_View import basicMainWindow_view
class basicMainWindow_Ctr():

    def __init__(self):
        self.bind()

    def bind(self):
        self.bmView = None
        # TODO: bind model
        # self.NameModel =

    def setView(self, bmView):
        self.bmView = bmView
        self.connectSlot()

    def setWindow(self, window):
        self.window = window

    def connectSlot(self):
        self.bmView.backTo_Sig.connect(self.backTo)
        self.bmView.home_Sig.connect(self.home)
        self.bmView.searchStudent_Sig.connect(self.searchStudent)
        self.bmView.teacherInfo_Sig.connect(self.clickTeacherInfo)

    def backTo(self):
        if self.window.Frame1.frameName_TBS.text() == "Module" :
            print("first Page")

        elif self.window.Frame1.frameName_TBS.text() == "Teaching Session" :
            print("back to Module")
            self.mainWindow = basicMainWindow_view()
            self.setView(self.mainWindow)
            self.window.hide()
            ## aviod import error
            from ModulePage_View import modulePage_view
            self.ModuleView = modulePage_view()
            self.ModuleView.setMainWindow(self.mainWindow)

            self.setWindow(self.ModuleView)

            self.ModuleView.show()

        elif self.window.Frame1.frameName_TBS.text() == "ModuleName:" : ###### ???Depends on if change the ModuleName
            print("back to Session")
            self.mainWindow = basicMainWindow_view()
            self.setView(self.mainWindow)
            self.window.hide()
            #avoid import error
            from sessionPage_View import sessionPage_View
            self.sessionView = sessionPage_View()
            self.sessionView.setMainWindow(self.mainWindow)
            self.setWindow(self.sessionView)
            self.sessionView.show()

        elif self.window.Frame1.frameName_TBS.text() == "Student Name" :
            self.mainWindow = basicMainWindow_view()
            self.setView(self.mainWindow)
            self.window.hide()
            ## aviod import error
            from ModulePage_View import modulePage_view
            self.ModuleView = modulePage_view()
            self.ModuleView.setMainWindow(self.mainWindow)

            self.setWindow(self.ModuleView)

            self.ModuleView.show()

        elif self.window.Frame1.frameName_TBS.text() == "Search Result:" :
            self.mainWindow = basicMainWindow_view()
            self.setView(self.mainWindow)
            self.window.hide()
            ## aviod import error
            from searchResult_View import searchResult_View
            self.searchResult = searchResult_View()
            self.searchResult.setMainWindow(self.mainWindow)

            self.setWindow(self.searchResult)

            self.searchResult.show()

        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def home(self):
        print("go home")
        self.mainWindow = basicMainWindow_view()
        self.setView(self.mainWindow)
        self.window.hide()
        ## aviod import error
        from ModulePage_View import modulePage_view
        self.ModuleView = modulePage_view()
        self.ModuleView.setMainWindow(self.mainWindow)

        self.setWindow(self.ModuleView)

        self.ModuleView.show()
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def searchStudent(self):
        print("search student")
        self.mainWindow = basicMainWindow_view()
        self.setView(self.mainWindow)
        self.window.hide()
        #avoid import error
        from searchResult_View import searchResult_View
        self.searchResult = searchResult_View()
        self.searchResult.setMainWindow(self.mainWindow)
        self.setWindow(self.searchResult)
        self.searchResult.show()   
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def clickTeacherInfo(self):
        print("Teacher Info")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet







