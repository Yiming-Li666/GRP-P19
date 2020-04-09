from faceRecognition_function import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import dbController
from resources.teacherUIPY.recording_totalframe import recording_totalframe
from recordingFrame_ctr import recordingFrame_ctr
import cv2


class recordingFrame_View(QFrame, recording_totalframe):
    start_Signal = pyqtSignal()
    stop_Signal = pyqtSignal()

    def __init__(self):
        super(recordingFrame_View, self).__init__()
        self.setupUi(self)

        # self.attendance_progressBar.setValue(25)
        self.attendance_progressBar.setProperty("value", 0)

        # connect with ctr
        self.recordingFrameCtr = recordingFrame_ctr()
        self.recordingFrameCtr.setCtr(self)

        # 初始化摄像头相关
        self.timer_camera = QTimer()  # 初始化定时器
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.CAM_NUM = 0
        self.slot_init()

        # 初始化签到相关
        # bdcontroller应该新增根据lesson的学生查询,现在的查询是写死的，获取的给到data
        # 开始
        studentId = 20031525
        #sql = "SELECT * FROM student WHERE studentId = '%s';" % studentId
        data = dbController.SearchStudentById(studentId)
        print("Initail")
        # 结束

        # 初始化识别相关
        self.known_face_encodings_list = []
        self.known_face_names_list = []
        for index in range(len(data)):
            known_face_names = data[index][1]
            known_face_encodings = data[index][4]
            numArr = np.fromstring(known_face_encodings, float)
            student_tuple = (numArr)
            self.known_face_encodings_list.append(student_tuple)
            self.known_face_names_list.append(known_face_names)
        self.is_attendance = [0] * len(self.known_face_names_list)
        self.attdence_buffer = []
        self.process_this_frame = True
        print("Initail2")
        # 初始化UI识别相关
        self.attendceRatio_label.setText("0/"+str(len(self.known_face_names_list)))

    def slot_init(self): 
        self.timer_camera.timeout.connect(self.show_camera)
        # 信号和槽连接
        self.stop_pushButton.clicked.connect(self.stop)
        self.start_pushButton.clicked.connect(self.start)
        print("slot")
        # self.succeed_pushbutton.clicked.connect(
        #     self.recordingFrameCtr.successRecoding)
        # self.fail_pushButton.clicked.connect(
        #     self.recordingFrameCtr.failRecoding)

    def show_camera(self):
        print("show camera")
        name_buffer, self.is_attendance = recognition(
                                         self.known_face_encodings_list,
                                         self.known_face_names_list,
                                         self.is_attendance,
                                         self.process_this_frame, self)
        new_attendance = [i for i in name_buffer if i not in self.attdence_buffer]
        self.attdence_buffer.extend(new_attendance)
        self.update_info()

    def update_info(self):
        print("update")
        if len(self.attdence_buffer) != 0:
            self.studentInfo_label.setText(self.attdence_buffer[0])
        else:
            self.studentInfo_label.setText('No one has attendant')
        print(self.attdence_buffer)
    '''
    def startRecording(self):
        print("start")
        #self.attendance_progressBar.setValue(5)
        #self.stop_pushButton.setText("1234")
        self.start_Signal.emit()

    def pauseRecording(self):
        print("stop")
        #self.attendance_progressBar.setValue(5)
        #self.stop_pushButton.setText("1234")
        self.stop_Signal.emit()
    '''
    # 打开摄像头
    def openCamera(self):
        print("open camera")
        flag = self.cap.open(self.CAM_NUM)
        print(flag)
        if flag is False:
            msg = QMessageBox.Warning(self, u'Warning',
                                      u'Please check the connection between computer and camera',
                                      buttons=QMessageBox.Ok,
                                      defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30)
            self.start_pushButton.setText('STOP')

        # 关闭摄像头
    def closeCamera(self):
        print("close camera")
        self.timer_camera.stop()
        self.cap.release()
        self.camera_label.clear()
        self.start_pushButton.setText('START')

    # for hide session window
    def setSessionWindow(self, Session):
        self.sessionWindow = Session

    def start(self):
        print("start")
        self.start_Signal.emit()

    def stop(self):
        print("stop")
        #self.attendance_progressBar.setValue(5)
        #self.stop_pushButton.setText("1234")
        self.stop_Signal.emit()