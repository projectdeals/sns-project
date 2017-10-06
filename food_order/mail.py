
from email.mime.text import MIMEText

import smtplib


def send_mail(email,user_name,item_name,price,total):

    from_email = "rrj8335@gmail.com"
    from_pass = "44201998"
    to_mail = "rsnk2013@gmail.com"
    msg = " <h3>Hi, "+ user_name+",</h3><br><br>"
    msg=msg+"<table border='1'><tr><th>Item</th><th>Price</th></tr>"
    subject ="Order details"
    for i,j in zip(item_name,price):
        msg +="<tr><td>"+str(i)+"</td><td>"+str(j)+"</td></tr>"
    msg +="</table><br><h5>You must pay " + str(total) + "</h5>"

    message = MIMEText(msg,'html')
    message['subject'] = subject
    message['to'] = to_mail
    message['from'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_pass)
    gmail.send_message(message)

