t = int(input())
for i in range(t):
    ans = 0
    n, m = map(int, input().split())
    c, d = map(int, input().split())
    if (c - 0) % 2 == 0 and d - 0 == 0:
        ans += c
    elif (c - 0) % 2 != 0 and d - 0 != 0:
            ans += c
    elif (c - 0) % 2 == 0 and d - 0 != 0:
        ans += c - 1
    elif (c - 0) % 2 != 0 and d - 0 == 0:
        ans += c - 1
    
    for j in range(1, n):
        a, b = map(int, input().split())
        if (a - c) % 2 == 0 and b - d == 0:
            ans += a - c
        elif (a - c) % 2 != 0 and b - d != 0:
            ans += a - c
        else:
            ans += a - c - 1
        c, d = a, b
    ans += m - c
    print(ans) 
        
       
   
       


