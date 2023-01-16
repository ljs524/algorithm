N = int(input())
score = map(int, input().split())
sum = 0
result = 0

for i in range(10):
    for _ in score:
        if _ == 1:
            sum += 1
            result += sum
        else:
            sum = 0
print(result)