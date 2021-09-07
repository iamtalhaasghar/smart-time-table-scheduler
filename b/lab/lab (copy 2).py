def makeLabs():
    lab = input('Enter Lab Name (q=quit): ')
    labList = list()
    while(lab != 'q'):
        labList.append(lab)
        lab = input('Enter lab name (q=quit): ')
    data = {'Name':labList}

    import pandas as pd
    labData = pd.DataFrame(data = data, index = [i for i in range(1, len(labList)+1)])
    labData = labData.rename_axis('Serial')
    labData.to_csv('labs/labs.csv')

def readAllLabs():
    import pandas as pd
    labData = pd.read_csv('labs/labs.csv')
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
    labDataFrame.to_csv('timetables/labmanagement.csv')

def makeLabManagementFile():
    import pandas as pd
    labDataFrame = pd.DataFrame(data = {'Lab':[],'Subject':[]})
    labDataFrame = labDataFrame.set_index('Subject')
    labDataFrame.to_csv('timetables/labmanagement.csv')
    
def readLabManagementFile():
    import pandas as pd
    labDataFrame = pd.read_csv('timetables/labmanagement.csv')
    labDataFrame = labDataFrame.set_index('Subject')
    return labDataFrame
