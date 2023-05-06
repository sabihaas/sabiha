import sqlite3

conn = sqlite3.connect('food.db')

conn.execute('''CREATE TABLE IF NOT EXISTS orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerName TEXT,
        ItemName TEXT,
        ItemPrice REAL,
        OrderDate DATE)''')

orders = [(1, 'Alice', 'Pizza', 10.99, '2023-05-01'),
          (2, 'Bob', 'Burger', 6.99, '2023-05-02'),
          (3, 'Charlie', 'Taco', 4.99, '2023-05-03'),
          (4, 'Alice', 'Salad', 8.99, '2023-05-04'),
          (5, 'David', 'Pizza', 10.99, '2023-05-05')]

conn.executemany("INSERT INTO orders (OrderID, CustomerName, ItemName, ItemPrice, OrderDate) VALUES (?, ?, ?, ?, ?)", orders)

conn.commit()
conn.close()
