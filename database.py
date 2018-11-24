import sqlite3 

conn = sqlite3.connect('database.db')
print ("Opened database successfully")
cur = conn.cursor()
cur.execute("DROP TABLE student")
print ("table Delete successfully")
conn.execute('CREATE TABLE student (Sno int, first_name TEXT, last_name TEXT, email TEXT, branch TEXT)')
print ("Table created successfully")

cur.execute("DROP TABLE images")
conn.execute('CREATE TABLE images (id int, img blob)')
print ("Table created successfully")

conn.commit()
conn.close()
