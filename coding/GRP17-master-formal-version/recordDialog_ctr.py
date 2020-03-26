from recordingPage_View import recordingPage_View
from basicMainWindow_View import basicMainWindow_view
from basicMainWindow_Ctr import basicMainWindow_Ctr

class recordDialog_ctr():
    def setCtr(self, recordDialogView, mainwindow):
        self.recordDialogView = recordDialogView
        self.mainwindow = mainwindow
        self.connectSlot()

    def connectSlot(self):
        self.recordDialogView.startRecord_Signal.connect(self.recording)
    
        
    def recording(self):
        print("start record")
        self.mainwindow.stackedWidget.setCurrentIndex(2)
        self.recordDialogView.hide()