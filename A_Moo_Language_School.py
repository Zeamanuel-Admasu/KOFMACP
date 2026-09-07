t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input()))
    count = 0
    for j in range(0, n, m):
        if sum(arr[j:j+m]) == m:
            count += 1
    print(count)


        
