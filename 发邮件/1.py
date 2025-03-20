import sendEmail

def worker():
    with open('/home/pi/wen/bb.txt','r',encoding='gbk') as f:
        a = f.read()
        
    sendEmail.sendEmail(a)

if __name__ == '__main__':
    worker()