from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords

l = input("说点什么吧:")
token = TreebankWordTokenizer().tokenize(l)
stop_words = set(stopwords.word('english'))
output = []
output = [k for k in token if k.isalpha()]
for k in stop_words:
    if k not in stop_words:
        output.append(k)
print(output)


