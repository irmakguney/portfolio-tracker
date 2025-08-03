#!/opt/anaconda3/bin/python

import yfinance as yf

def fiyat_cek(ticker):
    data = yf.download(ticker, period="1d", interval="1m", auto_adjust=True)
    if not data.empty and "Close" in data.columns:
        fiyat = data["Close"].iloc[-1]
        return float(fiyat)
    return None

while True:
    sembol = input("Canlı fiyatını görmek istediğin sembolü gir (örnek: BTC-USD, AAPL) veya çıkmak için 'q' yaz: ").strip().upper()
    
    # Burada çıkış kontrolü kesinlikle önce yapılmalı
    if sembol in ["", "Q", "EXIT"]:
        print("Programdan çıkılıyor...")
        break
    
    fiyat = fiyat_cek(sembol)
    if fiyat is not None:
        print(f"{sembol} güncel fiyatı: {fiyat} USD")
    else:
        print("Veri alınamadı. Sembolü kontrol et.")

