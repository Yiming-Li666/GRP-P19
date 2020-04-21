import pymysql
import numpy as np
import face_recognition

def AddStudent(filePath,studentID,Name):
    # read in photo
    fp = open(filePath, 'rb')
    img = fp.read()
    fp.close()
    # get the feature of the image file
    image = face_recognition.load_image_file(filePath)
    face_encoding = face_recognition.face_encodings(image)[0]
    face_string = face_encoding.tostring()
    print('Img processed!')
    # link to the database
    db = pymysql.connect("localhost", "root", "root1", "test")
    # use cursor() to get operation cursor
    cursor = db.cursor()
    # using sql to insert student table
    sql = "INSERT INTO student (studentId, studentName, studentImg, studentFeature) VALUES (%s, %s, %s, %s);"
    args = (studentID,Name,img,face_string)
    # execute SQL with arguments
    cursor.execute(sql, args)
    # commit to the database
    db.commit()
    # close the cursor
    cursor.close()
    # close the database connection
    db.close()

def Deletestudent(studentId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "DELETE FROM student WHERE studentId = '%s'" % studentId
    cursor.execute(sql)
    print("success")
    db.commit()
    cursor.close()
    db.close()

def AddTeacher(teacherId, teacherName, moduleId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "INSERT INTO teacher (teacherId, teacherName, moduleId) VALUES (%s, %s, %s);"
    args = (teacherId, teacherName, moduleId)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteTeacher(teacherId,moduleId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "DELETE FROM teacher WHERE teacherId = '%s' AND moduleId = '%s'" % (teacherId,moduleId)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddModule(moduleId, moduleName, faculty, school, year):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "INSERT INTO module (moduleId, moduleName, faculty, school, year) VALUES (%s, %s, %s, %s, %s);"
    args = (moduleId, moduleName, faculty, school, year)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteModule(moduleId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "DELETE FROM module WHERE moduleId = '%s'" % moduleId
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddLesson(lessonId, moduleId, studentId, lessonStart, lessonType, venue):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "INSERT INTO lesson (lessonId, moduleId, studentId, lessonStart,lessonType, venue) VALUES (%s, %s, %s, %s, %s, %s);"
    args = (lessonId, moduleId, studentId, lessonStart, lessonType, venue)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteLesson(lessonId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "DELETE FROM lesson WHERE lessonId = '%s'" % lessonId
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddAttendance(moduleId, lessonId, studentId, isAttend):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    if isAttend == 1:
        sql = "INSERT INTO attendance (moduleId, lessonId, studentId, isAttend, attendTime) VALUES (%s, %s, %s, True, NOW());"
    else:
        sql = "INSERT INTO attendance (moduleId, lessonId, studentId, isAttend, attendTime) VALUES (%s, %s, %s, False, NOW());"
    args = (moduleId, lessonId, studentId)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteAttendance(moduleId, lessonId, studentId):
    # may not be used
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "DELETE FROM attendance WHERE moduleId = '%s', lessonId = '%s' AND studentId = '%s'" % (moduleId, lessonId, studentId)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddLogin(userId, userName, userPsw):
    # may not be used
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "INSERT INTO login (userId, userName, userPsw) VALUES (%s, %s, %s);"
    args = (userId, userName, userPsw)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteLogin(userId):
    # may not be used
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "DELETE FROM login WHERE userId = '%s'" % userId
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def CheckLogin(userId,userPsw):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT userPsw FROM login WHERE userId = '%s';" % userId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchone()
    if(data == None):
        return False
    if(data[0] == userPsw):
        return True
    else:
        return False
    cursor.close()
    db.close()

def GetTeacherInfo(teacherId):
    # teacherId, teacherName, moduleId
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM teacher WHERE teacherId = '%s';" % teacherId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def GetSessionInfo(moduleId):
    #lessonId, moduleId, lessonStart, lessonType
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM lesson WHERE moduleId = '%s';" % moduleId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def CheckAdmin(userId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM teacher WHERE teacherId = '%s';" % userId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    if len(data) == 0:
        return True
    else:
        return False

def SearchStudentByName(studentName):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM student WHERE lower(studentName) LIKE '%" + str.lower(studentName) + "%';"
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    #print(data[0][0])
    return data

def SearchStudentById(studentId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM student WHERE studentId = '%s';" % studentId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    #print('Search result:', data)
    return data

def GetStudentInfo(studentId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM attendance WHERE studentId = '%s';" % studentId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data

def GetStudentInfoLesson(studentId, lessonType):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM attendance WHERE attendance.studentId = '%s' AND attendance.moduleId = any(SELECT lesson.moduleId FROM lesson WHERE lesson.lessonId = attendance.lessonId AND lesson.studentId = attendance.studentId AND lesson.lessonType = '%s');" % (studentId,lessonType)
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data

def GetStudentInfoAttend(studentId, isAttend):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM attendance WHERE studentId = '%s' AND isAttend = %d;" % (studentId,isAttend)
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data 

def GetStudentInfoLessonAttend(studentId, lessonType, isAttend):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM attendance WHERE attendance.studentId = '%s' AND isAttend = %d AND attendance.moduleId = any(SELECT lesson.moduleId FROM lesson WHERE lesson.lessonId = attendance.lessonId AND lesson.studentId = attendance.studentId AND lesson.lessonType = '%s');" % (studentId,isAttend,lessonType)
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data 

def GetAttendanceInfo(studentId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT count(*),ModuleId FROM attendance WHERE studentId = '%s' GROUP BY ModuleId HAVING count(*)>=1;" % studentId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data

def GetAttendedInfo(studentId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT count(*),ModuleId FROM attendance WHERE studentId = '%s' AND isAttend = 1 GROUP BY ModuleId HAVING count(*)>=1;" % studentId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data

def GetSessionAttendance(ModuleId, lessonId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM attendance WHERE moduleId = '%s' AND lessonId = '%s';" % (ModuleId, lessonId)
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data

def GetSessionType(moduleId, lessonId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT lessonType FROM lesson WHERE moduleId = '%s' AND lessonId = '%s';" % (moduleId, lessonId)
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    #print(data[0][0])
    cursor.close()
    db.close()
    #print(data)
    return data

def GetSession():
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT DISTINCT moduleId, lessonId FROM attendance;"
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def GetSessionByModule(moduleId):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT DISTINCT moduleId, lessonId FROM attendance WHERE moduleId = '%s';" % moduleId
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def GetSessionByType(lessonType):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT DISTINCT moduleId, lessonId FROM attendance WHERE attendance.moduleId = any(SELECT lesson.moduleId FROM lesson WHERE lesson.lessonId = attendance.lessonId AND lesson.studentId = attendance.studentId AND lesson.lessonType = '%s');" % lessonType
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def GetSessionByBoth(moduleId, lessonType):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    sql = "SELECT DISTINCT moduleId, lessonId FROM attendance WHERE attendance.moduleId = '%s' AND attendance.moduleId = any(SELECT lesson.moduleId FROM lesson WHERE lesson.lessonId = attendance.lessonId AND lesson.studentId = attendance.studentId AND lesson.lessonType = '%s');" % (moduleId, lessonType)
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def select_tb(sql):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def insert_tb(sql, data):
    db = pymysql.connect("localhost", "root", "root1", "test")
    cursor = db.cursor()
    cursor.executemany(sql, data)
    db.commit()
    cursor.close()
    db.close()

#readImage("/Users/liyiming/Desktop/test/test-P19/demo/biden.jpg")
#AddStudent('/Users/liyiming/Desktop/test/demo/test.jpeg','20031525', 'Li Yiming')
#AddStudent('/Users/liyiming/Desktop/GRP/demo/obama.jpg','20001000', 'Ghost')
#SearchStudent('Yiming')
#Deletestudent('20031525')
#AddTeacher('z202020','Paul','COMP1010')
#AddTeacher('test','me','COMP1010')
#DeleteTeacher('admin','COMP1234')
#AddModule('COMP1010', 'test', 'Faculty of Science and Engineering', 'Computer Science', 2020)
#DeleteModule('COMP1010')
'''
AddLesson('lecture1', 'COMP1010', '2010-01-10 10:00:00.00', 'seminer', 'TB-116')
AddLesson('lecture2', 'COMP1010', '2010-02-10 20:00:00.00', 'lecture', 'DB-A05')
AddLesson('lecture3', 'COMP1010', '2010-03-10 06:00:00.00', 'seminer', 'TB-116')
AddLesson('lecture4', 'COMP1010', '2010-04-10 11:00:00.00', 'lecture', 'DB-A05')
AddLesson('lecture5', 'COMP1010', '2010-05-10 12:00:00.00', 'seminer', 'TB-116')
AddLesson('lecture6', 'COMP1010', '2010-06-10 13:00:00.00', 'lecture', 'DB-A05')
AddLesson('lab1', 'COMP1010', '2010-06-10 13:00:00.00', 'lab', 'PMB432')
AddLesson('lab2', 'COMP1010', '2012-06-10 13:00:00.00', 'lab', 'PMB432')
AddLesson('lab3', 'COMP1010', '2013-06-10 13:00:00.00', 'lab', 'PMB432')
AddLesson('lab4', 'COMP1010', '2015-06-10 13:00:00.00', 'lab', 'PMB432')
AddLesson('lab5', 'COMP1010', '2016-06-10 13:00:00.00', 'lab', 'PMB432')
'''
#AddLesson('lab6', 'COMP1010', '20031525', '2020-06-10 13:00:00.00', 'lab', 'PMB432')
#DeleteLesson('lab4')
#DeleteLesson('lecture666')
#AddAttendance('lab1', '20031525', 1)
#AddAttendance('lecture1', '20031521', 0)
#DeleteAttendance('lecture1', '20031525')
#AddLogin('admin', 'GOD', 'admin')
#AddLogin('z202020', 'Paul', 'passward')
#AddLogin('test', 'me', '000')
#CheckLogin('admin','admin')
#DeleteLogin('z202020')
#GetTeacherInfo('z202020')
#GetSessionInfo()
#GetAttendanceInfo('20031525')
#GetSessionType('COMP1010','lab1')
'''
print("============")
print("Done! ")
'''