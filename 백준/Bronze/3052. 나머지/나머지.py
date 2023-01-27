list = []

for i in range(10):
    num = int(input())
    list.append(num % 42)
list = set(list)
print(len(list))