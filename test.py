import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info('verification')")
column_names = [row[1] for row in cursor.fetchall()]

conn.close()

print(column_names)
