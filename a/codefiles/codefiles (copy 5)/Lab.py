def createLabs(count):
    
    labList = list()
    for i in range(1,count+1):
        labList.append('LAB %d'%(i))
        
    data = {'Name':labList}

    import pandas as pd
    labData = pd.DataFrame(data = data, index = [i for i in range(1, len(labList)+1)])
    labData = labData.rename_axis('Serial')
    import Filer
    folder = Filer.createFolder('data')
    labData.to_csv('%s/%s.csv'%(folder,'Labs'))
    makeLabManagementFile()

def readAllLabs():
    import os
    p = os.getcwd() + '/data/Labs.csv'
    if(not os.path.exists(p)):
        print('Path %s does not exists.')
        input('TODO: Expception')
        
    import pandas as pd
    labData = pd.read_csv('%s'%(p))
    labData = labData.set_index('Serial')
    return labData

def selectLab(subject):
    labsData = readAllLabs()
    allLabs = list(labsData.Name)
    for i in range(len(allLabs)):
        print('%d : %s' %(i+1, allLabs[i]))
    lab = int(input('Select Lab: '))
    lab = allLabs[lab-1]
    
    labDataFrame = readLabManagementFile()
    labDataFrame = labDataFrame.T
    labDataFrame.insert(len(labDataFrame.columns),subject,lab)
    labDataFrame = labDataFrame.T
    import os
    p = os.getcwd() + '/data/LabManagement.csv'
    if(not os.path.exists(p)):
        print('Path %s does not exists')
        input('TODO: Exception') 
    labDataFrame.to_csv('%s'%(p))

def makeLabManagementFile():
    import pandas as pd
    labDataFrame = pd.DataFrame(data = {'Lab':[],'Subject':[]})
    labDataFrame = labDataFrame.set_index('Subject')
    import Filer
    folder = Filer.createFolder('data')
    labDataFrame.to_csv('%s/%s.csv'%(folder,'LabManagement'))
    
def readLabManagementFile():
    import os
    p = os.getcwd() + '/data/LabManagement.csv'
    if(not os.path.exists(p)):
        print('Path %s does not exists')
        input('TODO: Exception')
    import pandas as pd
    labDataFrame = pd.read_csv('%s'%(p))
    labDataFrame = labDataFrame.set_index('Subject')
    return labDataFrame

def findLabOfSubject(subject):
    dataF = readLabManagementFile()
    return dataF.loc[subject,'Lab']
