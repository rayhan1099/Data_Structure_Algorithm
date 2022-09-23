from typing import DefaultDict
from queue import Queue


n=int(input("How many nodes? "))
e=int(input("How many edges? "))
adj=DefaultDict(list)
print("Enter edges' information.")
for i in range(e):
    u,v=input("Edge %d: "%(i+1)).split()
    adj[u].append(v)
    adj[v].append(u)
visited=set()
q=Queue(maxsize=n)
s=input("Enter Source node: ")
q.put(s)
print("BFS")
while not q.empty():
    u=q.get()
    print(u,end=' ')
for element in adj[u]:
    if element not in visited:
        q.put(element)
        visited.add(element)
