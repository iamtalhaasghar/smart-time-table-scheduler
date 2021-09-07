def addTeachers():
    teacher = input('Enter Teacher Name (q=quit): ')
    teacherList = list()
    while(teacher != 'q'):
        teacherList.append(teacher)
        teacher = input('Enter Teacher name (q=quit): ')
    data = {'Name':teacherList}

    import pandas as pd
    teacherData = pd.DataFrame(data = data, index = [i for i in range(1, len(teacherList)+1)])
    teacherData = teacherData.rename_axis('Serial')
    import Filer
    folder = Filer.createFolder('data')
    teacherData.to_csv('%s/%s.csv'%(folder,'Teachers'))
    makeTeacherManagementFile()

def readAllTeachers():
    import os
    p = os.getcwd() + '/data/Teachers.csv'
    if(not os.path.exists(p)):
        print('Path %s does not exists'%(p))
        input('TODO: Exception ...')
    import pandas as pd
    data = pd.read_csv('%s'%(p))
    data = data.set_index('Serial')
    return data

def selectTeacher(subject):
    teachersData = readAllTeachers()
    allTeachers = list(teachersData.Name)
    for i in range(len(allTeachers)):
        print('%d : %s' %(i+1, allTeachers[i]))
    teacher = int(input('Select Teacher: '))
    teacher = allTeachers[teacher-1]
    
    teacherDataFrame = readTeacherManagementFile()
    teacherDataFrame = teacherDataFrame.T
    teacherDataFrame.insert(len(teacherDataFrame.columns),subject,teacher)
    teacherDataFrame = teacherDataFrame.T
    import os
    p = os.getcwd() + '/data/TeacherManagement.csv'
    if(not os.path.exists(p)):
        print('Path %s does not exists.'%(p))
        input('TODO: Exception...')
    teacherDataFrame.to_csv('%s'%(p))

def makeTeacherManagementFile():
    import pandas as pd
    teacherDataFrame = pd.DataFrame(data = {'Teacher':[],'Subject':[]})
    teacherDataFrame = teacherDataFrame.set_index('Subject')
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
    teacherDataFrame = teacherDataFrame.set_index('Subject')
    return teacherDataFrame

def findTeacherOfSubject(subject):
    dataF = readTeacherManagementFile()
    return dataF.loc[subject,'Teacher']
