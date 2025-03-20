import epub

try:
    book = epub.open_epub("1.epub")
    if book is None:
        raise FileNotFoundError("无法打开 EPUB 文件。")
except FileNotFoundError as e:
    print(f"错误: {e}")
except Exception as e:
    print(f"发生了一个意外错误: {e}")

# 获取书籍标题
title = book.get_metadata('DC', 'title')[0][0]

# 获取书籍作者
authors = book.get_metadata('DC', 'creator')
author = authors[0][0] if authors else None

# 获取书籍语言
language = book.get_metadata('DC', 'language')[0][0]
print(title, author, language)
