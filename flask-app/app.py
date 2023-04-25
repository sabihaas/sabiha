from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/information")
def information():
    employees = [
        {"id": 1, "name": "John", "age": 30, "address": "123 Main St", 
"salary": 50000},
        {"id": 2, "name": "Jane", "age": 25, "address": "456 Oak St", 
"salary": 60000},
        {"id": 3, "name": "Bob", "age": 40, "address": "789 Maple St", 
"salary": 70000},
    ]
    return render_template("information.html", employees=employees)

if __name__ == "__main__":
    app.run(debug=True)

