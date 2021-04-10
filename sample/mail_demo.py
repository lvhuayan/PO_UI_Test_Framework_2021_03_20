#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: mail_demo.py
# @time: 2021/4/10 11:51
# @desc:
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

current_path=os.path.dirname(__file__)
dri_path=os.path.join(current_path,'../reports/禅道自动化的是报告V1.4/禅道自动化的是报告.zip')
print(dri_path)

smtp_server='smtp.qq.com' #邮件服务器地址
smtp_sender='1059856747@qq.com'#发件人邮箱名
smtp_senderpassword='eyieywcajoxebfid'#授权码
smtp_receiver='1059856747@qq.com,335716673@qq.com'#邮件接收人
smtp_cc='1059856747@qq.com'#抄送人
smtp_subject='自动化测试报告（测试版）'#邮件主题
smtp_body='来自Python邮件测试' #邮件正文
stmp_file=dri_path

# msg=MIMEText(smtp_body,'html','utf-8') #邮件信息对象
# msg['from']=smtp_sender
# msg['to']=smtp_receiver
# msg['cc']=smtp_cc
# msg['subject']=smtp_subject

msg=MIMEMultipart()
with open(stmp_file,'rb') as f:
    # F: / PO_UI_Test_Framework_2021_03_20 /reports/禅道自动化的是报告V1.4/禅道自动化的是报告.zip
    mime=MIMEBase('zip','zip',filename=stmp_file.split('/')[-1])
    mime.add_header('Content-Disposition','attachment',filename=('gbk','',sstmp_file.split('/')[-1]))
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
msg.attach(MIMEText(smtp_body,'html','utf-8'))
msg['from']=smtp_sender
msg['to']=smtp_receiver
msg['cc']=smtp_cc
msg['subject']=smtp_subject

smtp=smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender,password=smtp_senderpassword)
smtp.sendmail(smtp_sender,smtp_receiver.split(',')+smtp_cc.split(','),msg.as_string())


