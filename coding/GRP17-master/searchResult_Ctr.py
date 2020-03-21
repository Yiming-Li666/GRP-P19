from basicMainWindow_View import basicMainWindow_view

from basicMainWindow_Ctr import basicMainWindow_Ctr

from oneStudentPage_View import oneStudentPage_View
class searchResult_Ctr():
    def setCtr(self, searchResultView):
        self.searchResultView = searchResultView
        self.connectSlot()
    
    def connectSlot(self):
        self.searchResultView.OneStudentInfo_Signal.connect(self.OneStudentInfo)
    
    def OneStudentInfo(self):
        print("One Student")
        self.mainWindow = basicMainWindow_view()
        self.mainWindowCtr = basicMainWindow_Ctr()
        self.mainWindowCtr.setView(self.mainWindow)

        self.oneStudentPage = oneStudentPage_View()
        self.oneStudentPage.setMainWindow(self.mainWindow)

        self.mainWindowCtr.setWindow(self.oneStudentPage)

        self.oneStudentPage.show()
        self.searchResultView.hide()