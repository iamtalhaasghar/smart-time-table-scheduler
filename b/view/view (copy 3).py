def makeRoomViews():
    'Separates master time table room wise'
    import TimeTable
    import pandas as pd
    
    timeTable = TimeTable.readTimeTable().copy(deep = True) # For Safety
    indexes = list(timeTable.index)
    allRooms = list()
    days = list()
    
    for k in indexes:
        if(days.count(k[0]) == 0):
            days.append(k[0])
        if(allRooms.count(k[1]) == 0):
            allRooms.append(k[1])
            
    periods = timeTable.columns
    tableFrame = pd.DataFrame(index = days, columns = periods)
    tableFrame = tableFrame.rename_axis('Days', axis='index')
    tableFrame = tableFrame.fillna(TimeTable.theDefaultEmptyChar())

    for r in allRooms:
        frameCopy = tableFrame.copy(deep = True)
        for d in tableFrame.index:
            for p in tableFrame.columns:
                frameCopy.loc[d,p] = timeTable.loc[(d,r),p]
        #frameCopy = frameCopy.T        
        frameCopy.to_csv('roomviews/%s.csv' % (r))
        frameCopy.to_html('htmlfiles/room/%s.html' % (r))

def makeClassViews(semester = 'CS1B'):
    'Separates master time table class wise'

    import TimeTable
    import pandas as pd
    
    timeTable = TimeTable.readTimeTable().copy(deep = True) # For Safety
    indexes = list(timeTable.index)
    allRooms = list()
    days = list()
    
    for k in indexes:
        if(days.count(k[0]) == 0):
            days.append(k[0])
        if(allRooms.count(k[1]) == 0):
            allRooms.append(k[1])
            
    periods = timeTable.columns
    tableFrame = pd.DataFrame(index = days, columns = periods)
    tableFrame = tableFrame.rename_axis('Days', axis='index')
    tableFrame = tableFrame.fillna(TimeTable.theDefaultEmptyChar())

    frameCopy = tableFrame.copy(deep = True)
    
    for d in tableFrame.index:
        for r in allRooms:
            for p in tableFrame.columns:        
                temp = timeTable.loc[(d,r),p]
                if(temp != TimeTable.theDefaultEmptyChar()):
                    temp = eval(temp)
                    if(temp[0] == semester):
                        frameCopy.loc[d,p] = [temp[1],temp[2],temp[3],r]
    
    #frameCopy = frameCopy.T
    frameCopy.to_csv('classviews/%s.csv' % (semester))
    frameCopy.to_html('htmlfiles/semester/%s.html' % (semester))
    
def makeTeacherViews():
    'Separates master time table Teacher wise'

    import TimeTable
    import pandas as pd
    
    timeTable = TimeTable.readTimeTable().copy(deep = True) # For Safety
    indexes = list(timeTable.index)
    allRooms = list()
    days = list()
    
    for k in indexes:
        if(days.count(k[0]) == 0):
            days.append(k[0])
        if(allRooms.count(k[1]) == 0):
            allRooms.append(k[1])
            
    periods = timeTable.columns
    tableFrame = pd.DataFrame(index = days, columns = periods)
    tableFrame = tableFrame.rename_axis('Days', axis='index')
    tableFrame = tableFrame.fillna(TimeTable.theDefaultEmptyChar())

    import teacher
    teacherList = teacher.readAllTeachers().Name

    for t in teacherList:
        frameCopy = tableFrame.copy(deep = True)
        for d in tableFrame.index:
            for r in allRooms:
                for p in tableFrame.columns:        
                    temp = timeTable.loc[(d,r),p]
                    if(temp != TimeTable.theDefaultEmptyChar()):
                        temp = eval(temp)
                        if(temp[2] == t):
                            frameCopy.loc[d,p] = [temp[0],temp[1],temp[3],r]
        
        frameCopy.to_csv('teacherviews/%s.csv' % (t))
        frameCopy.to_html('htmlfiles/teacher/%s.html' % (t))
makeTeacherViews()
makeClassViews()
makeRoomViews()
