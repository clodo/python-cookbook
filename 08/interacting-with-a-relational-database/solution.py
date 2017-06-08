import sqlite3

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

db = sqlite3.connect('database.sqlite')
c = db.cursor()

# Create table
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

# Insert data
c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

# Get all portfolios
for row in db.execute('select * from portfolio'):
    print(row)

# Get all portfolios where price > 100
min_price = 100
for row in db.execute('select * from portfolio where price >= ?',
                      (min_price,)):
    print(row)
