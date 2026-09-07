a = int(input())
for i in range(a):
    b = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for j in range(len(arr)):
        if arr[j] == 0:
            cnt += 1
    if cnt == 0:
        print("YES")
        ans = []
        for k in range(len(arr)):
            ans.append("C")
        print("".join(map(str, ans)))
    elif cnt >= 2:
        print("YES")
        ans = []
        flag = True
        for k in range(len(arr)):
            if flag and arr[k] == 0:
                flag = False
                ans.append("A")
            elif not flag and arr[k] == 0:
                ans.append("B")
            else:
                ans.append("C")
        print("".join(map(str, ans)))
        
    else:
        print("NO")

    