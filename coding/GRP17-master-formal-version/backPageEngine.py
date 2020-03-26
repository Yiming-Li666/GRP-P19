from sessionPage_View import sessionPage_View

class backPageEngine():
    def backToModule(self, mainwindow, mainWindowCtr):
        self.ModuleView = sessionPage_View()
        self.ModuleView.setMainWindow(mainwindow)

        mainWindowCtr.setWindow(self.ModuleView)

