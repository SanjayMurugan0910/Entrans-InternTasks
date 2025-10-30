lis=[7,5,4,6,10,12,1,3,9,8,2]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]>lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
print(lis)