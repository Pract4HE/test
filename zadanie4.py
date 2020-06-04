import sqlite3

# Указываем название файла базы данных
conn = sqlite3.connect('mydatabase.sqlite')
cursor = conn.cursor()

# Создаем таблицу blog с шестью полями - id , name , kurs , group , dolg , items
try:
    cursor.execute('''CREATE TABLE blog (id integer, name text, kurs integer, group integer, dolg integer, items text)''')
except:
    pass

# Вставляем в таблицу blog первую запись со значениями id , name , kurs , group , dolg , items
cursor.execute("INSERT INTO blog (id , name , kurs , group , dolg , items) VALUES (' ID', 'ФИО', 'курс', 'группа', 'количество задолженностей', 'предметы')")
conn.commit()

# Вставляем в таблицу blog вторую запись со значениями id , name , kurs , group , dolg , items
cursor.execute("INSERT INTO blog (id , name , kurs , group , dolg , items) VALUES (' ID', 'ФИО', 'курс', 'группа', 'количество задолженностей', 'предметы')")
conn.commit()

# Делаем выборку всех имеющихся в таблице записей и в цикле печатаем их значения
cursor.execute('SELECT * FROM blog')
row = cursor.fetchone()
while row is not None:
    print(row[0])
    print(row[1]+'\n')
    row = cursor.fetchone()

# Закрываем соединение с базой данных
cursor.close()
conn.close()