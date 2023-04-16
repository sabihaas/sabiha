from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my Flask app!"

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/login/", methods=["POST"])
def login_post():
    password = request.form.get("password")
    if password == "Buffalo$":
        return redirect(url_for("login_success"))
    else:
        return redirect(url_for("login_failure"))

@app.route("/login/success/")
def login_success():
    return "Login successful!"

@app.route("/login/failure/")
def login_failure():
    return "Login failed!"

if __name__ == "__main__":
    app.run(debug=True)
