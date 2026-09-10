t = int(input())
for i in range(t):
    emp, job, k = map(int, input().split())
    ans = 0
    
    if emp > job:
        ans = ((emp + (emp + k - 1)) * k) / 2
        print(ans)
    elif emp < job and job < (emp * 2):
        ans = (job % emp) * k
        print(ans)
    elif emp < job and job >= (emp * 2):
        while k > 0 and job > (emp * 2):
            ans += (job % emp)
            k -= 1
            emp += 1
            job += 1
        if k > 0:
            ans += (k - 1) * ((job + 1) % (emp + 1))
            print(ans)
        else:
            print(ans)
    else:
        print(0)

