import ollama

host = "localhost"
port = "8000"
client = ollama.Client(host=f"http://{host}:{port}")
#model = "deepseek-r1:14b"
model = "qwen2.5:14b"
"""
content1  = "下面给你一些文本，请将其翻译成日文。"

res = client.chat(model=model,
                  messages=[{"role": "system", "content": "You are a helpful translater"},
                            {"role": "user", "content": content1}],
                  options={"temperature": 8},
                  stream=False)

print(res.message.content)
"""
with open("1.txt", "r", encoding="utf-8",errors='ignore') as f:
    with open("2.txt", "w", encoding="utf-8") as f1:
        for line in f:
            #print(line.strip())
            #print("----------------")
            content = line.strip()
            if content == "":
                continue
            content = "下面给你一些文本，请将其翻译成日文。注意回答只保留翻译后的日文,并且就算有任何注释和提示都不要输出\n"+content
            res = client.chat(model=model,
                              messages=[
                                        {"role": "user", "content": content}],
                              options={"temperature": 8},
                              stream=False)

            print(res.message.content)
            f1.write(res.message.content+'\n\n')