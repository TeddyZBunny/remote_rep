import sqlite3
import os
      
conn = sqlite3.connect(r'C:\Users\aaa_s\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db')
cursor = conn.cursor()  # Object for executing and processing requests of SQL
cursor.execute('SELECT * FROM Customer') 
# print(cursor.fetchone()) #Возвращает следующую ОДНУ строку результата
print(cursor.fetchall())
conn.close() # Closing connection