from resources.teacherUIPY.modifyState_Dialog import modifyState_Dialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog

class modifyDialog_View(QDialog, modifyState_Dialog):
    def __init__(self):
        super(modifyDialog_View, self).__init__()
        self.setupUi(self)
    
    def confirmReset(self):
        print("Confirm")
        self.hide()
        
        '''
        Change the showing student state here
        '''

    def cancelReset(self):
        print("Cancel")
        self.hide()
    def editState(self):
        print("Edit State")