number = list(map(int, input().split()))
num_list = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(num_list[i] - number[i], end = ' ')