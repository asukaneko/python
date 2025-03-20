import ollama

host = "localhost"
port = "8000"
client = ollama.Client(host=f"http://{host}:{port}")

def get_model():
    n = int(input("按1选择qwen2.5:3b\n按2选择qwen2.5:7b\n按3选择qwen2.5:14b\n:"))
    if n == 1:
        model = "qwen2.5:3b"
    elif n == 2:
        model = "qwen2.5:7b"
    else:
        model = "qwen2.5:14b"
    return model

def get_ans():
    print("按q退出")
    while True:
        content = input("请输入:")
        if content == "q":
            break
        res = client.chat(model=model, messages=[{"role": "user", "content": content}], options={"temperature": 8},
                          stream=False)
        # print(res)
        print(res.message.content)

if __name__ == "__main__":
    model = get_model()
    get_ans()
