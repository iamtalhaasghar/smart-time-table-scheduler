def createRooms(count):
    
    rooms = list()
    
    for i in range(1,count+1):
        rooms.append('R%d'%(i))
    
    data = {'Name':rooms}
    import pandas as pd
    courses = pd.DataFrame(data=data, index = [i for i in range(1, len(rooms)+1)])
    courses = courses.rename_axis('Serial')

    import Filer
    folder = Filer.createFolder('data')
    courses.to_csv('%s/%s.csv'%(folder,'Rooms'))

def readAllRooms():
    'reads All Room Names'
    import os
    p = os.getcwd() + '/data/Rooms.csv'
    if(not os.path.exists(p)):
        print('%s does not exists'%(p))
        input('TODO: Exception')
        
    import pandas as pd
    data = pd.read_csv('%s'%(p))
    data = data.set_index('Serial')
    return data
    
