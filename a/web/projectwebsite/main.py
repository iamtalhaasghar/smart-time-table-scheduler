from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)

value=""
@app.route('/')
def home():
    email = request.args.get('Email')
    password = request.args.get('userpassword')
    connection = pymysql.connect(host='localhost', user='root', password='', db='american')
    with connection.cursor() as cursor:
        results = cursor.execute("SELECT * FROM registraion_form WHERE  password='" + str(password) + " ' AND rollno='" + str(email) + " '")
        all1 = cursor.fetchall()
        if all1.__len__()>0:
            return render_template('creat_account.html')
        else:
            return render_template('sign_in.html')

    return render_template('sign_in.html')


@app.route('/blog', methods={'GET','POST'})
def blog():
    if request.method=="POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        section = request.form.get('SECTION')
        program = request.form.get('Program')
        password = request.form.get('password')
        Roll_no = request.form.get('Roll_no')
        print(first_name)
        print(last_name)
        print(section)
        print(program)
        print(password)
        print(Roll_no)
        connection = pymysql.connect(host='localhost', user='root', password='', db='american')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM registraion_form WHERE  rollno='" + str(Roll_no) + " ' ")
            all12= cursor.fetchall()
            if all12.__len__() <= 0:
                query = "INSERT INTO`registraion_form`(`Firstname`, `Lastname`, `section`, `rollno`, `program`, `password`) VALUES('" + str(first_name) + "', '" + str(last_name) + "', '" + str(section) + "', '" + str( Roll_no) + "', '" + str(program) + "', '" + str(password) + "')"
                cursor.execute(query)
                connection.commit()
                value = "SUCCESSFULLY REGISTERED"
                return render_template('creat_account.html',value=value )
        value = "UNSUCCESSFULLY REGISTERED"
        return render_template('creat_account.html',value=value )

app.run(debug=False)
