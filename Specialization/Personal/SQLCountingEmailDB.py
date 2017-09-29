#!/usr/bin/env python3.1
import sqlite3
import urllib.request

conn = sqlite3.connect('emaildb2.sqlite')
cur = conn.cursor()

print ('Inizializing...')
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

print ('File created in SQLite...')
print ('Opening url...')

opener = urllib.request.FancyURLopener()
fh = opener.open('https://raw.githubusercontent.com/TaniaMol/PythonForEverybody/master/Python-SQLite/mbox.txt').read()
print ('Reading url sucessfully')
for line in fh :
    if not line.startswith('From: ', beg=0, end=len(line)) :
        continue
    print ('Reading...')
    pieces = line.split()
    email = pieces[1]
    parts = email.split('@')
    org = parts[-1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print ("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()
