import heapq

n = int(input())
h = list(map(int, input().split()))

heapq.heapify(h)

s = 0

while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)

    s += a + b

    heapq.heappush(h, a + b)

print(s / 20)
