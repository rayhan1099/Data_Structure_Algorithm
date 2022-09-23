
def topological_sort(adjacent: dict, visited: list, u, stack: list):
    if u not in visited:
        visited.append(u)
        for element in adjacent[u]:
            if element not in visited:
                topological_sort(adjacent, visited, element, stack)
    stack.append(u)


def detect_cycle(adjacent: dict, visited: list, u):
    if u not in visited:
        visited.append(u)
        for element in adjacent[u]:
            if element in visited:
                return True
            return detect_cycle(adjacent, visited, element)


def dfs(adjacent: dict, visited: list, u, stack: list):
    if u not in visited:
        visited.append(u)
        for element in adjacent[u]:
            if element not in visited:
                dfs(adjacent, visited, element, stack)

    # print(u, end=' ')
    stack.append(u)


def dfs_transpose(adjacent: dict, visited: list, u, stack: list):
    if u not in visited:
        visited.append(u)
        for element in adjacent[u]:
            if element not in visited:
                dfs_transpose(adjacent, visited, element, stack)
    # print(u)
    stack.append(u)


def run_dfs():
    inlist = list(input("Enter name of vertices: ").split(''))
    e = int(input("Enter number of edges: "))
    n = len(inlist)

    adj = {}
    print("Enter edge info. One per line: ")
    for i in inlist:
        adj[i] = []

    for i in range(e):
        u, v = input("Enter edge %d: " % (i + 1)).split(' ')
        adj[u].append(v)
        # adj[v].append(u)

    print(adj)

    visitedO = []
    print('DFS: ')
    for vertex in adj:
        if vertex not in visitedO:
            dfs(adj, visitedO, vertex)


def run_topological():
    inlist = list(input("Enter name of vertices: ").split(''))
    e = int(input("Enter number of edges: "))
    n = len(inlist)
    stack = []
    adj = {}
    print("Enter edge info. One per line: ")
    for i in inlist:
        adj[i] = []

    for i in range(e):
        u, v = input("Enter edge %d: " % (i + 1)).split(' ')
        adj[u].append(v)
        # adj[v].append(u)

    print(adj)

    visitedO = []
    print('Topological sort: ')
    for vertex in adj:
        if vertex not in visitedO:
            topological_sort(adj, visitedO, vertex, stack)

    print(stack)


def run_detect_cycle():
    inlist = list(input("Enter name of vertices: ").split(' '))
    e = int(input("Enter number of edges: "))
    n = len(inlist)

    adj = {}
    print("Enter edge info. One per line: ")
    for i in inlist:
        adj[i] = []

    for i in range(e):
        u, v = input("Enter edge %d: " % (i + 1)).split(' ')
        adj[u].append(v)
        # adj[v].append(u)

    print(adj)

    visitedO = []
    cycle = False
    for vertex in adj:
        if vertex not in visitedO:
            cycle = detect_cycle(adj, visitedO, vertex)

    if cycle:
        print("Cycle detected")
    else:
        print("No cycle! Yay!!")


def run_scc():
    inlist = list(input("Enter name of vertices: ").split(' '))
    e = int(input("Enter number of edges: "))
    n = len(inlist)

    adj = {}
    transpose_adj = {}
    mstack = []
    visited = []
    visited_transpose = []

    print("Enter edge info. One per line: ")
    for i in inlist:
        adj[i] = []
        transpose_adj[i] = []

    for i in range(e):
        u, v = input("Enter edge %d: " % (i + 1)).split(' ')
        adj[u].append(v)
        transpose_adj[v].append(u)
        # adj[v].append(u)

    for vertex in adj:
        if vertex not in visited:
            dfs(adj, visited, vertex, mstack)

    scc = 0
    while mstack:
        item = mstack.pop()
        if item not in visited_transpose:
            ts = []
            scc += 1
            print("SCC %d:" % scc, end=' ')
            dfs_transpose(transpose_adj, visited_transpose, item, ts)
            for i in ts:
                print(i, end='')
            print()
        run_scc()
