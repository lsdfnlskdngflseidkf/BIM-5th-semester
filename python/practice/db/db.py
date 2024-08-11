import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()

b="drop table if exists people;"
cursor.execute(b)

cursor.execute("""
create table if not exists people(
name text,
age integer
);
""")
cursor.execute("""
insert into people values('ujwal',20),('Nilesh',21),('Ronish',19),('Dikesh',22);
""")
print(f"Total number of changes to the database are {conn.total_changes}")
sel="""
select * from people;
"""
cursor.execute(sel)
rows=cursor.fetchall()
print(rows)

updque="""
update people set age=22 where name='ujwal';
"""
cursor.execute(updque)

rows=cursor.execute(sel)
for i in rows:
    print(i)



#deleting rows
deleter="""
delete from people where age=19;
"""
print("After oofing ronish from the database")
rows=cursor.execute(sel)
for i in rows:
    print(i)
conn.commit()
conn.close()

