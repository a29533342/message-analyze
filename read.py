data = [] #讀取以後裝進清單
count = 0
with open('reviews.txt', 'r') as f: #用讀取模式打開文字檔review，並當作f
	for line in f: #一次讀取的時候讀一行，每一行取名叫做line
	    data.append(line)  #把line裝進去data清單裡面
	    count += 1 #count = count + 1
	    if count % 100000 == 0:
	    	print(len(data))
sum_len = 0
for d in data: #讀取data，一次一行，每一行取名叫d
	# len(d) d的長度，即為該字串長度
	sum_len = sum_len + len(d) #也可簡寫成 sum_len(d) =+ 1
print('平均留言長度是:', sum_len / len(data))
print(len(data))
print(len(data[0]))
print(len(data[1]))
print('檔案讀取完了，總共有', len(data), '筆資料')

