import psycopg2

try:
    conn = psycopg2.connect(
        host='localhost',      # или IP удалённого сервера
        port='5432',
        dbname='your_database',
        user='postgres',
        password='your_password'
    )
    print("Подключение успешно!")
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone())
    cur.close()
    conn.close()
except Exception as e:
    print(f"Ошибка подключения: {e}")
