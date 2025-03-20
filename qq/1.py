import qqbot 
from qqbot import QQBotSlot as qqbotslot, RunBot 
from qqbot import _bot as bot 
import time 
import json 
import urllib
 
 
keyList = ['签到', '打卡', '在', ] # 匹配关键字
 
def check(keylist, str):
    for key in keyList:
        if (key in str):
            return True
    return False
 
@qqbot.QQBotSlot 
def onQQMessage(bot, contact, member, content):
    # bot: QQBot对象，提供List / SendTo / Stop / Restart等接口 contact: 
    # QContact对象，消息的发送者，具有ctype / qq / uin / nick / mark / card 
    # / name等属性 member: 
    # QContact对象，仅当本消息为群消息或讨论组消息时有效，代表实际发消息的成员 
    # content: str对象，消息内容
    if '@ME' in content: # 如果有人艾特的机器人
        message = content.replace('[@ME] ', '')
        # 添加名字的ASCII码，能够进行语义的连贯，而不是突兀的开启另外一段对话
        asciistr = ''
        for i in range(len(member.name)):
            asciistr += (str(ord(member.name[i]))) # 组装名字的字符编码，尽量的是唯一的
            if i > 3:
                break
        # 调用图灵机器人，进行对话的回复，如果出现图灵机器人，替换为浮沉沉
        bot.SendTo(contact, get_message(message, int(asciistr)).replace('图灵机器人', '浮沉沉'))
 
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
    elif check(keyList, content) and member.name != '静默':
        # bot.SendTo(contact, '您发送的消息是' + content)
        datatime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))
        print('member =', member.name + '', 'contact =', contact.name)
        strzz = contact.name + ':' + datatime + " " + member.name + "发送消息:" + content # 组装消息
        sendMsgToGroup(strzz, ['测试数据群'], bot)
        print(strzz + " contact.mark" + contact.mark)
 
 
def sendMsgToGroup(msg, groupList, bot):
    # print('向群里发送消息')
    for group in groupList:
        print('group =', group)
        bg = bot.List('group', group)
        if bg:
            b = bg[0]
            bot.SendTo(b, msg)
 
def sendMsgToBuddy(msg, buddyList, bot):
    # print('向好友发送消息')
    for buddy in buddyList:
        print('buddy', type(buddy), buddy)
        bb = bot.List('buddy', buddy)
        if bb:
            b = bb[0]
            bot.SendTo(b, msg)
 
def main(bot):
    groupMsg = '测试消息是发送到群里面的'
    buddyMsg = '测试消息是发送给好友的'
    # print('os.getcwd()', os.getcwd())
    with open('./qq.txt', 'r', encoding='UTF-8') as fr:
        qqGroup = fr.readline().strip()
        qqBuddy = fr.readline().strip()
        print('fr', fr, '\nqqGroup =', qqGroup, '\nqqBuddy', qqBuddy)
    qqGroupList = qqGroup.split(',')
    qqBuddyList = qqBuddy.split(',')
    # sendMsgToGroup(groupMsg, qqGroupList, bot) sendMsgToBuddy(buddyMsg, 
    # qqBuddyList, bot)
 
 
def get_message(message, userid):
    tuling = '2581f443bf364fd8a927fe87832e3d33' # 图灵机器人的id（用户自己创建的）
    api_url = "http://openapi.tuling123.com/openapi/api/v2" # API接口调用
    req = {
        "perception":
            {
                "inputText":
                    {
                        "text": message
                    },
 
                "selfInfo":
                    {
                        "location":
                            {
                                "city": "深圳",
                                "province": "广州",
                                "street": "XXX"
                            }
                    }
            },
        "userInfo":
            {
                "apiKey": tuling,
                "userId": userid
            }
    }
    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request(api_url, data=req, 
headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post) # 得到网页HTML代码
    response_str = response.read().decode('utf8') # 将网页的代码转化为UTF-8 处理 避免乱码
    response_dic = json.loads(response_str) #将得到的json格式的信息转换为Python的字典格式
    results_text = response_dic['results'][0]['values']['text']
    return results_text
 
 
 
if __name__=='__main__':
    bot.Login(['-q', '710469775'])
    # main(bot)
 
    RunBot()
