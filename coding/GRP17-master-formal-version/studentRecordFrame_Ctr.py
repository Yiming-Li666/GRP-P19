from modifyDialog_View import modifyDialog_View
class studentRecordFrame_Ctr():

    def setCtr(self, studentRecordFrame):
        self.studentRecordFrame = studentRecordFrame
        self.connectSlot()
    
    def connectSlot(self):
        self.studentRecordFrame.modifyDialog_Signal.connect(self.recordDialog)

    def recordDialog(self):
        self.dialog = modifyDialog_View()
        self.dialog.show()