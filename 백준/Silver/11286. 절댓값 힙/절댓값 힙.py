
# abs = 절댓값

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))