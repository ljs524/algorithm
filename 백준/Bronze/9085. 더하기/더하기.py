T = int(input())

for i in range(T): 
    nums = []
    K = int(input())
    nums = list(map(int, input().split()))
    print(sum(nums))