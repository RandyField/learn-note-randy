import pymysql

#打开数据库连接
db=pymysql.connect("localhost","root","a287572291","school")

#使用 cursor() 方法创建一个游标对象 cursor
cursor=db.cursor()

#使用execute()方法执行SQL查询
cursor.execute("select * from course;")

i=cursor.rowcount

data=cursor.fetchall()

results=cursor._rows
for row in data:
    courseid=row[0]
    credits=row[1]
    title=row[2]

    #打印结果
    print("courseid=%s,credits=%s,title=%s"%\
    (courseid,credits,title))

# #使用 fetchone()方法获取单条数据
# data=cursor.fetchall()

#SQL插入语句
sql="""INSERT INTO course
    (courseid,credits,title)
    VALUES('4042','4','math')"""

try:
    #执行sql语句
    cursor.execute(sql);

    #提交到数据库执行
    db.commit();
except Exception as e:
    db.rollback();

cursor.execute("select * from course;")
data=cursor.fetchall()

print("-------------插入后的数据------------------")
for row in data:
    courseid=row[0]
    credits=row[1]
    title=row[2]

    #打印结果
    print("courseid=%s,credits=%s,title=%s"%\
    (courseid,credits,title))

#关闭数据库
db.close()