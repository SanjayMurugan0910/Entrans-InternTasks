l1=[1,5,3,4,6,7]
target=4
l=0
r=len(l1)-1
while l<=r:
    m=(l+r)//2
    if l1[m]==target:
       print(m)
       break
    elif target>l1[m]:
        l=m+1
    elif target<l1[m]:
        r=m-1
else:
    print("Target not found")