def createDepartmentRooms(department,count):

    import Filer
    import sqlite3
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()
    
    for i in range(1,count+1):
        c.execute('Insert into Rooms (Name, Department) values(?, ?)',
                  ( ('%s R%d'%(department,i)) , department) )

    
    conn.commit()
    conn.close()
    
def readAllRoomsOfDepartment(department):

    import Filer
    import sqlite3
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()

    c.execute('Select Name from Rooms where Department = ?', (department,))
    return c.fetchall()
    
def readAllRooms():
    
    import Filer
    import sqlite3
    conn = sqlite3.connect(Filer.DATA_BASE_FILE)
    c = conn.cursor()

    c.execute('Select Name, Department from Rooms')
    return c.fetchall()

    
