from recordingPage_View import recordingPage_View
from basicMainWindow_View import basicMainWindow_view
from basicMainWindow_Ctr import basicMainWindow_Ctr
class recordDialog_ctr():
    def setCtr(self, recordDialogView):
        self.recordDialogView = recordDialogView
        self.connectSlot()

    def connectSlot(self):
        self.recordDialogView.startRecord_Signal.connect(self.recording)
    

    def recording(self):
        print("start record")
        self.mainWindow = basicMainWindow_view()
        self.mainWindowCtr = basicMainWindow_Ctr()
        self.mainWindowCtr.setView(self.mainWindow)

        self.recordingPage_View = recordingPage_View()
        self.recordingPage_View.setMainWindow(self.mainWindow)
        self.recordingPage_View.show()
        self.recordDialogView.hide()
        
        