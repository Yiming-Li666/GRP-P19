#!/usr/bin/python3

import pymysql
import numpy as np
import face_recognition

# 获得照片
fp = open("five.jpg", 'rb')
img = fp.read()
fp.close()

# 获得特征文件
lmc_image = face_recognition.load_image_file("five.jpg")
five_face_encoding = face_recognition.face_encodings(lmc_image)[0]
fice_face_string = five_face_encoding.tostring()

print('Img processed!')

# 打开数据库连接
db = pymysql.connect("localhost", "root", "lmclmc", "grp")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "INSERT INTO student (studentId, studentName, studentImg, studentFeature) VALUES (%s, %s, %s, %s);"
args = ('20031624', 'Li Mingchen', img, fice_face_string)

# 执行SQL语句
cursor.execute(sql, args)
# 提交至数据库
db.commit()
# 关闭游标
cursor.close()

# 关闭数据库连接
db.close()

print("============")
print("Done! ")
