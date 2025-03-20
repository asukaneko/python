from pywebio.input import *
from pywebio.output import put_text
from os import system,remove
try:
    code = textarea('Code Edit Online', code={'mode': "python",'theme': 'darcula'}, value='# input your code here\n')
    with open('temp.py','w',encoding = 'utf-8') as f:
        f.write(code)
    system('python3 temp.py')
    put_text('成功运行程序')
except Exception as e:
    put_text('运行：错误 at %s' % e)

