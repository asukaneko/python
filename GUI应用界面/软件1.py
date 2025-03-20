import PySimpleGUI as sg
import jfc


sg.ChangeLookAndFeel('LightGreen')
ok_btn = sg.SimpleButton('开始计算', size=(10, 2), font=("微软雅黑", 12), button_color=('white', 'firebrick3'))
cancel_btn = sg.Button('关闭程序', size=(10, 2), font=("微软雅黑", 12))
layout = [
    [sg.Text('一元一次方程，一元二次方程计算(ง •̀_•́)ง', font='Courier 12', text_color='blue', background_color='white')],
    [sg.Text('所有输入的内容必须是数字，不能是字符和字符串', font='Courier 12', text_color='blue', background_color='white')],
    [sg.Text('所有的方程都是ax2+bx+c=0的形式，一元一次方', font='Courier 12', text_color='blue', background_color='white')],
    [sg.Text('程是bx+c=0的形式（a=0）', font='Courier 12', text_color='blue', background_color='white')],
    [sg.Text('如果要做图的话，只能重复计算一次,还要导入ma\ntplotlib库，可以用pip3 install 导入', font='Courier 12', text_color='blue', background_color='white')],
    [sg.Input('重复计算的次数：')],
    [sg.Input('a:')],
    [sg.Input('b:')],
    [sg.Input('c:')],
    [ok_btn, cancel_btn],[sg.StatusBar('好好学习，天天向上\n编写语言：python ',size=(400,10), font=("微软雅黑", 12))],

]

window = sg.Window('方程计算机', default_element_size=(40, 2), size=(400, 485)).Layout(layout)

handleFunctionlist = ['chuti1BitAdd', 'chuti1BitAddH', 'chuti1Bitsub', 'chutiAdd', 'chutijian', 'allplugsub',
                      'chuti3BitAdd','chuti3BitSub']
while True:
    event, h = window.read()
    if event in ('关闭程序'):
        # User closed the Window or hit the Cancel button
        break
    elif event in ('开始计算'):
        jfc.a(h,a,b,c)
        break

window.close()