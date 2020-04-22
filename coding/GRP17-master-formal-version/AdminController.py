from AdminModel import adminData_Model
import dbController

class adminController():
    def __init__(self):
        self.adminView = None
        self.accountModel = adminData_Model()
        self.studentModel = adminData_Model()
        self.teacherModel = adminData_Model()
        self.sessionModel = adminData_Model()
        self.attendanceModel = adminData_Model()


    def setView(self, adminView):
        self.adminView = adminView
        self.connectSlot()

    def connectSlot(self):
        self.buildModel()

    def buildModel(self):
        self.setupModel(self.adminView.tableView_4,self.sessionModel)
        self.adminView.tableView.setModel(self.accountModel)
        self.adminView.tableView_2.setModel(self.studentModel)
        self.adminView.tableView_3.setModel(self.teacherModel)
        self.adminView.tableView_4.setModel(self.sessionModel)
        self.adminView.tableView_5.setModel(self.attendanceModel)

    def setupModel(self,tableName,modelName):
        # print(Login_View.userId)
        theData = dbController.GetSession()
        for r in theData:
            modelName.listItemData.append(r[0])
        tableName.setModel(modelName)
        print("hello")

