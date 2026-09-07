t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split())) 
    counto = 0
    counte = 0
    e = 0
    a = 0
    e1 = 0
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            counte += 1
            if (arr[j] / 2) % 2 == 0:
                e += 1
            else:
                e1 += 1
        else:
            counto += 1
    # print(counto, counte, e)
    a = 0
    if counto > e and counto > e1:
        a = counto     
    else:
        if e > e1:
            a = e
        else:
            a = e1
        
    print(a)
    