def addRooms():
    #rooms = ['R1','R2','R3']
    
    rooms = list()
    r = input('Enter name of room (q=quit): ')
    while r != 'q':
        rooms.append(r)
        r = input('Enter name of room (q=quit): ')
    
    data = {'Name':rooms}
    import pandas as pd
    courses = pd.DataFrame(data=data, index = [i for i in range(1, len(rooms)+1)])
    courses = courses.rename_axis('Serial')
    courses.to_csv('rooms/rooms.csv')

def readAllRooms():
    'reads All Room Names'
    import pandas as pd
    data = pd.read_csv('rooms/rooms.csv')
    data = data.set_index('Serial')
    return data
    
