from urllib.request import urlopen
d = urlopen('https://my.kfueit.edu.pk/users/testtable')
'''
f = open('data.html','bw')
f.write(d.read())
f.close()
'''
from bs4 import BeautifulSoup as bs
s = bs(d.read(), 'html.parser')
t = s.find(id='teacher')
c = s.find(id='class')
r = s.find(id='room')

t = t.find_all('option')
c = c.find_all('option')
r = r.find_all('option')

f = open('teachers.txt','w')
for i in t[1:]:
    f.write((i.string)+"\n")
f.close()

f = open('class.txt','w')
for i in c[1:]:
    f.write((i.string)+"\n")
f.close()


f = open('room.txt','w')
for i in r[1:]:
    f.write((i.string)+"\n")
f.close()
