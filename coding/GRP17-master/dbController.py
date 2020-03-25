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
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
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

def DeleteStudent(studentId):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "DELETE FROM student WHERE studentId = '%s'" % studentId
    cursor.execute(sql)
    print("success")
    db.commit()
    cursor.close()
    db.close()

def AddTeacher(teacherId, teacherName, moduleId):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "INSERT INTO teacher (teacherId, teacherName, moduleId) VALUES (%s, %s, %s);"
    args = (teacherId, teacherName, moduleId)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteTeacher(teacherId):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "DELETE FROM teacher WHERE teacherId = '%s'" % teacherId
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddModule(moduleId, moduleName, studentId):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "INSERT INTO module (moduleId, moduleName, studentId) VALUES (%s, %s, %s);"
    args = (moduleId, moduleName, studentId)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteModule(moduleId):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "DELETE FROM module WHERE moduleId = '%s'" % moduleId
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddLesson(lessonId, moduleId, lessonStart, lessonType):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "INSERT INTO lesson (lessonId, moduleId, lessonStart,lessonType) VALUES (%s, %s, NOW(), %s);"
    args = (lessonId, moduleId, lessonType)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteLesson(lessonId):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "DELETE FROM lesson WHERE lessonId = '%s'" % lessonId
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddAttendance(lessonId, studentId, isAttend):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    if isAttend == 1:
        sql = "INSERT INTO attendance (lessonId, studentId, isAttend, attendTime) VALUES (%s, %s, True, NOW());"
    else:
        sql = "INSERT INTO attendance (lessonId, studentId, isAttend, attendTime) VALUES (%s, %s, False, NOW());"
    args = (lessonId, studentId)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteAttendance(lessonId, studentId):
    # may not be used
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "DELETE FROM attendance WHERE lessonId = '%s' AND studentId = '%s'" % (lessonId, studentId)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def AddLogin(userId, userName, userPsw):
    # may not be used
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "INSERT INTO login (userId, userName, userPsw) VALUES (%s, %s, %s);"
    args = (userId, userName, userPsw)
    cursor.execute(sql, args)
    db.commit()
    cursor.close()
    db.close()

def DeleteLogin(userId):
    # may not be used
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
    cursor = db.cursor()
    sql = "DELETE FROM login WHERE userId = '%s'" % userId
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

def CheckLogin(userId,userPsw):
    db = pymysql.connect("localhost", "root", "JasonLi05@", "test")
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

#readImage("/Users/liyiming/Desktop/GRP/GRP-P19/demo/biden.jpg")
#AddStudent('/Users/liyiming/Desktop/GRP/GRP-P19/demo/biden.jpg','20031525', 'Li Yiming')
#DeleteStudent('20031525')
#AddTeacher('z202020','Paul','COMP1010')
#DeleteTeacher('z202020')
#AddModule('COMP1010', 'Computer Science', '20031525')
#DeleteModule('COMP1010')
#AddLesson('lecture1', 'COMP1010', '2019-03-05 01:53:55.63', 'lab')
#DeleteLesson('lecture1')
#AddAttendance('lecture1', '20031525', 1)
#AddAttendance('lecture1', '20031521', 0)
#DeleteAttendance('lecture1', '20031525')
#AddLogin('z202020', 'Paul', 'passward')
#AddLogin('admin', 'Li', 'admin')
#CheckLogin('admin','admin')
#DeleteLogin('z202020')
'''
print("============")
print("Done! ")
'''