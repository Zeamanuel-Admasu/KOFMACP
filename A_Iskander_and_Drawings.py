import math
t = int(input())
for i in range(t):
    a = int(input())
    arr = input()
    maxim = 0
    count = 0
    for j in range(a):
        if arr[j] == "#":
            count += 1
            maxim = max(maxim, count)
        else:
            count = 0
    print(math.ceil(maxim / 2))