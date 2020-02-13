from recordDialog_View import recordDialog_View


# TBC
class sessionPage_ctr():

    def setCtr(self, sessionPageView):
        self.sessionPageView = sessionPageView
        self.connectSlot()
    
    def connectSlot(self):
        self.sessionPageView.recordDialog_Signal.connect(self.recordDialog)

    def recordDialog(self):
        self.dialog = recordDialog_View()
        self.dialog.show()