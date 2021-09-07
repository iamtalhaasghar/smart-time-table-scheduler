from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
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
        return redirect('/timetables/class/show/%s' % (semesterName))  

    
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
        print(firstName),
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

@app.route('/timetables/room')
@app.route('/timetables/class')
@app.route('/timetables/teacher')

def showOtherTemplate():
    d = request.path
    return render_template('class.html', to_go='%s/show'%d)

@app.route('/timetables/<criteria>/show',methods={'POST','GET'})
def searchPoint(criteria):
    if request.method == 'POST':
        d = request.form.get('toSearch')
        s = '/timetables/%s/show/%s' % (criteria,d)
        return redirect(s)

    return redirect('/')

@app.route('/timetables/class/show/<className>')
def showDashboard(className):
    import views
    views.generateEmbeddedTimeTable(views.generateHtmlViewOfClass(className))
    return render_template('dashboard.html', time_table_of = className)


@app.route('/timetables/room/show/<roomName>')
def showRoomTimeTable(roomName):
    import views
    views.generateEmbeddedTimeTable(views.generateHtmlViewOfRoom(roomName))
    return render_template('dashboard.html', time_table_of = roomName)

@app.route('/timetables/teacher/show/<teacherName>')
def showTeacherTimeTable(teacherName):
    import views
    views.generateEmbeddedTimeTable(views.generateHtmlViewOfTeacher(teacherName))
    return render_template('dashboard.html', time_table_of = teacherName)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')    
