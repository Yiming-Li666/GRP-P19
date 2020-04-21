from resources.teacherUIPY.recordedSession_Frame import recordedSession_Frame
from PyQt5.QtWidgets import QFrame
import dbController as db
import globalVar as gl


class recordedSessionFrame_View(QFrame, recordedSession_Frame):

    def __init__(self):
        super(recordedSessionFrame_View, self).__init__()
        self.setupUi(self)

    def update(self):
        lessonId = str(gl.get_value('lessonId'))
        SessionName = str(gl.get_value('moduleId')) + " " + lessonId
        self.teachingSessionName_label.setText(SessionName)
        teacherName = db.GetTeacherInfo(gl.get_value('teacherId'))[0][1]
        self.teacherName_label.setText(teacherName)
        self.sessionName_label.setText(lessonId)
        sql = "SELECT lesson.venue FROM lesson, module WHERE lesson.moduleId = module.moduleId AND lesson.lessonId = '%s'" % lessonId
        venue = db.select_tb(sql)
        self.teachingVenue_label.setText(venue[0][0])
        total = str(len(gl.get_value('attendencelist')) +
                    len(gl.get_value('absentlist')))
        attdence_ratio = str(len(gl.get_value('attendencelist'))) + "/" + total
        self.attendance_label.setText(attdence_ratio)
        absent_list = "Absent Student:\n"
        for absentOne in gl.get_value('absentlist'):
            absent_list = absent_list + "          " + absentOne + "\n"

        if len(gl.get_value('absentlist')) == 0:
            self.label_10.setText("Absent Student:\nCongratulations! No one absent!")
        else:
            self.label_10.setText(absent_list)
