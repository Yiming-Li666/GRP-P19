from resources.teacherUIPY.startRecord_dialog import startRecord_dialog
from recordDialog_ctr import recordDialog_ctr
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog


class recordDialog_View(QDialog, startRecord_dialog):
    startRecord_Signal = pyqtSignal()

    def __init__(self):
        super(recordDialog_View, self).__init__()
        self.setupUi(self)

        #connect with Ctr
        self.recordDialogCtr = recordDialog_ctr()
        self.recordDialogCtr.setCtr(self)

        self.pushButton.clicked.connect(self.startRecord)

    def startRecord(self):
        self.startRecord_Signal.emit()