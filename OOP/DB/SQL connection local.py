import sqlite3
import os

con = sqlite3.connect(r'C:\Users\aaa_s\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db')
con.row_factory = sqlite3.Row  # Для доступа по именам столбцов - актуально только для sqlite
cursor = con.cursor() # Object for executing and processing requests of SQL
cursor.execute("SELECT * FROM customer")

customer = cursor.fetchall()
for person in customer:
    # customer_dict = dict(person)
    # full_name = f"{customer_dict['FirstName']} {customer_dict['LastName']}"
    print(dict(person)['FirstName'] + ' ' + dict(person)['LastName'])


# ТИПА ИНЪЕКЦИЯ
# f"Select * from users where user ='{user} and password ='{passw}'}'"

# Если потом в конце первого ввода ввести '; -- с пробелом в конце - он закомментирует оставшуюся часть и он прекратит запрос
# оставив только имя, после чего мы можем уже вводить что-угодно (читерство, поиск уязвимостей)
# query = "SELECT * FROM customer WHERE FirstName = '{0}' AND LastName ='{1}'"
# cursor.execute(query.format(input('FirstName'),input('LastName')))# что то вроде того - будет небезопасно (хотя у меня все равно 
# #не сработала инъекция)
# res = cursor.fetchall()
# for row in res:
#     print(dict(row))

FirstName = input('FirstName: ')
LastName = input('LastName: ')
cursor.execute("SELECT * FROM customer WHERE FirstName = ? AND LastName = ?", (FirstName, LastName))
persons = cursor.fetchall()
for person in persons:
    print(dict(person))

con.close()