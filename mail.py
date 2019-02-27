#!/usr/bin/env python3

from email.header import Header
from email.mime.text import MIMEText
import smtplib# 邮件发送
def sendmail(subject, content):
	sender = input('发件人邮箱:')
	password =input('发件人邮箱密码:')
	recipients = input('收件人邮箱:')
	host = 'mail.qianfg.com'# 发件人邮箱主机
	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = sender
	msg['To'] = recipients
	msg['Subject'] = Header(subject, 'utf-8').encode()
	server = smtplib.SMTP_SSL(host, 465)
	server.login(sender, password)
	server.sendmail(sender, [recipients], msg.as_string())
	server.quit()
