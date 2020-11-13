import requests
import json

danni = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
obmin = json.loads(danni.text)


class Converter:
    def __init__(self, type, amount, sale):
        self.type = type
        self.amount = amount
        self.sale = sale

    def convert(self):
        for i in obmin:
            if self.type in i.values():
                if self.sale:
                    return self.amount * float(i['buy'])
                else:
                    return self.amount * float(i['sale'])





choice = bool(0)
con = Converter('EUR', 8, choice)
if choice:
    print("Купити", con.amount, con.type, ":", con.convert(), "грн")
else:
    print("Продати", con.amount, con.type, ":", con.convert(), "грн")
