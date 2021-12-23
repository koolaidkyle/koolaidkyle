import requests
import tkinter as tk
from datetime import datetime

symbol = input('Enter crypto symbol(ie BTC): ').upper()
if len(symbol) < 1 : symbol = 'BTC'
exchange = input('Enter exchange currency(ie USD): ').upper()
if len(exchange) < 1 : exchange = 'USD'

def track_crypto():
    url = f'https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms={exchange}'
    raw = requests.get(url).json()
    price = raw[exchange]
    time = datetime.now().strftime('%H:%M:%S')

    labelPrice.config(text = str(price) + f': {exchange}')
    labelTime.config(text = 'Updated at: ' + time)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title('Crypto Tracker')

f1 = ("century gothic", 24, "bold")
f2 = ("century gothic", 22)
f3 = ("century gothic", 18)

label = tk.Label(canvas, text = f"{symbol} Price", font = f1)
label.pack(pady = 20)

labelPrice = tk.Label(canvas, font = f2)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack(pady = 20)

track_crypto()

canvas.mainloop()
