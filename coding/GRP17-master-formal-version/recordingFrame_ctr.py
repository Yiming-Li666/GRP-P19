from dbController import AddAttendance
import sessionFrame1_View


class recordingFrame_ctr():

    def setCtr(self, recordingFrameView):
        self.recordingFrameView = recordingFrameView
        self.connectSlot()

    def connectSlot(self):
        self.recordingFrameView.start_Signal.connect(self.startRecording)
        self.recordingFrameView.pause_Signal.connect(self.pauseRecoding)
        self.recordingFrameView.suces_Signal.connect(self.successRecoding)
        self.recordingFrameView.fail_Signal.connect(self.failRecoding)

    def startRecording(self):
        if self.recordingFrameView.is_Recording is False:
            # 打开摄像头并显示图像信息
            self.recordingFrameView.openCamera()
        else:
            # 关闭摄像头并清空显示信息
            self.recordingFrameView.closeCamera()

    def pauseRecoding(self):
        if self.recordingFrameView.is_Recording is True:
            if self.recordingFrameView.timer_camera.isActive() is False:
                # 继续record
                self.recordingFrameView.contine_recording()
            else:
                # 截图并停止record
                self.recordingFrameView.pause_recording()

    def successRecoding(self):
        if len(self.recordingFrameView.attdence_buffer) != 0:
            self.recordingFrameView.confirm_attendence.append(
                self.recordingFrameView.attdence_buffer[0])
            # 这个是写入成功签到
            moduleId = sessionFrame1_View.sessionFrame1_View.info[1]
            lessonId = sessionFrame1_View.sessionFrame1_View.info[0]
            AddAttendance(moduleId, lessonId, self.recordingFrameView.attdence_buffer[0], 1)
            del self.recordingFrameView.attdence_buffer[0]
        self.recordingFrameView.update_progress_ui()

    def failRecoding(self):
        if len(self.recordingFrameView.attdence_buffer) != 0:
            del self.recordingFrameView.attdence_buffer[0]
        self.recordingFrameView.update_info()
