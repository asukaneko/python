from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

mask=np.array(Image.open("/home/pi/server0/file/BB29EC41-BE37-475E-A3E4-BA6D33DEA2EB.jpeg"))
text= open("/home/pi/wen/xiaoshuo.1/嫌疑犯X的献身/第一卷 一卷全.txt",encoding='gbk',errors='ignore').read()
font = r'/home/pi/1.ttf'
wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2,background_color='white').generate(text.lower())

plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('wordcloud.png') 
