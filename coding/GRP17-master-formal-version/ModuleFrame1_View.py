from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QApplication
from resources.teacherUIPY.basicStructure_frame1 import Ui_Frame
import sys
from CommonHelper import CommonHelper
import ModulePage_View
import Login_ctr
import dbController
import ModulePage_Ctr
#test
from ModuleFrame1_Model import moduleFrame1_Model
from ModuleFrame_Delegate import moduleFrame_Deletagte


class moduleFrame1_view(QFrame, Ui_Frame):

    # send signal to module page
    enterSessionPage_SignalToPage = pyqtSignal()
    DateTime = []

    def __init__(self):
        # setup UI
        super(moduleFrame1_view, self).__init__()
        self.setupUi(self)

    def refresh(self):
        self.frameName_TBS.setText("Module")
        self.search_lineEdit.hide()
        self.search_toolButton.hide()
        self.addButton.hide()
        self.listView.clicked.connect(self.singleClicked)
        self.listView.doubleClicked.connect(self.goSession)

    def goSession(self, qModelIndex):
        # TODO: jump to the page
        # print("go to " + str(qModelIndex.row()))
        # get all the session to load session list
        self.sortSessionList(qModelIndex)
        self.enterSessionPage_SignalToPage.emit()

    # may not to be used
    def singleClicked(self, qModelIndex):
        print("you choosed " + str(qModelIndex.row()))

    def sort(self):
        print("sort")

    def sortSessionList(self,qModelIndex):
        #print("in")
        moduleId = ModulePage_View.modulePage_view.moduleModel.listItemData[qModelIndex.row()]
        sessionInfo = dbController.GetSessionInfo(moduleId)
        ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData = []
        if len(self.DateTime) != 0:
            self.DateTime = []
        for r in sessionInfo:
            # current = self.DateTime[len(self.DateTime)]
            current = int(r[2].replace(' ','').replace('-','').replace(':','').replace('.',''))
            self.DateTime.append(current)
            self.DateTime.sort()
            # print(self.DateTime)
            # only one element in list datatime, no element in listItemData
            if len(self.DateTime) == 1:
                #print("1")
                ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData.append(r[0]+ "  " + r[1] + "  " + r[2] + "  -  " + r[3])
            else:
                # 0 to len
                #print(str(self.DateTime[len(self.DateTime)-1]) + "  " + str(current))
                for inner in range(len(self.DateTime)):
                    # if current is the greatest
                    if self.DateTime[len(self.DateTime)-1] <= current:
                        #print('great   ' +str(self.DateTime[len(self.DateTime)-2])+"   "+str(current))
                        ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData.append(r[0]+ "  " + r[1] + "  " + r[2] + "  -  " + r[3])
                        break
                    # if the current is smaller than this one
                    if self.DateTime[inner] > current:
                        #print('insert  '+ str(current))
                        ModulePage_Ctr.ModulePage_ctr.sessionModel.listItemData.insert(inner-1,r[0]+ "  " + r[1] + "  " + r[2] + "  -  " + r[3])
                        break
                    else: 
                        continue

# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    test = moduleFrame1_view()
    delegate = moduleFrame_Deletagte()
    model = moduleFrame1_Model()
    test.listView.setModel(model)
    test.listView.setItemDelegateForRow(0,delegate)
    test.show()
    CommonHelper.readQSS("resources/qss/Module.qss",app)
    sys.exit(app.exec_())