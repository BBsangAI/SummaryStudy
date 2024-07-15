import re
from collections import defaultdict

def wordcount(text):
    # 将字符串转换为小写，并使用正则表达式提取所有单词
    words = re.findall(r'\b\w+\b', text.lower())
    
    # 使用defaultdict来存储单词及其出现的次数
    word_counts = defaultdict(int)
    
    # 遍历单词列表，统计每个单词出现的次数
    for word in words:
        word_counts[word] += 1
    
    return dict(word_counts)

def main():
    text =  """Got this panda plush toy for my daughter's birthday, who loves it and takes it everywhere. It's soft and super cute, and its face has a friendly look.
               It's  a bit small for what I paid though. I think there"
               might be other options that are bigger for the"
               same price. It arrived a day earlier than expected, 
               so I got to play with it myself before I gave it 
               to her."""
    print(wordcount(text))
if __name__== "__main__":
    main()
