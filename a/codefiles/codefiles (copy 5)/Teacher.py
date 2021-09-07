def addTeacher(teacherId,teacherName):
    
    import Filer
    folder = Filer.createFolder('data')
    path = '%s/%s.csv' % (folder,'Teachers')
    
    import pandas as pd
    import os
    
    if(os.path.exists(path)):
        #print('File present')
        teacherData = readAllTeachers()
        teacherData = teacherData.T
        teacherData.insert(len(teacherData.columns),teacherId,teacherName)
        teacherData = teacherData.T
    else:
        teacherData = pd.DataFrame({'Id':[teacherId],'Name':[teacherName]})
        teacherData = teacherData.set_index('Id')
        makeTeacherManagementFile()
    #print(teacherData)    
    teacherData.to_csv(path)    

def readAllTeachers():
    import os
    p = os.getcwd() + '/data/Teachers.csv'
    if(not os.path.exists(p)):
        print('Path %s does not exists'%(p))
        input('TODO: Exception ...')
    import pandas as pd
    data = pd.read_csv('%s'%(p))
    data = data.set_index('Id')
    return data

def assignTeacher(courseCode,className,teacherId,teacherName):
    
    import pandas as pd
    teacherDataFrame = pd.DataFrame(data = {'CourseCode':[courseCode],
                                            'ClassName':[className],
                                            'TeacherId':[teacherId],
                                            'TeacherName':[teacherName]})
    
    teacherDataFrame = teacherDataFrame.set_index(['CourseCode','ClassName'])
    teacherDataFrame = readTeacherManagementFile().append(teacherDataFrame)
    
    import os
    p = os.getcwd() + '/data/TeacherManagement.csv'
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
    folder = Filer.createFolder('data')
    teacherDataFrame.to_csv('%s/%s.csv'%(folder,'TeacherManagement'))
    
def readTeacherManagementFile():
    import pandas as pd
    import os
    p = os.getcwd()+'/data/TeacherManagement.csv'
    if(not os.path.exists(p)):
        print('Path %s does not exists.'%(p))
        input('TODO: Exception...')
        
    teacherDataFrame = pd.read_csv('%s'%(p))
    teacherDataFrame = teacherDataFrame.set_index(['CourseCode','ClassName'])
    return teacherDataFrame

def findTeacherOfSubject(courseCode,className):
    dataF = readTeacherManagementFile()
    return dataF.loc[(courseCode,className),'TeacherName']
