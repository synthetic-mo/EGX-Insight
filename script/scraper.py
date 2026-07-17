import sqlite3
import yfinance as yf

cib = yf.Ticker("COMI.CA")

price = cib.info.get("regularMarketPrice")

conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS egx_stocks (
        ticker TEXT PRIMARY KEY,
        price REAL
        )


""")

cursor.execute("""
    INSERT OR REPLACE INTO egx_stocks (ticker, price)
    VALUES (?, ?)
""", ("COMI.CA", price))


conn.commit()
conn.close()

print("Successfully saved COMI.CA to the SQL database!")