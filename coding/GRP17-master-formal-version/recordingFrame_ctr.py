
class recordingFrame_ctr():

    def setCtr(self, recordingFrameView):
        self.recordingFrameView = recordingFrameView
        self.connectSlot()

    def connectSlot(self):
        self.recordingFrameView.start_Signal.connect(self.startRecording)
        self.recordingFrameView.stop_Signal.connect(self.pauseRecording)

    def startRecording(self):
        if self.recordingFrameView.timer_camera.isActive() is False:
            # 打开摄像头并显示图像信息
            print("open camera")
            self.recordingFrameView.openCamera()
        else:
            print("close camera")
            # 关闭摄像头并清空显示信息
            self.recordingFrameView.closeCamera()

    def pauseRecording(self):
        print("pause")
        self.recordingFrameView.attendceRatio_label.setText("5/100")
        self.recordingFrameView.attendance_progressBar.setValue(5)
        self.recordingFrameView.stop_pushButton.setText("1234")
        # if self.recordingFrameView.timer_camera.isActive() is not False:
        #     # 截图并停止record
        #self.recordingFrameView.pause_recording()

    # def successRecoding(self):


    # def failRecoding(self):
