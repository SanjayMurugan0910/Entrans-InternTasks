lis=[7,5,4,6,10,12,1,3,9,8,2]
while True:
    swapped=False
    for i in range(len(lis)-1):
        if lis[i]>lis[i+1]:
            lis[i],lis[i+1]=lis[i+1],lis[i]
            swapped=True
    if not swapped:
        break