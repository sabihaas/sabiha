from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to my Flask application!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'Buffalo$':
            return redirect(url_for('login_successful'))
        else:
            return redirect(url_for('login_rejected'))
    return render_template('login.html')

@app.route('/login_successful/')
def login_successful():
    return 'Login successful!'

@app.route('/login_rejected/')
def login_rejected():
    return 'Login rejected. Incorrect password.'
