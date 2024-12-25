import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()

b="drop table if exists people;"
cursor.execute(b)

cursor.execute("""
create table if not exists people(
name text,
age integer
)
""")
cursor.execute("""
insert into people values('ujwal',20),('Nilesh',21),('Ronish',19),('Dikesh',22)
""")
print(f"Total number of changes to the database are {conn.total_changes}")
cursor.execute("""
select * from people
""")
rows=cursor.fetchall()
print(rows)

conn.commit()
conn.close()
