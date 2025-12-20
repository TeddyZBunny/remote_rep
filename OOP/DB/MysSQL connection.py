import mysql.connector



con = mysql.connector.connect(
    host='host',
    user='user',
    password='passsword',
    database='name'
)

# НО ЕСЛИ PostgreSQL      
# cursor = con.cursor() # Object for executing and processing requests of SQL
# cursor.execute('SELECT * FROM Customer') 
# # print(cursor.fetchone()) #Возвращает следующую ОДНУ строку результата
# customer = cursor.fetchall()
# for person in customer:
#   print(person['FírstName'])

# # for person in customer:
# #     print(person['FirstName']) 

# conn.close() # Closing connection

cursor = con.cursor() 
cursor.execute('SELECT * FROM Customer') 
# print(cursor.fetchone())
print(cursor.fetchall())
con.close()