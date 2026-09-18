t = int(input())
for i in range(t):
    n, c  = map(int, input().split())
    arr = list(map(int, input().split()))
    dictt = {}
    for j in arr:
        if j in dictt:
            dictt[j] += 1
        else:
            dictt[j] = 1
    ans = 0
    # print(dictt, c, )
    for k in arr:
        if dictt[k] > c:
            ans += c
            dictt[k] = 0
        elif dictt[k] <= c:
            ans += dictt[k]
            dictt[k] = 0
        # print(ans, "aaa")
    print(ans)