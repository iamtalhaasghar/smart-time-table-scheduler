def createDepartmentLabs(department,count):
    
    labList = list()
    for i in range(1,count+1):
        labList.append('%s LAB%d'%(department,i))
        
    data = {'Name':labList}

    import pandas as pd
    labData = pd.DataFrame(data = data, index = [i for i in range(1, len(labList)+1)])
    labData = labData.rename_axis('Serial')
    import Filer
    folder = Filer.createDepartmentFolder(department)
    labData.to_csv('%s/%s' % (folder, Filer.LAB_FILE_NAME))

def readAllLabsOfDepartment(department):
    import os
    import Filer
    p = '%s/%s/%s' % (Filer.DATA_FOLDER, department, Filer.LAB_FILE_NAME)
    if(not os.path.exists(p)):
        print('Path %s does not exists.')
        input('TODO: Expception')
        
    import pandas as pd
    labData = pd.read_csv('%s'%(p))
    labData = labData.set_index('Serial')
    return labData

def assignLab(courseCode, className, labName):
    import pandas as pd
    labDataFrame = pd.DataFrame(data = {'CourseCode':[courseCode],
                                        'ClassName':[className],
                                        'LabName':[labName]})
    labDataFrame = labDataFrame.set_index(['CourseCode','ClassName'])
    labDataFram = readLabManagementFile().append(labDataFrame)
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

def readAllLabs():
    import Filer
    departs = list(Filer.listAllDepartments())
    labs = readAllLabsOfDepartment(departs.pop(0))

    for d in departs:
        labs = labs.append(readAllLabsOfDepartment(d), ignore_index = True)
    
    return labs        


    
