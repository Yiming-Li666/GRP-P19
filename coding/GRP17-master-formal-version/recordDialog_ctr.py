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
        self.recordingPage_View = recordingPage_View()
        self.recordingPage_View.setMainWindow(self.mainwindow)
        self.recordingPage_View.Frame1.frameName_TBS.setText("Comp1010")
        self.recordingPage_View.Frame1.attendceRatio_label.setText("0/100")
        self.recordingPage_View.Frame1.attendance_progressBar.setValue(0)
        self.mainwindow.stackedWidget.setCurrentIndex(2)
        self.recordDialogView.hide()