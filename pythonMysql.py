import pymysql

db = pymysql.connect("localhost",'root','kumanxuan@gzitcast','xingzheng',charset='utf8')

mysql = db.cursor(pymysql.cursors.DictCursor)

sql = "select * from classroom"

def ifMain():
    if  __name__ != "__main__":
        print("I am not main,send by pythonMysql")

def testMysql():
   try:
     mysql.execute(sql)
     result = mysql.fetchall()
     for x in result:
       print(x)
     mysql.close()
   except:
    print("error")

   #mysql.close()
ifMain()
#xx
#testMysql()

