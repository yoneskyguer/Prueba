import sqlite3
from seed import user, category, product

conexion = sqlite3.connect('data.db')

cursor = conexion.cursor()

drop_table = "DROP TABLE IF EXISTS user;"
create_table = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, user text, password text)"
cursor.execute(drop_table)
cursor.execute(create_table)

drop_table3 = "DROP TABLE IF EXISTS category;"
create_tables3 = "CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, quantity float, product_id INTEGER)"
cursor.execute(drop_table3)
cursor.execute(create_tables3)

cursor.execute("INSERT INTO category VALUES (1, 'Oficina', 3, 1)")
cursor.execute("INSERT INTO category VALUES (2, 'Oficina', 2, 2)")
cursor.execute("INSERT INTO category VALUES (3, 'Oficina', 2, 3)")

drop_table4 = "DROP TABLE IF EXISTS product;"
create_tables4 = "CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, size text)"
cursor.execute(drop_table4)
cursor.execute(create_tables4)

cursor.execute("INSERT INTO product VALUES (1, 'Mouse', 'Pequeño')")
cursor.execute("INSERT INTO product VALUES (2, 'Teclado', 'Gamer')")
cursor.execute("INSERT INTO product VALUES (3, 'Laptop', 'Mediano')")

conexion.commit()

conexion.close()