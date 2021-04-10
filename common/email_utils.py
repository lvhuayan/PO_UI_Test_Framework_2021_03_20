#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: email_utils.py
# @time: 2021/4/10 14:12
# @desc:
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailUtils:
    def __init__(self,smtp_subject,smtp_body,smtp_file_path=None):
        self.smtp_server = 'smtp.qq.com'  # 邮件服务器地址
        self.smtp_sender = '1059856747@qq.com'  # 发件人邮箱名
        self.smtp_senderpassword = 'eyieywcajoxebfid'  # 授权码
        self.smtp_receiver = '1059856747@qq.com,335716673@qq.com'  # 邮件接收人
        self.smtp_cc = '1059856747@qq.com'  # 抄送人
        self.smtp_subject = smtp_subject  # 邮件主题
        self.smtp_body = smtp_body  # 邮件正文
        self.smtp_file = smtp_file_path

    def mail_content(self):
        if self.smtp_file!=None:
            msg = MIMEMultipart()
            with open(self.smtp_file,'rb') as f:
                mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
                mime.add_header('Content-Disposition', 'attachment', filename=('gbk', '', self.smtp_file.split('/')[-1]))
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
            msg.attach(MIMEText(self.smtp_body, 'html', 'utf-8'))
            msg['from'] = self.smtp_sender
            msg['to'] = self.smtp_receiver
            msg['cc'] = self.smtp_cc
            msg['subject'] = self.smtp_subject
            return msg
        else:
            msg=MIMEText(self.smtp_body,'html','utf-8') #邮件信息对象
            msg['from']=self.smtp_sender
            msg['to']=self.smtp_receiver
            msg['cc']=self.smtp_cc
            msg['subject']=self.smtp_subject
            return msg

    def send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_content=self.mail_content()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',') + self.smtp_cc.split(','), mail_content.as_string())
        except  Exception as e:
            print('发送失败')
        smtp.quit()

if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    dri_path = os.path.join(current_path, '..','reports/禅道自动化测试报告.zip')
    EmailUtils('自动化测试报告（正式版）', 'python自动化测试报告', dri_path).send_mail()