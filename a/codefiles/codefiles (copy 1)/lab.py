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
    import pandas as pd
    labDataFrame = pd.DataFrame(data = {'CourseCode':[courseCode],
                                        'ClassName':[className],
                                        'LabName':[labName]})
    labDataFrame = labDataFrame.set_index(['CourseCode','ClassName'])
    labDataFrame = readLabManagementFile().append(labDataFrame)
    import Filer
    labDataFrame.to_csv('%s/%s'%(Filer.DATA_FOLDER, Filer.LAB_MANAGEMENT_FILE_NAME))

def makeLabManagementFile():
    import pandas as pd
    labDataFrame = pd.DataFrame(data = {'CourseCode':[], 'ClassName':[], 'LabName':[]})
    labDataFrame = labDataFrame.set_index(['CourseCode','ClassName'])
    import Filer
    labDataFrame.to_csv('%s/%s'%(Filer.DATA_FOLDER, Filer.LAB_MANAGEMENT_FILE_NAME))
    
def readLabManagementFile():
    import os
    import Filer
    p = '%s/%s' % (Filer.DATA_FOLDER, Filer.LAB_MANAGEMENT_FILE_NAME)
    if(not os.path.exists(p)):
        print('Path %s does not exists')
        input('TODO: Exception')
    import pandas as pd
    labDataFrame = pd.read_csv('%s'%(p))
    labDataFrame = labDataFrame.set_index(['CourseCode','ClassName'])
    return labDataFrame

def findLabOfSubject(courseCode, className):
    dataF = readLabManagementFile()
    return dataF.loc[(courseCode, className) ,'LabName']

