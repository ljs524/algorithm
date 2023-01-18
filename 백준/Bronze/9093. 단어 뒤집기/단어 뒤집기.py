T = int(input())
for t in range(T):
    text = list(input().split())
    for _ in text:
        print(_[::-1], end=' ')