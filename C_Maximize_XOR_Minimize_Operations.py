t = int(input())
for i in range(t):
    a, b = map(int, input().split())

    s = a + b
    curr = 0
    for j in range(30, -1, -1):
        if s & (1 << j):
            if curr | (1 << j) <= a:
                curr |= (1 << j)
    print(s, a - curr)
    

