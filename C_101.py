t = int(input())
for i in range(t):
    a = int(input())
    arr = list(map(int, input().split()))
    first_neg = -1
    last_neg = -1
    first_one = -1
    last_one = -1

    for _ in range(len(arr)):
        if arr[_] == -1:
            if first_neg == -1:
                first_neg = _
            last_neg = _
    # print("bbb", first_neg, last_neg, first_one, last_one)
    for _ in range(len(arr)):
        if arr[_] == 1:
            if first_one == -1:
                first_one = _
            last_one = _

    changefirstneg = False
    if first_neg != -1:
        if first_one == -1 or first_neg < first_one:
            changefirstneg = True
    changelastneg = False
    if last_neg != -1:
        if last_one == -1 or last_neg > last_one:
            changelastneg = True
    # print(arr, "aaa", first_neg, last_neg, first_one, last_one, changefirstneg, changelastneg)
    for j in range(len(arr)):
        if arr[j] == -1:
            arr[j] = 0

    if changefirstneg:
        arr[first_neg] = 1
    if changelastneg:
        arr[last_neg] = 1
    print(*arr)
