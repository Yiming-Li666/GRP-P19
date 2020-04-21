from recordDialog_View import recordDialog_View
class upcomingEvent_Ctr():

    def __init__(self):
        self.bind()

    def bind(self):
        self.nameView = None
        # TODO: bind model
        # self.nameModel =

    def setView(self,nameView):
        self.nameView = nameView
    
    def setCtr(self, UpcomingView, mainwindow):
        self.UpcomingView = UpcomingView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.UpcomingView.recordDialog_Signal.connect(self.recordDialog)
    
    def recordDialog(self):
        self.dialog = recordDialog_View()
        self.dialog.setSessionWindow(self.mainwindow)
        self.dialog.show()