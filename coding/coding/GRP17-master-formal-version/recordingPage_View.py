from recordingFrame_View import recordingFrame_View
import globalVar


class recordingPage_View():
    def __init__(self):
        super(recordingPage_View, self).__init__()

        # connect with ctr
        # TODO: controller of recording page

    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()

    def setMainWindow(self, mainwindow):
        self.window = mainwindow
        self.setupMyUI()

    def setupMyUI(self):
        self.Frame1 = recordingFrame_View(self.window)
        globalVar.set_value('RecordingPage', self.Frame1)
        self.Frame1.setupUi(self.window.recordingFrame)
