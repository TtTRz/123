import re
def go_split(s,symbol):
	symbol = "[" + symbol + "]+"
	#拼正则表达式
	result = re.split(symbol,s)
	#一次性分割字符串
	return [ x for x in result if x ]
	#去除空字符
sentence = input()
sentence = sentence.lower() #字母小写
symbol = '.,;:?! '
sentence = go_split(sentence,symbol)
sentence1 = list(set(sentence))

dir1={}
for i in range (len(sentence1)) :
	dir1[sentence1[i]]=0
	for j in range (len(sentence)) :
		if(sentence1[i]==sentence[j]):
			dir1[sentence1[i]]+=1
for key in dir1.keys():
	print("{0}:{1}".format(key,dir1[key]))


