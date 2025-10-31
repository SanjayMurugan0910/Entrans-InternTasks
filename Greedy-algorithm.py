coins=[2,4,7]
coins.sort(reverse=True)
change=6
count=0
for coin in coins:
    count+=change//coin
    change=change%coin
if change==0:
        print(count)
else:
    print("Not possible to give exact change")