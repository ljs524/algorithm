a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lists = [a, b, c, d, e]
sum = 0

for n in lists:
    if n >= 40:
        sum += n
    else:
        sum += 40
print(int(sum//5))