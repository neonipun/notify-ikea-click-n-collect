import smtplib, ssl, sys

class Message:
    # Carriers can be added as necessary
    carriers = {
        'att':    '@mms.att.net',
        'tmobile':' @tmomail.net',
        'verizon':  '@vtext.com',
        'sprint':   '@page.nextel.com', 
        'gmail': '@gmail.com'
        }
    
    def __init__(self, message='DEFAULT-MESSAGE', subject='DEFAULT-SUBJECT', email='', password=''):
        self.message = f'Subject: {subject}\n\n{message}'
        self.subject = subject
        self.__email = email
        self.__password = password

    def send(self, to_recv, carrier, message=''):
        to_recv += self.carriers[carrier]
        msg = f'Subject: {self.subject}\n\n{message}' if message else self.message
       
        try:                        
            # Create a secure SSL context
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.__email, self.__password)
                server.sendmail(self.__email, to_recv, msg.encode('utf-8'))

        except Exception as e:
            sys.exit('Exception: '+str(e))