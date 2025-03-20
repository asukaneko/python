import random
import time
import datetime
from concurrent.futures import ThreadPoolExecutor
import sqlite3

executor = ThreadPoolExecutor(max_workers=2)

def a():
    try:
        import bof
        bof.bf()
    except Exception:
        print("没有找到播放文件")


cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
cards2 = [10,11,12,13,14,15,16,17,18,19,20]
cards3 = [14,15,16,17,18,19,20,21,22,23]
cards4 = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10',
          'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10',
          'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10',
          'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10']
cards5 = ['A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15',
         'B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15',
         'C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15',
         'D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15']


d1 = {'A':4,'B':3,'C':2,'D':1}
d2 = {1:'简单',2:'中级',3:'困难',4:'高级玩法'}
d3 = {1:'简单',2:'困难'}

p1 = []
p2 = []
win1 = 0
win2 = 0
q = []

print(datetime.date.today())


nan = input("选择难度(1:简单，2：中级，3：困难，4：高级玩法)：")
while True:
    try:
        nan = int(nan)
        while True:
            if nan > 4:
                print("在1--4中选择！！")
                nan = int(input("选择难度(1:简单，2：中级，3：困难，4：高级玩法)："))
            else:
                break
        break
    except ValueError:
        print("必须为整数,且在1——4中")
        nan = input("选择难度(1:简单，2：中级，3：困难，4：高级玩法)：")

if nan == 4:
    nd = input("选择难度(1:简单；2：困难):")
    while True:
        try:
            nd = int(nd)
            while True:
                if nd > 2:
                    print("在1--2中选择！！")
                    nd = int(input("选择难度(1:简单，2：困难)："))
                else:
                    break
            break
        except ValueError:
            print("必须为整数")
            nd = input("选择难度(1:简单；2：困难):")

if nan != 4:
    for i in range(13):
        card1 = random.choice(cards)
        p1.append(card1)
elif nan == 4:
    for i in range(13):
        card1 = random.choice(cards4)
        p1.append(card1)
    
try:
    with open('wins.txt','r') as f:
        fd = f.read()
        print("上一次比赛，{}".format(fd[-25:]))
except Exception:
    print("没有比赛记录，将会创建，请勿删除")
    pass

time.sleep(2)

if nan == 1:
    for i in range(13):
        card2 = random.choice(cards)
        p2.append(card2)
elif nan == 2:
    for i in range(13):
        card2 = random.choice(cards2)
        p2.append(card2)
elif nan == 3:
    for i in range(13):
        card2 = random.choice(cards3)
        p2.append(card2)
elif nan == 4:
    print("加入A,B,C,D四个值，A>B>C>D,当出相同的牌时，按照值的大小比较")
    print("输入的字母要大写！！！")
    time.sleep(2)
    if nd == 1:
        for i in range(13):
            card2 = random.choice(cards4)
            p2.append(card2)
    if nd == 2:
        for i in range(13):
            card2 = random.choice(cards5)
            p2.append(card2)



print("游戏规则:玩家为p1,电脑为p2,每人有13张牌，电脑随机出牌，只有当玩家牌大于电脑牌，\
玩家获胜，否则电脑获胜，打完所有的牌，或者赢了7次，即为获胜。")
print(5)
time.sleep(1)
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("比赛开始")
time.sleep(1)

n = 0
if nan != 4:
    while True:
        print("             ")
        print("玩家牌：{}".format(p1))
        n += 1
        print("                   ")
        print("第{}回合".format(n))
        print("                    ")
        r2 = random.choice(p2)
        print("电脑出牌:{}".format(r2))
        q.append(r2)
        p2.remove(r2)
        r1 = input("玩家出牌：")
        while True:
            try:
                r1 = int(r1)
                p1.remove(r1)
                q.append(r1)
                break
            except ValueError:
                print("必须为整数,且必须在牌组中选择卡牌")
                r1 = input("玩家出牌：")
        


        if r1 > r2:
            print("第{}回合结束,玩家获胜".format(n))
            print("电脑剩余牌数：{}".format(len(p2)))
            print("玩家剩余牌数：{}".format(len(p1)))
            print("牌堆：{}".format(q))
            print("                   ")
            win1 += 1
        if r1 == r2:
            print("平局")
            print("电脑剩余牌数：{}".format(len(p2)))
            print("玩家剩余牌数：{}".format(len(p1)))
            print("牌堆：{}".format(q))
        if r1 < r2:
            win2 += 1
            print("第{}回合结束，电脑获胜".format(n))
            print("电脑剩余牌数：{}".format(len(p2)))
            print("玩家剩余牌数：{}".format(len(p1)))
            print("牌堆：{}".format(q))


        if win1 == 7:
            print("游戏结束")
            print("玩家赢了")
            time.sleep(3)
            break
        if win2 == 7:
            print("游戏结束")
            print("电脑赢了")
            time.sleep(3)
            break
        if len(p1) == 0:
            print("游戏结束")
            print("玩家赢了")
            time.sleep(3)
            break
        if len(p2) == 0:
            print("游戏结束")
            print("电脑赢了")
            time.sleep(3)
            break

elif nan == 4:
    while True:
        print("             ")
        print("玩家牌：{}".format(p1))
        n += 1
        print("                   ")
        print("第{}回合".format(n))
        print("                    ")
        r2 = random.choice(p2)
        print("电脑出牌:{}".format(r2))
        q.append(r2)
        p2.remove(r2)
        r1 = input("玩家出牌：")
        while True:
            try:
                p1.remove(r1)
                q.append(r1)
                break
            except ValueError:
                print("字母要大写！！,或者必须出卡牌中有的牌")
                r1 = input("玩家出牌：")

        r2a = r2[0]
        r1a = r1[0]
        if len(r2) == 2:
            r2b = int(r2[1])
        if len(r1) == 2:
            r1b = int(r1[1])
        if len(r2) == 3:
            r2b = int(r2[1:])
        if len(r1) == 3:
            r1b = int(r1[1:])
        
        r2aa = d1.get(r2a)
        r1aa = d1.get(r1a)
        
        if r1b > r2b:
            print("第{}回合结束,玩家获胜".format(n))
            print("电脑剩余牌数：{}".format(len(p2)))
            print("玩家剩余牌数：{}".format(len(p1)))
            print("牌堆：{}".format(q))
            print("                   ")
            win1 += 1
        elif r1b == r2b:
            if r1aa > r2aa:
                print('第{}回合结束，玩家获胜'.format(n))
                print("电脑剩余牌数：{}".format(len(p2)))
                print("玩家剩余牌数：{}".format(len(p1)))
                print("牌堆：{}".format(q))
                print("                      ")
                win1 += 1
            elif r1aa == r2aa:
                print("平局")
                print("电脑剩余牌数：{}".format(len(p2)))
                print("玩家剩余牌数：{}".format(len(p1)))
                print("牌堆：{}".format(q))
            elif r1aa < r2aa:
                print("第{}回合结束，电脑获胜".format(n))
                print("电脑剩余牌数：{}".format(len(p2)))
                print("玩家剩余牌数：{}".format(len(p1)))
                print("牌堆：{}".format(q))
                print("                         ")
                win2 += 1
        elif r1b < r2b:
            print("第{}回合结束，电脑获胜".format(n))
            print("电脑剩余牌数：{}".format(len(p2)))
            print("玩家剩余牌数：{}".format(len(p1)))
            print("牌堆：{}".format(q))
            print("                       ")
            win2 += 1

        if win1 == 7:
            print("游戏结束")
            print("玩家赢了")
            time.sleep(3)
            break
        elif win2 == 7:
            print("游戏结束")
            print("电脑赢了")
            time.sleep(3)
            break
        elif len(p1) == 0:
            print("游戏结束")
            print("玩家赢了")
            time.sleep(3)
            break
        elif len(p2) == 0:
            print("游戏结束")
            print("电脑赢了")
            time.sleep(3)
            break

if nan != 4:
    af = d2.get(nan)
if nan == 4:
    bf = d3.get(nd)

'''with open('wins.txt','at') as f:
    if nan != 4:
        f.write("挑战难度：{} ".format(af))
    if nan == 4:
        f.write("挑战难度：{} ".format(bf))
    f.write("玩家获胜次数：{} ".format(str(win1)))
    f.write("电脑获胜次数：{}".format(str(win2)))
'''

    

print("-"*60)
print("游戏版本:v2.0 Beta")
print("使用语言：Python")
print("时间：2021年2月5日第n次修改")
print("作者：yc")
time.sleep(1)

a()