import sqlite3


def initiate_db():
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    # Products = [
    #     ('Вишня', 'Гейнер со вкусом вишни', 100),
    #     ('Клубника', 'Гейнер со вкусом клубники', 200),
    #     ('Персик-Маракуйя', 'Гейнер со вкусом персик-маракуйя', 300),
    #     ('Шоколад', 'Гейнер со вкусом шоколада', 400)
    # ]

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    # cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', Products)
    # cursor.execute('DELETE FROM Products')
    # cursor.execute('DELETE FROM Users')
    # connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT username FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        return True
    else:
        return False


def get_all_products():
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    prods = cursor.fetchall()
    return prods


# print(get_all_products()[0][1]) '''Поверка метода извлечения значений из функции'''
initiate_db()
# get_all_products()
# is_included('sasha')
