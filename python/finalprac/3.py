import sqlite3
connection=sqlite3.connect('test.db')
cursor=connection.cursor()
query="""drop table if exists testing;"""
cursor.execute(query)
q2="""create table testing(roll int PRIMARY KEY,name text,address text);"""
cursor.execute(q2)
inq="""insert into testing values(1,'Ujwal Parajuli','Sallaghari'),(2,'Shiva Raj Poudel','Sinamangal'),(3,'Aakash Adhikari','Dharan');"""
cursor.execute(inq)
upq="""update testing set address='Shankhamul' where roll=3; """
cursor.execute(upq)
get="""select * from testing"""
cursor.execute(get)
this=cursor.fetchall()
print("Retriving all records from the testing table before deleting 2")
for that in this:
    print(that)
print("\n\n\n\n\n")
deq="""delete from testing where roll=2"""
cursor.execute(get)
print("After deliting one record")
this=cursor.fetchall()
for that in this:
    print(that)
