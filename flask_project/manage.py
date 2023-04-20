from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to my Flask application!'

if __name__ == "__main__":
    app.run()
