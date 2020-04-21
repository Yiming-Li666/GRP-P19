from faceRecognition_function import recognition
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from dbController import select_tb, AddAttendance
from resources.teacherUIPY.recording_totalframe import recording_totalframe
from recordingFrame_ctr import recordingFrame_ctr
import globalVar as gl
import numpy as np
import Login_View
import sessionFrame1_View
import cv2


class recordingFrame_View(QFrame, recording_totalframe):
    start_Signal = pyqtSignal()
    pause_Signal = pyqtSignal()
    suces_Signal = pyqtSignal()
    fail_Signal = pyqtSignal()
    is_Recording = False
    confirm_attendence = []

    def __init__(self, mainwindow):
        super(recordingFrame_View, self).__init__()
        self.setupUi(self)

        self.mainwindow = mainwindow

        # connect with ctr
        self.recordingFrameCtr = recordingFrame_ctr()
        self.recordingFrameCtr.setCtr(self)

        # 初始化摄像头相关
        self.timer_camera = QTimer()  # 初始化定时器
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.CAM_NUM = 0
        self.slot_init()

    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        # 信号和槽连接
        self.stop_pushButton.clicked.connect(
            self.recordingFrameCtr.pauseRecoding)

        self.start_pushButton.clicked.connect(
            self.recordingFrameCtr.startRecording)

        self.succeed_pushbutton.clicked.connect(
            self.recordingFrameCtr.successRecoding)
        self.fail_pushButton.clicked.connect(
            self.recordingFrameCtr.failRecoding)

    def show_camera(self):
        name_buffer, self.is_attendance = recognition(
            self.known_face_encodings_list,
            self.ids_list,
            self.is_attendance,
            self.process_this_frame, self)
        new_attendance = [
            i for i in name_buffer if i not in list(set(self.confirm_attendence).union(set(self.attdence_buffer)))]
        self.attdence_buffer.extend(new_attendance)
        self.update_info()

    def update_info(self):
        if len(self.attdence_buffer) != 0:
            index = self.ids_list.index(self.attdence_buffer[0])
            self.studentInfo_label.setText(self.student_names_list[index])
        else:
            self.studentInfo_label.setText('No one has attendant')
        print(self.attdence_buffer)

    def update_progress_ui(self):
        progressBar_value = len(self.confirm_attendence) / len(self.ids_list)
        self.attendance_progressBar.setProperty("value", progressBar_value*100)
        self.attendceRatio_label.setText(
            str(len(self.confirm_attendence))+"/"+str(len(self.ids_list)))
        if progressBar_value == 1:
            self.is_Recording = False
            self.timer_camera.stop()
            self.cap.release()
            self.end_recording()

    def end_recording(self):
        # 记录所有未签到的学生
        not_attendance = [
            i for i in self.ids_list if i not in self.confirm_attendence]
        for not_attendant_student in not_attendance:
            moduleId = sessionFrame1_View.sessionFrame1_View.info[1]
            lessonId = sessionFrame1_View.sessionFrame1_View.info[0]
            AddAttendance(moduleId, lessonId, not_attendant_student, 0)

        gl.set_value('teacherId', Login_View.userId)
        gl.set_value('lessonId', sessionFrame1_View.sessionFrame1_View.info[0])
        gl.set_value('moduleId', sessionFrame1_View.sessionFrame1_View.info[1])
        gl.set_value('attendencelist', self.confirm_attendence)
        gl.set_value('absentlist', not_attendance)

        # 跳出前置空
        self.attdence_buffer = []
        self.process_this_frame = True
        self.is_Recording = False
        self.confirm_attendence = []
        self.known_face_encodings_list = []
        self.ids_list = []
        self.student_names_list = []

        # 跳转
        gl.get_value('RecordedPage').update()
        self.mainwindow.stackedWidget.setCurrentIndex(7)

    def pause_recording(self):
        self.stop_pushButton.setText("Continue")
        self.timer_camera.stop()
        self.cap.release()

    def contine_recording(self):
        flag = self.cap.open(self.CAM_NUM)
        if flag is False:
            msg = QMessageBox.Warning(self, u'Warning',
                                      u'Please check the connection between computer and camera',
                                      buttons=QMessageBox.Ok,
                                      defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30)
            self.stop_pushButton.setText("Pause")

    # 打开摄像头
    def openCamera(self):
        self.is_Recording = True
        flag = self.cap.open(self.CAM_NUM)
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
        self.is_Recording = False
        self.timer_camera.stop()
        self.cap.release()
        self.camera_label.clear()
        self.start_pushButton.setText('START')
        self.stop_pushButton.setText('Pause')
        self.end_recording()

    # for hide session window
    def setSessionWindow(self, Session):
        self.sessionWindow = Session

    def startRecording(self):
        if self.recordingFrameView.timer_camera.isActive() is False:
            # 打开摄像头并显示图像信息
            self.recordingFrameView.openCamera()
        else:
            # 关闭摄像头并清空显示信息
            self.recordingFrameView.closeCamera()

    def start(self):
        self.start_Signal.emit()

    def pause_singnal(self):
        self.pause_Signal.emit()

    def suces_signal(self):
        self.suces_Signal.emit()

    def fail_signal(self):
        self.fail_Signal.emit()

    def init(self):

        # print(sessionFrame1_View.sessionFrame1_View.info[0])

        # 初始化本页面各项数据
        lessonId = sessionFrame1_View.sessionFrame1_View.info[0]
        moduleId = sessionFrame1_View.sessionFrame1_View.info[1]
        sql = "SELECT student.studentId, studentName, studentFeature FROM student, lesson WHERE student.studentId=lesson.studentId AND lessonId = '%s' AND moduleId = '%s';" % (
            lessonId, moduleId)
        data = select_tb(sql)

        # 初始化识别相关
        self.known_face_encodings_list = []
        self.ids_list = []
        self.student_names_list = []
        for index in range(len(data)):
            ids = data[index][0]
            student_names = data[index][1]
            known_face_encodings = data[index][2]
            numArr = np.fromstring(known_face_encodings, float)
            student_tuple = (numArr)
            self.student_names_list.append(student_names)
            self.known_face_encodings_list.append(student_tuple)
            self.ids_list.append(ids)
        self.is_attendance = [0] * len(self.ids_list)
        self.attdence_buffer = []
        self.process_this_frame = True

        # 初始化UI相关
        self.attendceRatio_label.setText(
            "0/"+str(len(self.ids_list)))
        self.attendance_progressBar.setValue(0)
        sql = "SELECT moduleName FROM module WHERE moduleId = '%s'" % moduleId
        modulename = select_tb(sql)
        show_modulename = "ModuleName: " + moduleId + " " + modulename[0][0]
        self.frameName_TBS.setText(show_modulename)
        self.camera_label.setText('')
        self.studentInfo_label.setText('')
