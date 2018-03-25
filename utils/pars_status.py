import xml.etree.ElementTree as ET
import requests
import time

tree = ET.parse('status.xml')
root = tree.getroot()
url = 'http://localhost:8000/customerupdate/1'

for child in root.findall('chel'):
    telefon = "+7" + child.find('telefon').text
    doplata = child.find('doplata').text
    data = ({"phone": telefon, "discount": doplata})
    res = requests.post(url, json=data)
    time.sleep(1)
