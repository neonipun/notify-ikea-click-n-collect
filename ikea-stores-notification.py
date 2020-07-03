from collections import defaultdict
from msg import Message
from plyer import notification
import time
import requests
import sys 

def sender(messenger, message, receivers_carriers):
    # SMS get Spam filtered for any mention of IKEA, Notification or Store
    sms = Message(subject="Update Text/Test", email=email, password=password) if email and password else None

    for receiver, carrier in receivers_carriers:
        if carrier in {'gmail'} and messenger:
            messenger.send(to_recv=receiver, carrier=carrier, message=message)
        elif sms:
            sms.send(to_recv=receiver, carrier=carrier, message=message)
        
    if notification_flag:
        notification.notify(title='IKEA Stores Notification!', message=message, app_icon='./bell.ico', timeout=30)

# DO NOT COMMIT FILES WITH CREDENTIALS. Modify variables below as necessary.
email = ''
password = ''
notification_flag = True

if not notification_flag and not email and not password:
    sys.exit('Neither of the SMS/Email/Desktop notifications are set.')

receivers_carriers = [('000-000-0000', 'carrier'), ('0000000000', 'carrier'), ('email-ID', 'carrier')]

stores_open = Message(subject="IKEA STORES OPEN!", email=email, password=password) if email and password else None
stores_closed = Message(subject="IKEA STORES CLOSED!", email=email, password=password) if email and password else None

ikea_stores = defaultdict(bool)
r = requests.get('https://api.ikea-status.dong.st/prod/locations')
for store in r.json()['locations']:
    if store['status'] == 'open':
        ikea_stores[(store['countryCode'], store['subdivisionCode'], store['locationName'])] = True

stores_open_msg = f'First notification from script about IKEA Stores availability ran at {time.strftime("%d-%b-%Y %H:%M:%S", time.localtime())} Local Time.\n'
for countryCode, subdivisionCode, locationName in ikea_stores.keys():
    stores_open_msg += f'{countryCode}, {subdivisionCode}, {locationName}: OPEN\n'

sender(stores_open, stores_open_msg, receivers_carriers)

while True:
    stores_open_msg = ''
    stores_closed_msg = ''

    try:
        r = requests.get('https://api.ikea-status.dong.st/prod/locations')    
        for store in r.json()['locations']:
            if ikea_stores[(store['countryCode'], store['subdivisionCode'], store['locationName'])] and (store['status'] == 'closed'):
                ikea_stores[(store['countryCode'], store['subdivisionCode'], store['locationName'])] = False
                stores_closed_msg += f"{store['countryCode']}, {store['subdivisionCode']}, {store['locationName']}: CLOSED\n"
            elif not ikea_stores[(store['countryCode'], store['subdivisionCode'], store['locationName'])] and (store['status'] == 'open'):
                ikea_stores[(store['countryCode'], store['subdivisionCode'], store['locationName'])] = True
                stores_open_msg += f"{store['countryCode']}, {store['subdivisionCode']}, {store['locationName']}: OPEN\n"
    except Exception as e:
        print("Exception:", e)
        pass
    
    if stores_open_msg:
        sender(stores_open, stores_open_msg, receivers_carriers)
    
    if stores_closed_msg:
        sender(stores_closed, stores_closed_msg, receivers_carriers)
    
    print('OK')
    time.sleep(45)