from openai import OpenAI

client = OpenAI(api_key="sk-464b5baf13384c3fb0ccf951f14142af", base_url="https://api.deepseek.com")

#id = int(input("请选择模型：\n 1为deepseek-v3\n 2为deepseek-r1\n"))

id = 2

model = ""

if id == 1:
    model = "deepseek-chat"
if id == 2:
    model = "deepseek-reasoner"

# 初始化消息列表，用于保存历史对话
messages = []

while True:
    content = input("请输入：")
    if content == "q":
        break
    # 将用户输入添加到消息列表
    messages.append({"role": "user", "content": content})
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False
    )
    # 获取助手的回复
    assistant_response = response.choices[0].message.content
    # 将助手的回复添加到消息列表
    messages.append({"role": "assistant", "content": assistant_response})
    print(assistant_response)
