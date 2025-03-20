#更改文件名与书名的错版
import os
import re
import time

def rename_txt_files(max_retries=3, retry_delay=1):
    for filename in os.listdir('.'):
        if not filename.endswith('.txt'):
            continue

        for attempt in range(max_retries):
            try:
                # 读取文件内容
                with open(filename, 'r', encoding='utf-8',errors='ignore') as f:
                    content = f.read()

                # 提取书名
                a = 170
                content = str(content)
                b=content.find("gt")-1
                name = content[a:b]
                print(name)

                # 生成基础文件名
                new_name = f"{name}.txt"

                # 如果新文件名与当前文件名相同则跳过
                if new_name == filename:
                    print(f'保持：{filename} 无需修改')
                    break

                # 处理文件名冲突（自动追加句号）
                while os.path.exists(new_name):
                    name += '。'
                    new_name = f"{name}.txt"

                # 重命名文件
                os.rename(filename, new_name)
                print(f'重命名成功：{filename} → {new_name}')
                break

            except PermissionError:
                if attempt < max_retries - 1:
                    print(f'文件 {filename} 被占用，第{attempt+1}次重试...')
                    time.sleep(retry_delay)
                else:
                    print(f'错误：{filename} 仍被占用，请检查资源管理器或文本编辑器')
            except Exception as e:
                print(f'处理 {filename} 时发生意外错误：{str(e)}')
                break

if __name__ == '__main__':
    rename_txt_files()

