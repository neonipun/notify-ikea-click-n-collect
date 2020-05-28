from msg import Message
from collections import defaultdict
import requests
import time

# DO NOT COMMIT FILES WITH CREDENTIALS
email = 'EMAIL'
password = 'PASSWORD'
numbers_carriers = [('0000000000 or 000-000-0000', 'carrier')]

var = "PLZ WORK"
test = Message(subject="Update Text/Test", email=email, password=password)
msg = "Wubba Lubba Dub Dub\n"
for _ in range(5):
    msg += f'Wubba Lubba Dub Dub {var}\n'

ikea_stores = defaultdict(bool)
r = requests.get('https://ikea-status.dong.st/latest.json')
for store in r.json():
    if store['last_open'] and store['last_open'] > store['last_closed']:
        ikea_stores[(store['country'], store['state'], store['name'])] = True

msg += f'First notification from script about IKEA store availability ran at {time.strftime("%d-%b-%Y %H:%M:%S", time.localtime())} Local Time.\n'
for country, state, name in ikea_stores.keys():
    msg += f'{country}, {state}, {name} - OPEN\n'

for number, carrier in numbers_carriers:
    test.send(to_recv=number, carrier=carrier, message=msg)

print('OK')