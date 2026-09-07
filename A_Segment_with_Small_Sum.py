n, m = map(int, input().split())
arr = list(map(int, input().split()))
j = 0
count = 0
maxim = 0
i = 0
summ = 0
while i < len(arr):
    summ += arr[i]
    count += 1
    while summ > m:
        summ -= arr[j]
        j += 1
        count -= 1
    maxim = max(maxim, count)
    i += 1
print(maxim)
        

