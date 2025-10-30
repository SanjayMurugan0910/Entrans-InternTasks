Lis=[1,2,3,4,5,6]
Traget=8
"""
    In the two pointer concept the List is should be in sorted order. And make two pointers one at the start and other at the end of the List.
"""
left=0
right=len(Lis)-1
for i in range(len(Lis)):
    if Lis[left]+Lis[right]>Traget:
        right-=1
    elif Lis[left]+Lis[right]==Traget:
            print(f"Pair found: ({Lis[left]}, {Lis[right]})")
            break
    else:
            left+=1
            


