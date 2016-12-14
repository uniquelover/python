#!/usr/bin/python
# coding:utf-8

import smtplib
from email.header import Header
from email.mime.text import MIMEText

def send_mail(message):
    smtp_info = {}
    server = smtplib.SMTP('smtp.163.com', 25)
    server.login('uniquelover@163.com', 'tt12131417')
    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = '499350242@qq.com'
    msg['Subject'] = Header(u'text', 'utf8').encode()
    msg['To'] = u'√Œ‘⁄±À∞∂ <499350242@qq.com>'
    try:
        server.sendmail('uniquelover@163.com', ['499350242@qq.com'], msg.as_string())	
    except smtplib.SMTPException as e:
        print str(e)
        print "Error,failed to send mail"	
    else:
        print "send mail successfully!"
		
if __name__ == '__main__':
    send_mail("this only for testing!!!")		