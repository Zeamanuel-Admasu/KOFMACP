def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    # graph = [[] for _ in range(n)]
    # for i in range(n):
    #     if i + x < n:
    #         graph[i].append(i + x)
    #         graph[i + x].append(i)
    # for i in range(n):
    #     if i + y < n:
    #         graph[i].append(i + y)
    #         graph[i + y].append(i)
    comp = [-1] * (n + 1)
    compid = 0
    for i in range(n):
        if comp[i] != -1:
            continue
        stack = [i]
        comp[i] = compid
        while stack:
            node = stack.pop()
            for nbr in [node + x, node - x, node + y, node - y]:
                if 0 <= nbr < n and comp[nbr] == -1:
                    stack.append(nbr)
                    comp[nbr] = compid
        compid += 1

            

    # def dfs(node, compid):
    #     comp[node] = compid
    #     for nbr in graph[node]:
    #         if comp[nbr] == -1:
    #             dfs(nbr, compid)
    
    # print(graph)
    # for i in range(n):
    #     if comp[i] == -1:
    #         dfs(i, compid)
    #         compid += 1
    for i in range(n):
        curr_pos = i
        corr_pos = a[i] - 1
        if comp[curr_pos] != comp[corr_pos]:
            print("NO")
            return

    print("YES")

a = int(input())
for i in range(a):
    solve()
