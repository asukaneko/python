import ollama

host = "localhost"
port = "8000"

def get_ans():
    content = input("请输入:")
    fg=0
    model=model1
    while True:
        client = ollama.Client(host=f"http://{host}:{port}")
        res = client.chat(model=model, messages=[{"role": "user", "content": content}], options={"temperature": 8},
                          stream=False)
        # print(res)
        ans=res.message.content
        print("{}:".format(model))
        print(ans)
        content=ans
        if fg==0:
            model=model2
            fg=1
        else:
            model=model1
            fg=0

if __name__ == '__main__':
    model1 = "qwen2.5:7b"
    model2 = "qwen2.5:3b"
    get_ans()
