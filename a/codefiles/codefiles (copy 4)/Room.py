def createDepartmentRooms(department,count):
  
    rooms = list()
    
    for i in range(1,count+1):
        rooms.append('%s R%d'%(department,i))
    
    data = {'Name':rooms}
    import pandas as pd
    courses = pd.DataFrame(data=data, index = [i for i in range(1, len(rooms)+1)])
    courses = courses.rename_axis('Serial')

    import Filer
    folder = Filer.createDepartmentFolder(department)
    courses.to_csv('%s/%s'%(folder, Filer.ROOM_FILE_NAME))

def readAllRoomsOfDepartment(department):
    'reads All Room Names'
    import Filer
    import os
    p = '%s/%s/%s' %(Filer.DATA_FOLDER, department, Filer.ROOM_FILE_NAME)
    if(not os.path.exists(p)):
        print('%s does not exists'%(p))
        input('TODO: Exception')
        
    import pandas as pd
    data = pd.read_csv('%s'%(p))
    data = data.set_index('Serial')
    return data
    
def readAllRooms():
    import Filer
    departs = list(Filer.listAllDepartments())
    rooms = readAllRoomsOfDepartment(departs.pop(0))
    for d in departs:
        rooms = rooms.append(readAllRoomsOfDepartment(d), ignore_index = True)

    return rooms
    

    
