import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from datetime import datetime
import itchat
import xlrd
from apscheduler.schedulers.background import BlockingScheduler

def SentChatRoomsMsg(name, context):
    itchat.get_chatrooms(update=True)
    iRoom = itchat.search_chatrooms(name)
    for room in iRoom:
        if room['NickName'] == name:
            userName = room['UserName']
            break
    itchat.send_msg(context, userName)
    print("发送时间：" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        "发送到：" + name + "\n"
        "发送内容：" + context)
    print("\n*********************************************************************\n")
    scheduler.print_jobs()

def loginCallback():
    print("登录成功")

def exitCallback():
    print("退出成功")

itchat.auto_login(hotReload=True, loginCallback=loginCallback, exitCallback=exitCallback)
#itchat.auto_login(hotReload=True, enableCmdQR=True, loginCallback=loginCallback, exitCallback=exitCallback)
workbook = xlrd.open_workbook("/home/pi/WeChat/AutoSentChatroom.xlsx")
sheet = workbook.sheet_by_name('Chatrooms')
iRows = sheet.nrows

scheduler = BlockingScheduler()
index = 1
for i in range(1, iRows):
    textList = sheet.row_values(i)
    name = textList[0]
    context = textList[2]
    float_dateTime = textList[1]
    date_value = xlrd.xldate_as_tuple(float_dateTime, workbook.datemode)
    date_value = datetime(*date_value[:5])
    if datetime.now() > date_value:
        continue
    date_value = date_value.strftime('%Y-%m-%d %H:%M:%S')
    textList[1] = date_value
    scheduler.add_job(SentChatRoomsMsg, 'date', run_date=date_value, kwargs={"name": name, "context": context})
    print("任务" + str(index) + "\n待发送时间：" + date_value + "\n待发送到：" + name + "\n待发送内容：" + context)
    print("\n*********************************************************************\n")
    index = index + 1

if index == 1:
    print("***没有任务需要执行***")
scheduler.start()
