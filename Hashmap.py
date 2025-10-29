from collections import defaultdict
str=["eat","tea","tan","ate","nat","bat"]
anagarams=defaultdict(list)
result=[]
for i in str:
    sorted_str=''.join(sorted(i))
    anagarams[sorted_str].append(i)
for group in anagarams.values():
    result.append(group)
print(result)