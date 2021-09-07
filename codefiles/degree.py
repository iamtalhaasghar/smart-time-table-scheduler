class Degree(object):
    def __init__(self, name, department):
        self.name = name
        self.department = department
        
    def saveToDatabase(self):
        import Filer
        import sqlite3 as sq
        con = sq.connect(Filer.DATA_BASE_FILE)
        c = con.cursor()
        query = 'Insert into Degrees (Name, Department) values(?,?)'
        c.execute(query, (self.name, self.department))
        con.commit()
        con.close()
        
def programsOfDepartment(department):
    import Filer
    import sqlite3 as sq
    con = sq.connect(Filer.DATA_BASE_FILE)
    c = con.cursor()
    query = 'Select Name from Degrees where Department = ?'
    c.execute(query,(department,))
    r = c.fetchall()
    result = [r[i][0] for i in range(len(r))]
    return result

