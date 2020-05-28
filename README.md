# notify-ikea-click-n-collect
Email and SMS notification script for IKEA's Click &amp; Collect Availability during the COVID-19 situation.

---------------------------------------
## Description and Motivation of this Project
I needed a table to work from home and what better option is there than IKEA's 25$ combo LINNMON/ADILS for a student on a budget. 
Because of the COVID-19 quarantine all of IKEA's stores were closed, but they had a new Click & Collect option for select stores. My friends and I were trying that out for weeks, only to be notified that either the store's capacity to take orders were done for the day or that they were out of stock. 
Bummed from the week long searches and wait, a little reddit deep dive couple of days ago since the initial commit of this project made me come across [this post](https://www.reddit.com/r/IKEA/comments/gpl3x0/ikea_click_collect_status_website/). That post had an [awesome website](https://ikea-status.dong.st/) that turned out to be a life saver! 
We still had to wait for when our closest store was open for Click & Collect. I DID NOT want to wait anymore, even with the convenience of that website. So, ended up checking out how the site gets the information, looked around its source code, and eventually decided to make this project where I can get an email/sms/desktop notification when a particular store gets opened or closed. 

As soon as my closest store's open notification came in, which was luckily late night at a time I don't usually sleep, I jumped on my already open shopping cart and placed the order. It went thrugh and the next day I FINALLY got to pick up my sweet IKEA budget table :).

**Update**: https://ikea-status.dong.st/ now supports email notifcations! Additional updates on notifications will be added according to the developer.

## Usage
First off, if you have a gmail account, you should _Allow less secure apps to be ON_ https://myaccount.google.com/lesssecureapps. You can turn this back off once you're done using this script. 

Modify the ```ikea-stores-notification.py``` scripts variables with your email, password and the necessary emails and mobile number you wish to receive updates on.
The ```msg.py``` has a ```carriers``` variable that you can change too if your carrier isn't there. 

Once you set all the variables right, you can run the code and wait for a notification on when your closest store will open.

**Needs Python 3 to run.** 
**Required modules**:
- requests
- plyer

## Future Work
- Make a CLI out of this? 
- Add script for notifications on a specific or specific stores
- Refactor and increase modularity of code?
  
## References
This project's code was mixed up and referenced from places mentioned below.
- https://ikea-status.dong.st/
- https://plyer.readthedocs.io/en/latest/#plyer.facades.Notification
- https://www.reddit.com/r/Python/comments/8gb88e/free_alternatives_to_twilio_for_sending_text/dyaguc6?utm_source=share&utm_medium=web2x
- https://realpython.com/python-send-email/
- https://discuss.python.org/t/parse-z-timezone-suffix-in-datetime/2220
