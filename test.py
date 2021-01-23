import sqlite3

conn = sqlite3.connect("wishlist.db")

c = conn.cursor()

items = [
    (None, "Кошка", 30, "example.com"),
    (None, "Холодильник", 30000, "holodilniki.com"),
    (None, "Кирпич", 5, "kirpichi.com"),
    (None, "Клавиатура", 7000, "keyboard.com"),
]

c.executemany("INSERT INTO wishlist VALUES (?,?,?,?)", items)

for row in c.execute("SELECT * FROM wishlist"):
    print(row)
