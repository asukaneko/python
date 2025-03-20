from openai import OpenAI

client = OpenAI(api_key="sk-464b5baf13384c3fb0ccf951f14142af", base_url="https://api.deepseek.com")

model = "deepseek-chat"


with open("1.txt", "r", encoding="utf-8",errors='ignore') as f:
    with open("2.txt", "w", encoding="utf-8") as f1:
        for line in f:
            #print(line.strip())
            #print("----------------")
            content = line.strip()
            if content == "":
                continue
            content = "下面给你一些文本，请将其翻译成中文。注意回答只保留翻译后的中文,并且就算有任何注释和提示都不要输出\n"+content
            response = client.chat.completions.create(
                    model=model,
                    messages=[
                    {"role": "system", "content": "You are a helpful translater"},
                    {"role": "user", "content": content},
                    ],
                    stream=False
            )
            print(response.choices[0].message.content)
            f1.write(response.choices[0].message.content+'\n\n')