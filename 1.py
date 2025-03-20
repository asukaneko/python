from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import datetime
from PIL import ImageFont
import sendEmail
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
gpio = 18
font1 = ImageFont.truetype('2.ttf',15)
font2 = ImageFont.truetype('1.ttf', 28)
font3 = ImageFont.truetype('3.ttf', 15)

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
while True:
    d = datetime.datetime.now()
    d = str(d)
    d1 = d[:10]
    d2 = d[11:-7]
    q = int(d[17:-7])
    
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box,outline="white",fill="black") 
        draw.text((28, 20),d1,font=font3,fill="white")
        draw.text((38,40),d2,font=font3,fill="white")
        
        draw.text((0,0),'电脑温度:',font=font1,fill='white')
        with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
            temp = int(f.read()) / 1000
            temp = str(temp)[:4]
        draw.text((73,0),temp,font=font3,fill='white')
    if isinstance(q/10,int):
        sendEmail.sendEmail('2645229359@qq.com','电脑温度:{}'.format(temp))
        print('发送成功')
        '''
        draw.text((0,10),'-'*30,font=font3,fill='white')
        draw.text((0,22),'环境温度:',font=font1,fill='white')
        draw.text((0,30),'-'*30,font=font3,fill='white')
        draw.text((0,44),'环境湿度:',font=font1,fill='white')
        
        hum,tem = Adafruit_DHT.read_retry(sensor,gpio)
        if hum is not None and tem is not None:
            draw.text((73,22),tem,font=font3,fill='white')
            draw.text((73,22),hum,font=font3,fill='white')
        
        with open('/media/pi/03FC-7193/a.txt','r') as f:
            a = f.read()
            a = a[27:-4]
        draw.text((0,10),'下载页数:',font=font1,fill='white')
        draw.text((73,10),a,font=font3,fill='white')
        '''
