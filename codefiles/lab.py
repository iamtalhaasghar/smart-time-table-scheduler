#creates labs for a given department
def createDepartmentLabs(department,count):

    import Filer
    import sqlite3
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    for i in range(1,count+1):
        c.execute('Insert into Labs (Name, Department) values (?, ?)',
                  (('%s LAB%d'%(department,i)), department))

    conn.commit()
    conn.close()
    
#reads all labs of required department
def readAllLabsOfDepartment(department):

    import Filer
    import sqlite3

    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Select Name from Labs where Department = ?', (department,))
    return c.fetchall()

def readAllLabs():

    import Filer
    import sqlite3

    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    c.execute('Select Name, Department from Labs')
    return c.fetchall()


def assignLab(courseCode, className, labName):
    import Filer
    import sqlite3 as sq
    con = sq.connect(Filer.MANAGEMENT_FILE)
    c = con.cursor()
    query = ('Insert into Labs (CourseCode, LabName, ClassName) values(?,?,?)')
    c.execute(query, (courseCode,labName, className))
    con.commit()
    con.close()
    
def readLabManagementFile():
    import sqlite3 as sq
    import Filer
    import pandas as pd
    con = sq.connect(Filer.MANAGEMENT_FILE)
    labDataFrame = pd.read_sql_query('Select * from Labs', con)
    labDataFrame = labDataFrame.set_index(['CourseCode','ClassName'])
    labDataFrame = labDataFrame.drop(columns='Serial')
    return labDataFrame

def findLabOfSubject(courseCode, className):
    dataF = readLabManagementFile()
    return dataF.loc[(courseCode, className) ,'LabName']

