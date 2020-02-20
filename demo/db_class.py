import mysql.connector


class database:
    def __init__(self, ip, port, user, psw, dbname):
        try:
            con = mysql.connector.connect(
                host=ip,
                user=user,
                password=psw,
                port=port,
                database=dbname,
                charset='utf8',
                buffered=True
            )
            print('Database Connected!')
            self.con = con  # used in multi-case
        except mysql.connector.Error as e:
            print('Fail in connect', str(e))

    def create_tb(self, sql):
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)
            print('Table created!')
        except mysql.connector.Error as e:
            print('Fail in table created', str(e))
        finally:
            cursor.close()

    def insert_tb(self, sql, data):
        try:
            cursor = self.con.cursor()
            cursor.executemany(sql, data)
            self.con.commit()
            print('Insert successfully!')
        except mysql.connector.Error as e:
            self.con.rollback()
            print('Fail in Insert', str(e))
        cursor.close()

    def select_tb(self, sql):
        try:
            cursor = self.con.cursor(dictionary=True)
            cursor.execute(sql)
            result1 = cursor.fetchall()
            print('Search result:', result1)
        except mysql.connector.Error as e:
            print('Fail in search', str(e))
        finally:
            cursor.close()

    def select_tb_one(self, sql):
        try:
            cursor = self.con.cursor(dictionary=True)
            cursor.execute(sql)
            result2 = cursor.fetchone()
            print('Search one result:', result2)
        except mysql.connector.Error as e:
            print('Fail in search', str(e))
        finally:
            cursor.close()

    def select_tb_many(self, sql, count):
        try:
            cursor = self.con.cursor(dictionary=True)
            cursor.execute(sql)
            result3 = cursor.fetchmany(count)
            print('Search result:', result3)
        except mysql.connector.Error as e:
            print('Fail in search', str(e))
        finally:
            cursor.close()


# 连接数据库
db = database('localhost', '3306', 'root', 'lmclmc', 'test')
# 创建表
sql_create = 'create table student_5(id int(10) not null auto_increment, name varchar(10) default null, age int(3) default null, primary key (id))engine=myisam default charset=utf8;'
db.create_tb(sql_create)
# #插入数据
sql_insert = 'insert into student_5(id,name,age) values(%s,%s,%s)'
data_insert = [(1, 'guozhen', 18), (2, 'ss', 19), (3, 'alen', 30)]
db.insert_tb(sql_insert, data_insert)
# 查询全部数据
sql_select = 'select * from student_5'
db.select_tb(sql_select)
# 查询多条数据
db.select_tb_many(sql_select, 2)
# 查询一条数据
db.select_tb_one(sql_select)
# 关闭数据库连接
db.con.close()
