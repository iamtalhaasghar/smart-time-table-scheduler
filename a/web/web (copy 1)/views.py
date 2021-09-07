DEFAULT_EMPTY_CHAR = '-'
CSS_CLASS_NAME = 'table table-striped table-sm'
DATABASE_NAME = 'MasterTimeTable.db'
TABLE_NAME = 'TimeTable'

def makeTeacherViews():
    'Separates master time table Teacher wise'

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
    tableFrame = tableFrame.fillna(DEFAULT_EMPTY_CHAR)

    import teacher
    teacherList = [i[0] for i in teacher.readAllTeachers()]

    for t in teacherList:
        frameCopy = tableFrame.copy(deep = True)
        for d in tableFrame.index:
            for r in allRooms:
                for p in tableFrame.columns:        
                    temp = timeTable.loc[(d,r),p]
                    if(temp != DEFAULT_EMPTY_CHAR):
                        temp = eval(temp)
                        if(temp[2] == t):
                            frameCopy.loc[d,p] = [temp[0],temp[1],temp[3],r]
        import Filer
        frameCopy.to_csv('%s/%s.csv' % (Filer.TEACHER_VIEW_FOLDER,t))
        frameCopy.to_html('%s/teacher/%s.html' % (Filer.HTML_FOLDER,t))

def generateHtmlViewOfRoom(roomName):
   
    import pandas as pd

    import sqlite3
    conn = sqlite3.connect(DATABASE_NAME)
    
    timeTable = pd.read_sql_query('Select * from %s' % TABLE_NAME, conn)
    timeTable = timeTable.set_index(['Days','Rooms'])
    
    indexes = list(timeTable.index)
    days = list()
    allRooms = list()
    for k in indexes:
        if(days.count(k[0]) == 0):
            days.append(k[0])
        if(allRooms.count(k[1]) == 0):
            allRooms.append(k[1])
            
    if(roomName not in allRooms):
        return ('<h2>Sorry! There is no room named as "%s".</h2>' % roomName)
            
    periods = timeTable.columns
    tableFrame = pd.DataFrame(index = days, columns = periods)
    tableFrame = tableFrame.rename_axis('Days', axis='index')
    tableFrame = tableFrame.fillna(DEFAULT_EMPTY_CHAR)
    for d in tableFrame.index:
        for p in tableFrame.columns:
            temp = timeTable.loc[(d,roomName),p]
            if(temp != DEFAULT_EMPTY_CHAR):
                temp = eval(temp)
                tableFrame.loc[d,p] = '%s<br>%s<br>%s<br>%s'%(temp[0],temp[1],temp[2], temp[3])
    htmlString = dataFrameToHtmlString(tableFrame)
    return htmlString

def generateHtmlViewOfClass(semester):

    import sqlite3
    import pandas as pd

    conn = sqlite3.connect(DATABASE_NAME)
    timeTable = pd.read_sql_query('Select * from %s' % TABLE_NAME, conn)
    timeTable = timeTable.set_index(['Days','Rooms'])
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
    tableFrame = tableFrame.rename_axis('Periods', axis='columns')
    tableFrame = tableFrame.rename_axis('Days', axis = 'index')
    tableFrame = tableFrame.fillna(DEFAULT_EMPTY_CHAR)
    wasFound = False
    for d in tableFrame.index:
        for r in allRooms:
            for p in tableFrame.columns:        
                temp = timeTable.loc[(d,r),p]
                if(temp != DEFAULT_EMPTY_CHAR):
                    temp = eval(temp)
                    if(temp[0] == semester):
                        wasFound = True
                        tableFrame.loc[d,p] = '%s<br>%s<br>%s<br>%s'%(temp[1],temp[2],temp[3],r)

    if (wasFound):
       return dataFrameToHtmlString(tableFrame, True)
    
    return ('<h2>Sorry! Your Time Table was not found.</h2>')

def pasteTimeTableInDashboard(tableString):            
    import io
    data = io.StringIO()
    
    with open('templates/dash.html') as dashboard:
        for l in dashboard:
            if l.strip().startswith('<div class="table-responsive">'):
                data.write(l)
                data.write(getTimeTableStyle())
                data.write('\n%s\n' % tableString)
            else:
                data.write(l)
    return data.getvalue()

def generateEmbeddedTimeTable(timeTableHtml):
    
    prettyTimeTable = pasteTimeTableInDashboard(timeTableHtml)
    open('templates/dashboard.html', 'w').write(prettyTimeTable)

def getTimeTableStyle():
    styleString = """\n<style>
            body{font-family: -apple-system,BlinkMacSystemFont,
            "Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,
            "Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol",
            "Noto Color Emoji";}
            table{border: 3px solid #E1E8ED;border-collapse:collapse;
	    width: 100%;height: 100%;}th{
		text-align: center;
		background-color: #34A853;
		color: #F7F7F7;
		border: 2px solid #E1E8ED;}td{
		border: 2px solid #E1E8ED;
		text-align: center;
		font-weight: 500;}td:hover{
		background-color:#88cc00;}
                h1{text-align: center; color: black}
                footer{padding: 20px 20px 20px 20px; text-align: center;}
		</style>
		\n
            """

    return styleString

def generateTimeTablePdf(semester):

    tableHtml = generateHtmlViewOfClass(semester)
    
    '''
    footerString = """
        <footer>
        <small>The Time Table is generated by the software <i>"The Smart Time Scheduler"</i>.
	</small></footer>
    	"""
    '''
    import io
    buffer = io.StringIO()
    buffer.write(getTimeTableStyle())
    buffer.write(tableHtml)
    buffer.write(footerString)
    open('templates/export.html','w').write(buffer.getvalue())

def dataFrameToHtmlString(dFrame, shallTranspose = True):

    if(shallTranspose):
        dFrame = dFrame.T
    import pandas as pd
    pd.set_option('display.max_colwidth', 0)
    import io
    buffer = io.StringIO()
    dFrame.to_html(buffer,
                      classes = CSS_CLASS_NAME, escape = False, border=0)
    return buffer.getvalue()
