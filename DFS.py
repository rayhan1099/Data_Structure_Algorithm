from typing import DefaultDict
def dfs(adj,visited,u):
    if u not in visited:
        visited.add(u)
        for element in adj[u]:
            if element not in visited:
                dfs(adj, visited,element)
    print(u,end=' ')

n=int(input("How many nodes? "))
e=int(input("How many edges? "))
adj=DefaultDict(list)
print("Enter edges' information.")
for i in range(e):
    u,v=input("Edge %d: "%(i+1)).split()
    adj[u].append(v)
print(adj)
visited=set()
print("DFS: ")
for vertex in adj:
        if vertex not in visited:
            dfs(adj,visited,vertex)
