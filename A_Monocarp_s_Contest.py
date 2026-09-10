t = int(input())
for i in range(t):
    a = int(input())
    arr = list(map(int, input().split()))
    count = 0

    for j in range(len(arr)):
        if arr[j] == 0:
            count += 1
    if count >= 2:
        if arr[0] == 0 and arr[-1] == 0:
            print("0")
        elif arr[0] != 0 and arr[-1] != 0:
            print("2")
        elif arr[0] == 0 and arr[-1] != 0:
            print("1")
        elif arr[0] != 0 and arr[-1] == 0:
            print("1")
    else:
        print("-1")