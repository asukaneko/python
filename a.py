import machine
import random
from machine import Pin,SoftI2C
from ssd1306 import SSD1306_I2C
import time
i2c=SoftI2C(scl=Pin(0),sda=Pin(1))
oled=SSD1306_I2C(128,64,i2c)
but = Pin(2,Pin.IN)#定义按键
get_time = time.time()#显示用到的游戏时间
game_time = time.time()#用于
jump = 0#刷新率为40，跳起时每秒加1，等效于计时器作用（写的时候还不会计时器）
jump_num = [0,8,15,21,25,29,32,34,35]#跳起高度，类似于二次方程，模拟重力加速度
down = False#用于判断jump自加还是自减
score = 0#分数
max_score=-111
gameover = False#判断游戏结束
far = 0#距离，很多用处

'''
障碍物的想法是每个障碍物之间最少距离40，宽度8，三个总长超过
屏幕宽度128，这样就不会同时出现四个，所以只创建三个，当第1
个障碍物跑完屏幕的同时将此时的第2个障碍物定义为第1个，第3个
定义为第2个，然后再创建第3个。就做到实际上就三个障碍物轮番跑
'''
box1 = random.randint(40,120)
box2 = random.randint(40,120) + box1
box3 = random.randint(40,120) + box2
speed = 2#速度（障碍物每帧移动的像素点）

while True:
    if not gameover:
        #触发跳起动作
        if but.value() and jump == 0:
            jump = 1
        if jump != 0:
            jump += 1 if not down else -1
            if jump == 0:
                down = False
                score += 1
        if jump == 8:
            down = True#跳到最高点下落
        
        far += speed#移动的距离按速度累加（实际是障碍物移动的距离）
        score = far//30#本来分数==时间然后感觉太蠢了就随便写个东西，直接用far太容易把字符挤出了
        speed = 2 + score//100#每过100分速度加1
        
        oled.fill(0)#我用的SSD1306太捞了没有clear函数T^T
        oled.line(0,63,128,63,1)#最底下那条线
        #画分数和时间
        oled.text('SCORE:'+str(score),0,1)
        get_time = 'TIME:'+str(int(time.time()-game_time))
        oled.text(get_time,140-len(get_time)*10,1)
        #画小恐龙的外形
        for i in range(6):
            oled.line(15-i,51-jump_num[jump],15-i,58-jump_num[jump],1)
            oled.line(17-i,51-jump_num[jump],17-i,54-jump_num[jump],1)
            oled.line(11-i,55-jump_num[jump],11,58-jump_num[jump],1)
        oled.line(14,55-jump_num[jump],14,60-jump_num[jump],1)
        oled.line(10,55-jump_num[jump],10,60-jump_num[jump],1)
        oled.line(14,52-jump_num[jump],14,53-jump_num[jump],0)
        oled.line(13,52-jump_num[jump],13,53-jump_num[jump],0)
        
        #画障碍物
        for i in range(8):
            oled.line(i+box1-far,55,i+box1-far,61,1)
        
        for i in range(8):
            oled.line(i+box2-far,55,i+box2-far,61,1)
        
        for i in range(8):
            oled.line(i+box3-far,55,i+box3-far,61,1)
        #判断当前障碍物过了屏幕，就把它变最后一个
        if box1+8-far <= 0:
            box1 = box2 
            box2 = box3 
            box3 = box2 + random.randint(40,120)
        #判断是否碰到障碍物
        if 14 > box1-far > 2 and 60-jump_num[jump] > 55:
            gameover = True

    else:
        if score>max_score:
            max_score=score
        oled.text('GAME_OVER',128//2-35,30)
        oled.text("Max Score:{}".format(max_score),128//2-45,40)
        #再次按下按钮初始化并重新开始
        if but.value():
            score = 0
            game_time = time.time()
            gameover = False
            far = 0
            box1 = random.randint(50,120)
            box2 = random.randint(50,120) + box1
            box3 = random.randint(50,120) + box2
            speed = 2
            continue
        
    time.sleep(1/40)
    oled.show()
