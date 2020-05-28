# notify-ikea-click-n-collect
Email and SMS notification script for IKEA's Click &amp; Collect Availability during the COVID-19 situation.

---------------------------------------
## Description and Motivation of this Project
I needed a table to work from home and what better option is there than IKEA's 25$ combo LINNMON/ADILS for a student on a budget. 
Because of the COVID-19 quarantine all of IKEA's stores were closed, but they had a new Click & Collect option for select stores. My friends and I were trying that out for weeks, only to be notified that either the store's capacity to take orders were done for the day or that they were out of stock. 
Bummed from the week long searches and wait, a little reddit deep dive couple of days ago since the initial commit of this project made me come across [this post](https://www.reddit.com/r/IKEA/comments/gpl3x0/ikea_click_collect_status_website/). That post had an [awesome website](https://ikea-status.dong.st/) that turned out to be a life saver! 
We still had to wait for when our closest store was open for Click & Collect. I DID NOT want to wait anymore, even with the convenience of that website. So, ended up checking out how the site gets the information, looked around its source code, and eventually decided to make this project where I can get an email/sms/desktop notification when a particular store gets opened or closed. 

As soon as my closest store's open notification came in, which was luckily late night at a time I don't usually sleep, I jumped on my already open shopping cart and placed the order. It went thrugh and the next day I FINALLY got to pick up my sweet IKEA budget table :).

## References
This project's code was mixed up and referenced from places mentioned below.
- https://ikea-status.dong.st/
- https://plyer.readthedocs.io/en/latest/#plyer.facades.Notification
- https://www.reddit.com/r/Python/comments/8gb88e/free_alternatives_to_twilio_for_sending_text/dyaguc6?utm_source=share&utm_medium=web2x
- https://realpython.com/python-send-email/
- https://discuss.python.org/t/parse-z-timezone-suffix-in-datetime/2220
