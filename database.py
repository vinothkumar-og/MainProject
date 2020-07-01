import sqlite3

db = sqlite3.connect('Registration')
rs = db.cursor()

rs.execute('''create table Register(name varchar(50), email varchar(100),phone varchar(10), passwd varchar(10))''')
db.commit()
#Add data in Table
rs.execute('''insert into Register values('vinoth','vinoth@gmail.com','966732191','vinoth1234#')''')
db.commit()
rs.execute('select * from Register')
for i in rs:
	print(i)
