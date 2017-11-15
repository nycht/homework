import smtplib
import email.mime.multipart
import email.mime.text
import time
def sleeptime(min,sec):
    return min*60+sec;
second = sleeptime(0,3);
while 1 == 1:
    time.sleep(second);
    count = 0
    while  (count < 999999):
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = 'nycht@sina.com'
        msg['to'] = '552010694@qq.com'
        msg['subject'] = 'emmmmm,'
        content = '''''
        emmmmm
        '''
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        smtp = smtplib
        smtp = smtplib.SMTP()
        smtp.connect('smtp.sina.com', '25')
        smtp.login('nycht@sina.com', 'qwe1230')
        smtp.sendmail('nycht@sina.com', '552010694@qq.com', str(msg))
        smtp.quit()
    count = count+1
    print("邮件发送第",count,"次")
print("邮件发送完毕，Thinks")
