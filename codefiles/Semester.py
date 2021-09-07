class Semester(object):

    def __init__(self, department='<Department Name>',
                 degree='<Degree>', className='<Class Name>'):
        
        self.department = department
        self.degree = degree
        self.className = className
        
        import pandas as pd
        self.courses = pd.DataFrame({'CourseCode':[],'Subjects':[],'CH':[],'CM':[]})

    def setDepartment(self, depart):
        self.department = depart
    def setClassName(self, className):
        self.className = className
    def setDegree(self, degree):
        self.degree = degree

    def getDepartment(self):
        return self.department
    def getClassName(self):
        return self.className
    def getDegree(self):
        return self.degree

    def getCoursesString(self):
        return str(self.courses)
        
    def addCourse(self,course, oneCreditHour, creditHour):

        from course import Course
        import pandas as pd
        contactMins = (creditHour * oneCreditHour) * 60
        data = {'CourseCode':[course.getCode()],
                'Subjects':[course.getName()], 'CH':[creditHour],'CM':[contactMins]}
        subject = pd.DataFrame(data)
        #print('-----------------')
        #print(self.courses)
        self.courses = self.courses.append(subject, ignore_index=True)
        #print(self.courses)
        #print('-----------------')

    def saveToDatabase(self):
        import sqlite3 as sq
        import Filer
        path = '%s/%s.db' % (
            Filer.createDepartmentFolder(self.getDepartment()), self.getDegree())
        c = sq.connect(path)
        self.courses.to_sql(self.getClassName(),c)
        c.commit()
        c.close()
        
    # reads class from database and converts it into dataframe
    def readClass(self):
        import sqlite3 as sq
        import Filer
        path = '%s/%s.db' % (
            Filer.createDepartmentFolder(self.getDepartment()), self.getDegree())

        con = sq.connect(path)

        import pandas as pd
        query = 'Select * from %s' % self.getClassName()
        data = pd.read_sql_query(query, con)
        data = data.set_index('CourseCode')
        data = data.drop(columns=['index'])
        return data
    
def classesOfProgram(department, program):
    import Filer
    import sqlite3 as sq
    path = '%s/%s/%s.db' % (Filer.DATA_FOLDER, department, program)
    con = sq.connect(path)
    c = con.cursor()
    c.execute("Select name from sqlite_master where type = 'table'")
    r = c.fetchall()
    result = [r[i][0] for i in range(len(r))]
    return result

