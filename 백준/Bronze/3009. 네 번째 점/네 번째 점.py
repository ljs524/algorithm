numA = []
numB = []
a4 = 0
b4 = 0

for i in range(3):
    a, b = map(int, input().split())
    numA.append(a)
    numB.append(b)

for _ in range(3):
    if numA.count(numA[_]) == 1:
        a4 = numA[_]
    elif numB.count(numB[_]) == 1:
        b4 = numB[_]
print(f'{a4} {b4}')