import sqlite3

conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM egx_stocks")
rows = cursor.fetchall()


print("--- Current Database Content ---")
for row in rows:
    print(row)


conn.close()