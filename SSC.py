def dfs(node, color, adj, t):
    color[node] = 'gray'
    for elements in adj[node]:
        if color[elements] == 'white':
            dfs(elements, color, adj, t)

    color[node] = 'black'
    t.append(node)


def scc(node, visited, transpose):
    visited.add(node)

    for elements in transpose[node]:
        if elements not in visited:
            scc(elements, visited, transpose)

    print(node, end=' ')
def main():
    n = input("Enter Nodes Name: ").split()
    e = int(input("Enter Number of Edges: "))

    adj = {}
    color = {}
    transpose = {}
    t = []
    transpose_DFS = []

    for node in n:
        color[node] = 'white'
        adj[node] = []
        transpose[node] = []

    for i in range(e):
        v, u = input("Edge %d: " % (i + 1)).split()
        adj[v].append(u)
        transpose[u].append(v)

    for elements in n:
        if color[elements] == 'white':
            dfs(elements, color, adj, t)

    while len(t):
        transpose_DFS.append(t.pop())

    visited = set()
    i = 1

    for member in transpose_DFS:
        if member not in visited:
            print()
            print("SCC %d: " % (i), end='')
            i += 1
            scc(member, visited, transpose)


main()
