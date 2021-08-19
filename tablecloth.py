n = int(input())
width, height = map(int, input().split())
cost = 1001 # max cost + 1

width, height = min(width, height), max(width, height)

for _ in range(n):
    w, h, c = map(int, input().split())
    w, h = min(w, h), max(w, h)

    if w >= width and h >= height:
        cost = min(cost, c)

print(cost)
