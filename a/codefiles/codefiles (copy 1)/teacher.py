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

def readAllTeachers():
    import sqlite3
    import Filer
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Select ID, Name, Department from Teachers')
    return (c.fetchall())

def deleteTeacher(identity):
    import sqlite3 as sq
    import Filer
    conn = sq.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Delete from Teachers where ID = %s' % identity)
    conn.commit()
    conn.close()
    
def readAllTeachersOfDepartment(department):
    import sqlite3
    import Filer
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Select ID, Name from Teachers where Department = ?',(department,))
    return (c.fetchall())
    
def assignTeacher(courseCode,className,teacherId,teacherName):
    
    import pandas as pd
    teacherDataFrame = pd.DataFrame(data = {'CourseCode':[courseCode],
                                            'ClassName':[className],
                                            'TeacherId':[teacherId],
                                            'TeacherName':[teacherName]})
    
    teacherDataFrame = teacherDataFrame.set_index(['CourseCode','ClassName'])
    teacherDataFrame = readTeacherManagementFile().append(teacherDataFrame)
    
    import os
    import Filer
    p = '%s/%s'%(Filer.DATA_FOLDER, Filer.TEACHER_MANAGEMENT_FILE_NAME)
    if(not os.path.exists(p)):
        print('Path %s does not exists.'%(p))
        input('TODO: Exception...')
    teacherDataFrame.to_csv('%s'%(p))

def makeTeacherManagementFile():
    import pandas as pd
    teacherDataFrame = pd.DataFrame(data = {'CourseCode':[],'ClassName':[],
                                            'TeacherId':[],'TeacherName':[]})
    teacherDataFrame = teacherDataFrame.set_index(['CourseCode','ClassName'])
    import Filer
    teacherDataFrame.to_csv('%s/%s'%(Filer.DATA_FOLDER, Filer.TEACHER_MANAGEMENT_FILE_NAME))
    
def readTeacherManagementFile():
    import pandas as pd
    import os
    import Filer
    p = '%s/%s' % (Filer.DATA_FOLDER, Filer.TEACHER_MANAGEMENT_FILE_NAME)
    if(not os.path.exists(p)):
        print('Path %s does not exists.'%(p))
        input('TODO: Exception...')
        
    teacherDataFrame = pd.read_csv('%s'%(p))
    teacherDataFrame = teacherDataFrame.set_index(['CourseCode','ClassName'])
    return teacherDataFrame

def findTeacherOfSubject(courseCode,className):
    dataF = readTeacherManagementFile()
    return dataF.loc[(courseCode,className),'TeacherName']

