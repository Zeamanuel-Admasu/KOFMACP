from math import ceil


t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    arr = input()
    pref = [0] * n
    for i in range(1, n):
        pref[i] = pref[i - 1] + (arr[i] == arr[i - 1])
    for j in range(q):
        l, r, k = map(int, input().split())
        l = l - 1
        r = r - 1
        bad = pref[r] - pref[l]
        operations = ceil(bad / 2)
        print("YES" if operations <= k else "NO")