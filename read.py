data = [] #讀取以後裝進清單
count = 0
with open('reviews.txt', 'r') as f: #用讀取模式打開文字檔review，並當作f
	for line in f: #一次讀取的時候讀一行，每一行取名叫做line
	    data.append(line)  #把line裝進去data清單裡面
	    count += 1 #count = count + 1
	    if count % 10000 == 0:
	    	print(len(data))
print(len(data))
print(data[0])