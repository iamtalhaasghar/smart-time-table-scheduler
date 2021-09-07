class Teacher(object):
    
    def __init__(self, identity, name, department):
        self.identity = identity
        self.name = name
        self.department = department
        
    def saveToDatabase(self):
        import sqlite3
        import Filer
        conn = sqlite3.connect(Filer.DATA_BASE_FILE)
        c = conn.cursor()
        c.execute('Insert into Teachers (ID, Name, Department) values(?,?,?)',
                  (self.identity, self.name, self.department))
    
        conn.commit()
        conn.close()

    def getName(self):
        return self.name
    def getDepartment(self):
        return self.department
    def getFacultyId(self):
        return self.identity
    def setName(self, name):
        self.name = name
    def setDepartment(self, department):
        self.department = department
    def setFacultyId(self, identity):
        self.identity = identity
                    

def readAllTeachers():
    import sqlite3
    import Filer
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Select ID, Name, Department from Teachers')
    return (c.fetchall())


def findTeacher(teacherId):
    import sqlite3 as sq
    import Filer
    con = sq.connect(Filer.DATA_BASE_FILE)
    c = con.cursor()
    q = 'Select Name from Teachers where ID = %s' % teacherId
    c.execute(q)
    return c.fetchone()

def deleteTeacher(identity):
    import sqlite3 as sq
    import Filer
    conn = sq.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Delete from Teachers where ID = %s' % identity)
    conn.commit()
    conn.close()

# Reads all teachers of required department    
def readAllTeachersOfDepartment(department):
    import sqlite3
    import Filer
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Select ID, Name from Teachers where Department = ?',(department,))
    r = c.fetchall()
    return ['%s : %s' % (r[i][1], r[i][0]) for i in range(len(r))]
    
def assignTeacher(courseCode,className,teacher):
    import Filer
    import sqlite3 as sq
    import pandas as pd
    con = sq.connect(Filer.MANAGEMENT_FILE)
    c = con.cursor()
    query = 'Insert into Teachers (CourseCode, ClassName, TeacherId) values(?,?,?)'
    c.execute(query,(courseCode, className, teacher.getFacultyId()))
    con.commit()
    con.close()
   
def readTeacherManagementFile():
    import sqlite3 as sq
    import pandas as pd
    import Filer
    con = sq.connect(Filer.MANAGEMENT_FILE)
    teacherDataFrame = pd.read_sql_query('Select * from Teachers', con)
    teacherDataFrame = teacherDataFrame.set_index(['CourseCode','ClassName'])
    teacherDataFrame = teacherDataFrame.drop(columns='Serial')
    return teacherDataFrame

def findTeacherOfSubject(courseCode,className):
    dataF = readTeacherManagementFile()
    tId = dataF.loc[(courseCode,className),'TeacherId']
    result = findTeacher(tId)
    return result[0]

def searchTeachersWithNameLike(tName):
    import Filer
    import sqlite3 as sq
    cn = sq.connect(Filer.DATA_BASE_FILE)
    c = cn.cursor()
    q = 'Select ID, Name from Teachers where Name like "%s%s"' %(tName, '%')
    c.execute(q)
    r = c.fetchall()
    return ['%s : %s' %(r[i][1],r[i][0]) for i in range(len(r))]
    

    
    
