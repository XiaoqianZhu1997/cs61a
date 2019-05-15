from urllib.request import urlopen  #可以从网络导入
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
words = set(shakespeare.read().decode().split())   #read读取URL的数据，decode将数据转换成文字，split将文字转化成一个一个的单词
{w for w in words if len(w) == 6 and w[::-1] in words}  #w[::-1] 表示倒过来拼写
