import os
     
print("内置函数：播放音乐（bfyy），解决apt占用（x）,玩cardgame(cardgame),解方程（jfc）")


def bfyy():
    print("播放音乐")
    a = input("路径+音乐名:")
    os.system("mpv {}".format(a))

def x():
    print("解决apt占用")
    os.system("sudo rm /var/cache/apt/archives/lock")
    os.system("sudo rm /var/lib/dpkg/lock")

def cardgame():
    print("玩cardgame")
    import cardgame2
    #cardgame2.a()
    cardgame2.b()

def jfc():
    print("解方程和绘制图像")
    import sd
    import jfc   
