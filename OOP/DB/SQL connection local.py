import sqlite3
import os
      
# conn = sqlite3.connect(r'C:\Users\aaa_s\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db')
# conn.row_factory  = sqlite3
# cursor = conn.cursor() # Object for executing and processing requests of SQL
# cursor.execute('SELECT * FROM Customer') 
# # print(cursor.fetchone()) #Возвращает следующую ОДНУ строку результата
# person = (dict(row)['FirstName'] for row in cursor.fetchall())
# print(person)

# # for person in customer:
# #     print(person['FirstName']) 

# conn.close() # Closing connection

conn = sqlite3.connect(r'C:\Users\aaa_s\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db')
conn.row_factory = sqlite3.Row  # Для доступа по именам столбцов
cursor = conn.cursor() # Object for executing and processing requests of SQL
cursor.execute("SELECT * FROM customer")

customer = cursor.fetchall()
for person in customer:
    # customer_dict = dict(person)
    # full_name = f"{customer_dict['FirstName']} {customer_dict['LastName']}"
    print(dict(person)['FirstName'] + ' ' + dict(person)['LastName'])

conn.close()