def addTeacherInDepartment(department,teacherId,teacherName):
    
    import Filer
    folder = Filer.createDepartmentFolder(department)
    path = '%s/%s' % (folder, Filer.TEACHER_FILE_NAME)
    
    import pandas as pd
    import os
    
    if(os.path.exists(path)):
        teacherData = readAllTeachersOfDepartment(department)
        teacherData = teacherData.T
        teacherData.insert(len(teacherData.columns),teacherId,teacherName)
        teacherData = teacherData.T
    else:
        teacherData = pd.DataFrame({'Id':[teacherId],'Name':[teacherName]})
        teacherData = teacherData.set_index('Id')

    teacherData.to_csv(path)    

def readAllTeachersOfDepartment(department):
    import Filer
    import os
    p = '%s/%s/%s' %(Filer.DATA_FOLDER, department, Filer.TEACHER_FILE_NAME)
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

def readAllTeachers():
    import Filer
    departs = list(Filer.listAllDepartments())
    teachers = readAllTeachersOfDepartment(departs.pop(0))
    for d in departs:
        teachers = teachers.append(readAllTeachersOfDepartment(d), ignore_index = True)

    return teachers

    
