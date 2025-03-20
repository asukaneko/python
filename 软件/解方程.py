import math
import time
import datetime

try:
    import sd
except Exception:
    pass

def result(a,b,c):
    derat = b**2-4*a*c
    if a == 0:
        if b != 0:
            x = -c / b
            x = float('%.3f' % x)
            return x
        else:
            return '无解'
                
    else:
        if derat < 0:
            return '无实根 '
        elif derat == 0:
            x = (-b-math.sqrt(derat))/2*a
            return x
        else:
            xone = (-b+math.sqrt(derat))/2*a
            xtwo = (-b-math.sqrt(derat))/2*a
            xone = float('%.4f' % xone)
            xtwo = float('%.4f' % xtwo)
            return xone,xtwo

print(datetime.date.today())

print("一元一次方程，一元二次方程计算(ง •̀_•́)ง")
time.sleep(1)

print("所有输入的内容必须是数字，不能是字符和字符串ԅ(¯ㅂ¯ԅ)")
time.sleep(2)

print("所有的方程都是ax2+bx+c=0的形式，一元一次方程是bx+c=0的形式（a=0）٩( 'ω' )و ")
time.sleep(2)
print("如果要做图的话，只能重复计算一次,还要导入matplotlib库，可以用pip3 install 导入")
time.sleep(2)

h = input("重复计算的次数：")
while True:
    try:
        h = int(h)
        break
    except ValueError:
        print("输入的必须是数字")
        h = input("重复计算的次数：")
        
n = 0
for i in range(h):
    print("                                                ")
    print("---------------------start----------------------")
    q = input("按q退出，任意键继续:")
    if q == "q":
        break
    n += 1
    print("第{}次计算".format(n))

    a = input('a的值：')
    while True:
        try:
            a = float(a)
            break
        except ValueError:
            print("必须输入数字")
            a = input('a的值：')
    
    b = input('b的值：')
    while True:
        try:
            b = float(b)
            if a == 0:
                if b != 0:
                    break
                else:
                    print("b不能为0")
                    b = input('b的值：')
            else:
                break
        except ValueError:
            print("必须输入数字")
            b = input('b的值：')
  
    c = input('c的值：')
    while True:
        try:
            c = float(c)
            break
        except ValueError:
            print("必须输入数字")
            c = input('c的值：')
    print("                                                          ")
    print("-------------------result{}---------------------".format(n))
    print("x = {}".format(result(a,b,c)))
    
    print("此方程的函数图像相关信息：")
    if a > 0:
        print("  开口向上")
    elif a < 0:
        print("  开口向下")
    if a != 0:
        d = -(b/(a+a))
        d = float('%.4f' % d)
    if a == 0:
        d = -c/b
        d = float('%.4f' % d)
    if a != 0:
        print("  对称轴是x={}".format(d))
    if a != 0:
        f = (4*a*c-b**2)/4*a
        print("  顶点坐标：（{}，{}）".format(d,f))

    if a > 0:
        print("  当x>{}时，y随x的增大而增大;当x<{}时，y随x的增大而减小。".format(d,d))
        print("  当x={}时，y有最小值{}".format(d,f))
    elif a < 0:
        print("  当x>{}时，y随x的增大而减小；当x<{}时，y随x的增大er增大。".format(d,d))
        print("  当x={}时，y有最大值{}".format(d,f))
    elif b > 0:
        print("  y随x的增大而增大")
    elif b < 0:
        print("  y随x的增大而减小")
    
    print("  与y轴的交点是(0，{})".format(c))

    if a != 0:
        print("  根与系数的关系")
        p = -b/a
        p = float('%.3f' % p)
        print("   x1 + x2 = {}".format(p))
        q = c/a
        q = float('%.3f' % q)
        print("   x1 x x2 = {}".format(q))
    print("注：0.3333就是三分之一，06667就是三分之二，有些循环小数可用分数代替")
    try:
        sd.a(d,a,b,c)
    except Exception:
        print("没有做图工具")
        pass
  
print("计算已完成✺◟(∗❛ัᴗ❛ั∗)◞✺")
print("版本：v2.0")
print("更新内容：支持做图！！")
time.sleep(2)

q2 = input("按e退出：")
if q2 != "e":
    sd = 0
    for i in range(2000):
        sd += 1
        print("按e退出{}！！！！！！！".format(sd))
        time.sleep(0.001)
    print("下次记得一定要按e退出！")
    time.sleep(2)

    
