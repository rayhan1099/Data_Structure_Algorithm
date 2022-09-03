
def dfs(u):
    color[u] = 'gray'
    for element in adj[u]:
        if color[element]=='gray':
            print("the given graph is not a DAG")
            exit()
        elif color[element] == 'white':
            dfs(element)

    color[u] = 'black'
    T.append(u)


n = input("Enter Nodes Name:").split()
e = int(input("Number of Edges: "))

adj = {}
color = {}
for element in n:
    adj[element] = []
    color[element] = 'white'
for i in range(e):
    u, v = input("Edge %d: " %(i+1)).split()
    adj[u].append(v)
T = []
print("Topological Sort: ")
for member in n:
    if color[member] == 'white':
        dfs(member)
while len(T) != 0:
    print(T.pop(), end=' ')
print()
print()
print(adj)
print(color)