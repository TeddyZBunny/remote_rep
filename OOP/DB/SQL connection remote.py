import mysql.connector
      
con = mysql.connector.connect(
    host='host',
    user='user',
    password='passsword',
    database='name'
)

cursor = con.cursor() 
cursor.execute('SELECT * FROM Customer') 
# print(cursor.fetchone())
print(cursor.fetchall())
con.close()