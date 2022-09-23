from typing import DefaultDict

def dfs(adj,visited,u):
    if u not in visited:
        visited.add(u)
        for element in adj[u]:
            if element not in visited:
                dfs(adj, visited,element)
    T.append(u)

n=int(input("How many nodes? "))
e=int(input("How many edges? "))
adj=DefaultDict(list)
print("Enter edges' information.")
for i in range(e):
    u,v=input("Edge %d: "%(i+1)).split()
    adj[u].append(v)
print(adj)
visited=set()
T=[]
print("topologicalSort")
for vertex in list(adj):
        if vertex not in visited:
            dfs(adj,visited,vertex)
while len(T)!=0:
    print(T.pop(),end=' ')
     
    