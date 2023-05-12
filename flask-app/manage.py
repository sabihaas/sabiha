from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__, template_folder='templates')
app.secret_key = "secret key"

conn = sqlite3.connect('employees.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employees (
        EmpID INTEGER PRIMARY KEY,
        EmpName TEXT,
        EmpGender TEXT,
        EmpPhone TEXT,
        EmpBdate DATE)''')
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

        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("INSERT INTO employees (EmpName, EmpGender, EmpPhone, EmpBdate) VALUES (?, ?, ?, ?)" , (empname, empgender, empphone, empbdate))
        conn.commit()
        conn.close()

        return redirect(url_for('information'))
    
    return render_template('registration.html')

@app.route('/information')
def information():
    with sqlite3.connect('employees.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
    return render_template('information.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)