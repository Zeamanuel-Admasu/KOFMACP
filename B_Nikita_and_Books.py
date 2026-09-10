t = int(input())
for i in range(t):
    a = int(input())
    pre_B = [0] * (a + 1)
    pre_A = [0] * (a + 1)
    arr = list(map(int, input().split()))
    for j in range(a):
        pre_B[j] = pre_B[j - 1] + (j + 1)
    for j in range(a):
        pre_A[j] = pre_A[j - 1] + (arr[j])
    # print(pre_A, pre_B)
    flag = True
    for j in range(a):
        if pre_A[j] < pre_B[j]:
            flag = False
            print("NO")
            break
        else:
            continue
    if flag:
            print("YES")