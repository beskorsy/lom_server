import requests
import time

url = 'http://localhost:8000/requestadd/'

data = ({'phone': '+79039225020',
         'loader': False,
         'cutter': False,
         'calculatedInPlace': False,
         'discount': '50',
         'locality': 'Зея',
         'address': 'Зея, ул. Убивцев',
         'scrapyard': 'Белогорск',
         'distantce': '123',
         'transport': 'Варавайка',
         'cost': '12000',
         'tonn': '6',
         'data': '20.05.18',
         'comment': 'ой коммент коммент',
         })
res = requests.post(url, json=data)
time.sleep(1)



