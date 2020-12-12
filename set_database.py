import sqlite3

conexion = sqlite3.connect('data.db')

cursor = conexion.cursor()

drop_table = "DROP TABLE IF EXISTS usuario;"
create_table = "CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario text, contrasena text)"
cursor.execute(drop_table)
cursor.execute(create_table)

drop_table2 = "DROP TABLE IF EXISTS producto;"
create_tables2 = "CREATE TABLE IF NOT EXISTS producto (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, valor real, category_id INTEGER)"
cursor.execute(drop_table2)
cursor.execute(create_tables2)

drop_table3 = "DROP TABLE IF EXISTS categoria;"
create_tables3 = "CREATE TABLE IF NOT EXISTS categoria (id INTEGER PRIMARY KEY AUTOINCREMENT, name text)"
cursor.execute(drop_table3)
cursor.execute(create_tables3)

conexion.commit()

conexion.close()