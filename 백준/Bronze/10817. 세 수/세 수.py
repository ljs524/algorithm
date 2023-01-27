from heapq import heapify, nsmallest

heap = list(map(int, input().split()))
heapify(heap)
print(nsmallest(3, heap)[1])