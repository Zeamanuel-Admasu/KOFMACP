a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    ans = 0
    left = 0

    for right in b:
        segment_sum = sum(arr[left:right])
        ans += abs(segment_sum)
        left = right

    ans += sum(arr[left:])
    print(ans)