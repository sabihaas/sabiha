import sqlite3

conn = sqlite3.connect('employees.db')

conn.execute('''CREATE TABLE employees
             (EmpID INTEGER PRIMARY KEY,
             EmpName TEXT,
             EmpGender TEXT,
             EmpPhone TEXT,
             EmpBdate TEXT)''')

employees = [(1, 'Joe', 'F', '×234', '1/11/1985'),
             (2, 'Sue', 'F', '×345', '2/7/1983'),
             (3, 'Amy', 'IM', '×456', '8/4/1990'),
             (4, 'Pat', 'M', '×567', '3/8/1971'),
             (5, 'Mike', 'F', '×678', '5/5/1965'),
             (10, 'Mike', 'F', '×666', '8/1/1974'),
             (7, 'Barbara', 'x777', 'x777', '4/5/1980'),
             (11, 'Ivan', '×777', '×777', '3/4/1981'),
             (9, 'Amy', 'x777', 'x777', '1/11/1985')]

conn.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", 
employees)

conn.commit()
conn.close()

