from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Flask app!'

@app.route('/greetings')
def greetings():
    return """
    <h1>Seasonal Greetings</h1>
    <ul>
        <li>Merry Christmas!</li>
        <li>Happy New Year!</li>
        <li>Happy Easter!</li>
        <li>Happy Halloween!</li>
    </ul>
    """

@app.route('/greetings/christmas')
def christmas():
    return 'Merry Christmas!'

@app.route('/greetings/newyear')
def newyear():
    return 'Happy New Year!'

if __name__ == '__main__':
    app.run()

