from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/add_employee', methods=['POST', 'GET'])
def add_employee():
    try:
        EmpID = request.form['EmpID']
        EmpName = request.form['EmpName']
        EmpGender = request.form['EmpGender']
        EmpPhone = request.form['EmpPhone']
        EmpBdate = request.form['EmpBdate']

        with sqlite3.connect("employees.db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employees (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES (?, ?, ?, ?, ?)"
            cur.execute(cmd, (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate))
            con.commit()
            msg = "Record successfully added"
    except:
        con.rollback()
        msg = "Error in insert operation"

    finally:
        con.close()
        return render_template("output.html", msg=msg)

@app.route('/information')
def information():
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('information.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
