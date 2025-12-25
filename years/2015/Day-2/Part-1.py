with open("data-1.txt", encoding="utf-8") as f:
    data = f.read()

total = 0

for i in data.splitlines():
    a = int(i.split('x')[0])
    b = int(i.split('x')[1])
    c = int(i.split('x')[2])
    number = (2*a*b) + (2*b*c) + (2*c*a)
    number += min(a*b,b*c,c*a)

    total += number

print(total)