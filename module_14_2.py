# Загрузка библиотек
import sqlite3


# Создадим базу
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполним базу согласно задания
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?) ",
                   (f'user{i}', f'examle{i}@gmail.com', i * 10, 1000))

# установим баланс каждой второй записи в 500
cursor.execute("UPDATE Users SET balance = 500 WHERE id%2 != 0")

# Удалим каждую третью запись начиная с первой
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

# Удалим запись с пользователем с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Посчитаем общее количество записей в базе
cursor.execute("SELECT COUNT(*) FROM Users")
# Сохраним и выведем значение количества записей
total_users = cursor.fetchone()[0]
print(f'Обшее количество записей/пользователей в базе: {total_users}')

# Общая сумма баланса пользователей
cursor.execute("SELECT SUM(balance) FROM Users")
# Сохраним и выведем значение общей суммы баланса
all_balance = cursor.fetchone()[0]
print(f'Общая сумма баланса пользователей: {all_balance}')

# Рассчитаем среднее значение баланса
print(f'Среднее расчетное значение баланса: {all_balance / total_users}')

# Сделаем запрос к базе среднего значения баланса
cursor.execute("SELECT AVG(balance) FROM Users")

# выведем полученное среднее значение
print(f'Среднее значение баланса из запроса: {cursor.fetchone()[0]}')

connection.commit()
connection.close()