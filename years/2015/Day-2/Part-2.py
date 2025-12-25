import re

with open("data-1.txt", encoding="utf-8") as f:
    data = f.readlines()

# total = []

# for i in data.splitlines():
#     number = 0
#     a = int(i.split('x')[0])
#     b = int(i.split('x')[1])
#     c = int(i.split('x')[2])
#     number = (a+a+b+b)
#     number += math.prod([a,b,c])

#     total.append(number)

# print(sum(total))



sizes = [[int(x) for x in re.findall(r'\d+', s)] for s in data]

print(sum(2*(sum(s) - max(s)) + s[0]*s[1]*s[2] for s in sizes))