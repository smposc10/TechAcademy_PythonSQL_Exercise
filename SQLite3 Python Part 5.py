# Part 5: https://www.youtube.com/watch?v=AtBZC9F-MjI&index=5&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo
# Part 5 involves updating and deleting entries on your database.

import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

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

def graph_data():
    #we will graph value for evey type that is in a database
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #dates.append()
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))

        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, '-')
    plt.show()

##create_table()
##data_entry() <-- for part 2, we comment out data_entry function because we will be using dynamic_data_entry instead

##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)

##read_from_db()

graph_data()
c.close()
conn.close()