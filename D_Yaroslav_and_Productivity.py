a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    b = set(map(int, input().split()))
    

    ans = 0
    dp0 = 0
    dp1 = float('-inf')

    for i in range(n - 1, -1, -1):
        if i + 1 in b:
            best = max(dp0, dp1)
            ndp0 = best + arr[i]
            ndp1 = best - arr[i]
        else:
            ndp0 = dp0 + arr[i]
            ndp1 = dp1 - arr[i]
        dp0, dp1 = ndp0, ndp1
    print(max(dp0, dp1))

