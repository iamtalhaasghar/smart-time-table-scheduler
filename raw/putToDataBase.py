import sqlite3 as sq
c = sq.connect('data.db')
cr = c.cursor()
f = open('teachers.txt')
tId = 1000
for i in f:
    q = 'Insert into Teachers (ID, Name, Department) values("%d","%s","%s")' % (
        tId, i.strip(), 'CS')
    cr.execute(q)
    tId += 1
c.commit()
c.close()
f.close()
