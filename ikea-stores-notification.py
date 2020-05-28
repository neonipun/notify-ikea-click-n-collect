from collections import defaultdict
from msg import Message
from plyer import notification
import time
import requests
import sys 

def sender(messenger, message, receivers_carriers):
    # SMSs get Spam filtered for any mention of IKEA, Notification or Store with tmobile carries for some reason.
    sms = Message(subject="Update Text/Test", email=email, password=password)

    for receiver, carrier in receivers_carriers:
        if carrier in {'gmail'}:
            messenger.send(to_recv=receiver, carrier=carrier, message=message)
            continue
        sms.send(to_recv=receiver, carrier=carrier, message=message)

    # For Desktop notifications   
    if notification_flag:
        notification.notify(title='IKEA Stores Notification!', message=message, app_icon='./bell.ico', timeout=30)

# DO NOT COMMIT FILES WITH CREDENTIALS. Modify variables below as necessary.
email = 'EMAIL'
password = 'PASSWORD'
notification_flag = True
receivers_carriers = [('000-000-0000', 'carrier'), ('0000000000', 'carrier'), ('email-ID', 'carrier')]

stores_open = Message(subject="IKEA STORES OPEN!", email=email, password=password)
stores_closed = Message(subject="IKEA STORES CLOSED!", email=email, password=password)

ikea_stores = defaultdict(bool)
r = requests.get('https://ikea-status.dong.st/latest.json')
for store in r.json():
    if store['last_open'] and store['last_open'] > store['last_closed']:
        ikea_stores[(store['country'], store['state'], store['name'])] = True

stores_open_msg = f'First notification from script about IKEA Stores availability ran at {time.strftime("%d-%b-%Y %H:%M:%S", time.localtime())} Local Time.\n'
for country, state, name in ikea_stores.keys():
    stores_open_msg += f'{country}, {state}, {name}: OPEN\n'

sender(stores_open, stores_open_msg, receivers_carriers)

while True:
    stores_open_msg = ''
    stores_closed_msg = ''
    r = requests.get('https://ikea-status.dong.st/latest.json')    
    for store in r.json():
        if ikea_stores[(store['country'], store['state'], store['name'])] and (store['last_open'] and store['last_open'] < store['last_closed']):
            ikea_stores[(store['country'], store['state'], store['name'])] = False
            stores_closed_msg += f"{store['country']}, {store['state']}, {store['name']}: CLOSED\n"
        elif not ikea_stores[(store['country'], store['state'], store['name'])] and (store['last_open'] and store['last_open'] > store['last_closed']):
            ikea_stores[(store['country'], store['state'], store['name'])] = True
            stores_open_msg += f"{store['country']}, {store['state']}, {store['name']}: OPEN\n"
    
    if stores_open_msg:
        sender(stores_open, stores_open_msg, receivers_carriers)
    
    if stores_closed_msg:
        sender(stores_closed, stores_closed_msg, receivers_carriers)
    
    print('OK')
    time.sleep(45)