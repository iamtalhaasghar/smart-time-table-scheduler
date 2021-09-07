from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def showHomePage():
    return render_template('index.html')

@app.route('/sign_in')
def showSignInPage():
    return render_template('sign_in.html')

@app.route('/sign_up')
def showSignUpPage():
    return render_template('sign_up.html')


@app.route('/log_in', methods={'POST'})
def logIn():
    rollNumber = request.form.get('roll_number')
    password = request.form.get('password')
    
    import pymysql as sq
    connection = sq.connect(host='localhost', user='root', password='', db='Accounts')
    c = connection.cursor()
    query = 'Select Semester from users where RollNumber=%s and Password = %s'
    c.execute(query,(rollNumber, password))
    result = c.fetchall()
    if(len(result) == 1):
        semesterName = str(result[0][0])
        connection.close()
        return redirect('/timetables/class/%s' % (semesterName))  

    
    return redirect('/index')
    
@app.route('/create_account', methods={'GET','POST'})
def createAccount():    
    if request.method=="POST":
        firstName = request.form.get('first_name')
        lastName = request.form.get('last_name')
        rollNumber = request.form.get('roll_number')
        program = request.form.get('program')
        semester = request.form.get('semester')
        password = request.form.get('password')
        '''
        print(firstName)
        print(lastName)
        print(rollNumber)
        print(program)
        print(semester)
        print(password)
        '''
        import pymysql as sq
        connection = sq.connect(host='localhost', user='root', password='', db='Accounts')
        c = connection.cursor()
        query = "INSERT INTO `users`(`FirstName`, `LastName`, `Semester`, `RollNumber`, `Program`, `Password`) VALUES(%s,%s,%s,%s,%s,%s)"  
        c.execute(query,(firstName, lastName, semester, rollNumber, program, password) )
        connection.commit()
        connection.close()        
    return redirect('/index')


@app.route('/timetables/class/<className>')
def showDashboard(className):
    import views
    views.generateEmbeddedTimeTable(views.generateHtmlViewOfClass(className))
    return render_template('dashboard.html', time_table_of = className)


@app.route('/export')
def exportTimeTable(className):
    import views
    views.generateTimeTablePdf(className)
    return render_template('export.html',
                           time_table_of = className)



@app.route('/timetables/room/<roomName>')
def showRoomTimeTable(roomName):
    import views
    views.generateEmbeddedTimeTable(views.generateHtmlViewOfRoom(roomName))
    return render_template('dashboard.html', time_table_of = roomName)

if __name__ == '__main__':
    app.run(debug = True)    
