class Course(object):
    
    def __init__(self, code='<Course Code>', name='<Course Name>'):
        self.code = code
        self.name = name

    @classmethod
    def readName(self,code):
        
        import Filer
        import sqlite3 as sq
        con = sq.connect(Filer.DATA_BASE_FILE)
        c = con.cursor()
        query = 'Select Name from Courses where Code = "%s"' % code
        c.execute(query)
        results = c.fetchone()
        if(results != None):
            return results[0]
        else:
            return ''
                   
    @classmethod
    def readCode(self,name):
        
        import Filer
        import sqlite3 as sq
        con = sq.connect(Filer.DATA_BASE_FILE)
        c = con.cursor()
        query = 'Select Code from Courses where Name = "%s"' % name
        c.execute(query)
        results = c.fetchone()
        if(results != None):
            return results[0]
        else:
            return ''
        
    def saveToDatabase(self):
        import Filer
        import sqlite3 as sq
        con = sq.connect(Filer.DATA_BASE_FILE)
        c = con.cursor()
        query = 'Insert into Courses (Code, Name) Values(?,?)'
        c.execute(query,(self.code, self.name))
        con.commit()
        con.close()

    def getName(self):
        return self.name
    def getCode(self):
        return self.code
    def setCode(self, code):
        self.code = code
    def setName(self, name):
        self.name = name
    def setCodeAndName(self, code):
        self.code = code
        self.name = Course.readName(code)
    def setNameAndCode(self, name):
        self.name = name
        self.code = Course.readCode(name)
    
    
def searchCourseNameLike(courseName):
    import Filer
    import sqlite3 as sq
    con = sq.connect(Filer.DATA_BASE_FILE)
    c = con.cursor()
    q = 'Select Name from Courses where Name LIKE "%s%s"' % (courseName,'%')
    c.execute(q)
    r = c.fetchall()
    if(r != None):
        return [r[i][0] for i in range(len(r))]
    else:
        return list('')
    
def searchCourseCodeLike(courseCode):
    import Filer
    import sqlite3 as sq
    con = sq.connect(Filer.DATA_BASE_FILE)
    c = con.cursor()
    q = 'Select Code from Courses where Code LIKE "%s%s"' % (courseCode,'%')
    c.execute(q)
    r = c.fetchall()
    if(r != None):
        return [r[i][0] for i in range(len(r))]
    else:
        return list('')
    

    
