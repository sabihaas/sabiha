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
    database='food'
)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerName TEXT,
        ItemName TEXT,
        ItemPrice REAL,
        OrderDate DATE)''')
print("Table created")
conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    items = [
        {'name': 'Pizza', 'price': 10.99},
        {'name': 'Burger', 'price': 6.99},
        {'name': 'Taco', 'price': 4.99},
        {'name': 'Salad', 'price': 8.99},
    ]
    return render_template('menu.html', items=items)

@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        name = request.form['name']
        item_name = request.form['item_name']
        item_price = request.form['item_price']
        order_date = request.form['order_date']

        conn = mysql.connector.connect(
            host='localhost',
            user='flask',
            password='password',
            database='food'
        )
        c = conn.cursor()
        c.execute("INSERT INTO orders (CustomerName, ItemName, ItemPrice, OrderDate) VALUES (%s, %s, %s, %s)", (name, item_name, item_price, order_date))
        conn.commit()
        conn.close()

        return redirect(url_for('order_history'))
    
    items = [
        {'name': 'Pizza', 'price': 10.99},
        {'name': 'Burger', 'price': 6.99},
        {'name': 'Taco', 'price': 4.99},
        {'name': 'Salad', 'price': 8.99},
    ]
    return render_template('place_order.html', items=items)

@app.route('/order_history')
def order_history():
    conn = mysql.connector.connect(
        host='localhost',
        user='flask',
        password='password',
        database='food'
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    conn.close()
    return render_template('order_history.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
