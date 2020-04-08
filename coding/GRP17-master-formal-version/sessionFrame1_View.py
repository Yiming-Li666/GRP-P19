from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.basicStructure_frame1 import Ui_Frame
from CommonHelper import CommonHelper
from sessionFrame1_Model import sessionFrame1_model
import ModulePage_Ctr
import Login_ctr
import datetime
import sys


class sessionFrame1_View(QFrame,Ui_Frame):

    # send signal to module page
    enterRecordingPage_SignalToPage = pyqtSignal(str)
    info = []
    def __init__(self):
        # setup UI
        super(sessionFrame1_View, self).__init__()
        self.setupUi(self)
        # self.refresh()
        
    def refresh(self):
        self.frameName_TBS.setText("Teaching Session")
        self.setSlot()

    def setSlot(self):
        self.search_toolButton.clicked.connect(self.searchSession)
        self.search_lineEdit.returnPressed.connect(self.searchSession)
        #self.comboBox.currentIndexChanged.connect(self.getComboBoxItem)
        self.addButton.clicked.connect(self.addSession)
        self.listView.doubleClicked.connect(self.doubleClicked)
        self.listView.clicked.connect(self.goSession)

    def goSession(self, qModelIndex):
        #print(self.listView.currentText)
        #selected = self.listView.currentIndex()
        #print(selected)
        #print(self.sessonId)
        # TODO: jump to the page
        sortI = self.comboBox.currentText()
        if sortI == "In Progress":
            s = self.Process_sessionModel.listItemData[qModelIndex.row()]
        elif sortI == "Future":
            s = self.Future_sessionModel.listItemData[qModelIndex.row()]
        elif sortI == "Past":
            s = self.Past_sessionModel.listItemData[qModelIndex.row()]
        else:
            s = ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData[qModelIndex.row()]
        self.info = s.split()

        #print(self.info)
        #print("go to " + str(qModelIndex.row()))
        #!!!!!
        #emit different Sig for different page

        self.enterRecordingPage_SignalToPage.emit(str(qModelIndex.row()))

    def doubleClicked(self, qModelIndex):
        ("you choosed " + str(qModelIndex.row()))

    def searchSession(self):
        print("search Session")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def print(self):
        print("print recording")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def addSession(self):
        print("add Session")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sort(self):
        sortI = self.comboBox.currentText()
        #print(sortI)
        if sortI == "In Progress":
            self.Process_sessionModel = sessionFrame1_model()
            self.sortSession("In Progress")
            #self.Process_sessionModel.listItemData = ["in progress"]
            #print(self.Process_sessionModel.listItemData)
            self.listView.setModel(self.Process_sessionModel)
        elif sortI == "Future":
            self.Future_sessionModel = sessionFrame1_model()
            self.sortSession("Future")
            #self.Future_sessionModel.listItemData = ["future"]
            self.listView.setModel(self.Future_sessionModel)
        elif sortI == "Past":
            self.Past_sessionModel = sessionFrame1_model()
            self.sortSession("Past")
            #self.Past_sessionModel.listItemData = ["Past"]
            self.listView.setModel(self.Past_sessionModel)
        else:
            self.listView.setModel(ModulePage_Ctr.ModulePage_ctr.sessionModel)
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def sortSession(self,category):
        for session in ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData:
            r = session.split()
            r[2] = r[2].replace('-','')
            r[3] = r[3].replace(':','').replace('.','')
            timer = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
            timer = timer.split()
            timer[0] = timer[0].replace('-','')
            timer[1] = timer[1].replace(':','').replace('.','')
            if category == "In Progress" :
                start = str(int(r[3]) - 1000000)
                if len(start) <= 7 :
                    start = "0" + start
                if r[2] == timer[0] and (start <= timer[1] and str(int(r[3])+2000000) > timer[1]) :
                    self.Process_sessionModel.listItemData.append(session)
            elif category == "Future" :
                if r[2] > timer[0] or (r[2] == timer[0] and r[3] >= timer[1]) :
                    self.Future_sessionModel.listItemData.append(session)
            elif category == "Past" :
                if r[2] < timer[0] or (r[2] == timer[0] and str(int(r[3])+2000000) <= timer[1]) :
                    self.Past_sessionModel.listItemData.append(session)

# test code

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.resize(800, 600)

    frame1 = QFrame(mainWindow)
    frame1.setGeometry(QtCore.QRect(0, 0, 300, 300))

    test = sessionFrame1_View()
    test.refresh()

    test.show()
    CommonHelper.readQSS("resources/qss/sessionFrameView.qss",app)
    sys.exit(app.exec_())