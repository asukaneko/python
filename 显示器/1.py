from luma.oled.serial import i2c
from luma.oled.device import ssd1306
from luma.oled.render import canvas
from datetime import datetime

a = datetime.now()
serial = i2c(port=1,address=0x3C)
devices = ssd1306(serial)

while True:
    with canvas(devices) as draw:
        draw.rectangle(devices.bounding_box,outline="white",fill="black")
        draw.text((30,40),"杨诗哲",fill="white")
        draw.text((60,40),"{}".format(a),fill="white")
