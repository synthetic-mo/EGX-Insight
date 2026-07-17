import yfinance as yf

cib = yf.Ticker("COMI.CA")

price = cib.info.get("regularMarketPrice")

print(f"COMI.CA Current price is: {price} EGP")