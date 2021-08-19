n = input()[::-1]

last = -1
if n[0] != '*':
    last = int(n[0])

penultimate = -1
if n[1] != '*':
    penultimate = int(n[1])

third_to_last = -1
if len(n) == 2:
    third_to_last = 0
elif n[2] != '*':
    third_to_last = int(n[2])

ans = [1]

# 2
if last != -1 and last % 2 == 0:
    ans.append(2)

# 3 - need sum of digits

# 4
if last != -1 and penultimate != -1:
    s = penultimate * 10 + last

    if s % 4 == 0:
        ans.append(4)

# 5
if last != -1 and last in [0, 5]:
    ans.append(5)

# 6 - need sum of digits

# 7 - need all digits

# 8
if last != -1 and penultimate != -1 and third_to_last != -1:
    s = third_to_last * 100 + penultimate * 10 + last
    if s % 8 == 0:
        ans.append(8)

# 9 - need sum of digits

print(*ans, sep=' ')
