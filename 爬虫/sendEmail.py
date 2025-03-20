import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
#发件人
sender = 'ycssbc@163.com'
#客户端授权码：需要在注册邮箱后，登录进入->设置->常规设置->客户端授权码 里面进行设置
authCode = 'TNqC29bkXuU3nyQP'
 
#email：收件人，message:发送内容
def sendEmail(email, message,subject):
    #print("sendEmailMessage, emial:" + email + "，message:" + message)
    messageObj = MIMEText(message, "plain", "utf-8")
    #设置主题
    messageObj['Subject'] = Header(subject, "utf-8")
    #设置发件人
    messageObj['From'] = sender
    #设置收件人
    messageObj['To'] = email
    while True:
        try:
            #建立客户端
            smtpObj = smtplib.SMTP()
            #连接
            #此处是网易126邮箱，使用163邮箱则为smtp.163.com
            smtpObj.connect('smtp.163.com')
            #认证
            smtpObj.login(sender, authCode)
            #发送邮件
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            #断开连接
            smtpObj.close()
            print("成功发送邮件")
            break
        except smtplib.SMTPException as ex:
            print("发送邮件失败")
            #print(ex)
            
if __name__ == '__main__' :
    #验证
    sendEmail("2645229359@qq.com","test邮箱是否可以调用")
