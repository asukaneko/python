#以<>为查找点进行重命名
import os

def rename():
    for filename in os.listdir('.'):
        if not filename.endswith('.txt'):
            continue
        name = filename.replace('.txt', '')
        with open(filename, 'r', encoding='gbk') as f:
            content = f.read()
            content = str(content)
            a = content.find("<")
            b = content.find(">")
            title = content[a+1:b]
            #print(title)
            new_name = f'{title}.txt'
            try:
                os.rename(filename, new_name)
                print(f'{filename} ---> {new_name}')
            except FileExistsError:
                print(f'文件 {new_name} 已存在，跳过')
            except PermissionError:
                print(f'文件 {filename} 被占用，无法重命名')
            except Exception as e:
                print(f'处理 {filename} 时发生意外错误：{str(e)}')


if __name__ == '__main__':
    rename()
