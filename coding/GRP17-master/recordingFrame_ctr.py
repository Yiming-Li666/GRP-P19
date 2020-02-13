
class recordingFrame_ctr():
    
    def setCtr(self, recordingFrameView):
        self.recordingFrameView = recordingFrameView
        self.connectSlot()
        
    def connectSlot(self):
        self.recordingFrameView.start_Signal.connect(self.startRecording)
        
    def startRecording(self):
        print("recording..........")
        '''
            slot document goes here
        '''