from recordDialog_View import recordDialog_View


# TBC
class sessionPage_ctr():

    def setCtr(self, sessionPageView, mainwindow):
        self.sessionPageView = sessionPageView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.sessionPageView.recordDialog_Signal.connect(self.recordDialog)

    def recordDialog(self):
        self.dialog = recordDialog_View()
        self.dialog.setSessionWindow(self.mainwindow)
        self.dialog.show()