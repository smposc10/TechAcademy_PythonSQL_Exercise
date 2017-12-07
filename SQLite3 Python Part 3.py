# Part 3
# This part, how to pull entries in your database, using randomized data with timestamps

import sqlite3
import time
import datetime
import random

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


#part 2 starts here
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute("SELECT * FROM stuffToPlot")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)


##create_table()
##data_entry() <-- for part 2, we comment out data_entry function because we will be using dynamic_data_entry instead

##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)

read_from_db()
c.close()
conn.close()
