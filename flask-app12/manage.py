import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
Bootstrap(app)
app.secret_key = "secret key"

conn = mysql.connector.connect(
    host='localhost',
    user='flask',
    password='password',
    database='employees'
)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
        EmpID INT AUTO_INCREMENT PRIMARY KEY,
        EmpName VARCHAR(255),
        EmpGender VARCHAR(255),
        EmpPhone VARCHAR(255),
        EmpBdate VARCHAR(255))''')
print("Table created")
conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        empname = request.form['EmpName']
        empgender = request.form['EmpGender']
        empphone = request.form['EmpPhone']
        empbdate = request.form['EmpBdate']

        conn = mysql.connector.connect(
            host='localhost',
            user='flask',
            password='password',
            database='employees'
        )
        c = conn.cursor()
        c.execute("INSERT INTO employees (EmpName, EmpGender, EmpPhone, EmpBdate) VALUES ('{0}', '{1}', '{2}', '{3}')".format(empname, empgender, empphone, empbdate))
        conn.commit()
        conn.close()

        return redirect(url_for('information'))
    
    return render_template('registration.html')

@app.route('/information')
def information():
    conn = mysql.connector.connect(
        host='localhost',
        user='flask',
        password='password',
        database='employees'
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.close()
    return render_template('information.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
