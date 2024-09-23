import sqlite3
import os

DIR = os.getcwd() + "\Database"
os.chdir(DIR)

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# Create a new table
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(10, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()