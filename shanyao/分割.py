
f = open('E:/python笔记/text/shanyao/1.json','r')
data = open('1.txt','w')
for i in range(300):
    a = f.readline().split('"')
    print(a[3],a[-2])
    data.write(a[3] + '\t' + a[-2] + '\n')
data.close()
