# Video tutorial:
# Part 1: https://www.youtube.com/watch?v=o-vsdfCBpsU&feature=youtu.be&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo
# Part 2: https://www.youtube.com/watch?v=qfGu0fBfNBs&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo&index=2

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
    #Note: all caps for things that are SQL and lowercase for things that are not to standardize

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1451255552, '2016-01-02','Python', 8)")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()