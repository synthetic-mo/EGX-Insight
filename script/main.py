import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Initialize the FastAPI application
app = FastAPI()

# 2. Add CORS Middleware 
# This is crucial! Browsers block frontends from talking to backends 
# on different ports unless you explicitly allow it here.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any local frontend port to access this data
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Create your first endpoint (the web address)
@app.get("/api/stocks")
def get_stored_stocks():
    # Connect to your existing SQLite database file
    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()
    
    # Grab all entries from the table
    cursor.execute("SELECT * FROM egx_stocks")
    rows = cursor.fetchall()
    conn.close()
    
    # 4. Format the raw tuples into clean dictionaries (JSON format)
    stocks_list = []
    for row in rows:
        stocks_list.append({
            "ticker": row[0],
            "price": row[1]
        })
        
    return stocks_list