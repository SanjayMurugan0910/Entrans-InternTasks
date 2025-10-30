lis=[7,5,4,6,10,12,1,3,9,8,2]
li1=[]
for i in range(len(lis)):
    m=min(lis)
    li1.append(m)
    lis.remove(m)
print(li1)
