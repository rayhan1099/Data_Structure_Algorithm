def make_set(x):
    parent[x]=x
    rank[x]=0
def find_set(x):
    if parent[x]!=x:
       parent[x]=find_set(parent[x])
def union_set(x,y):
    if rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y
        if range[x]==rank[y]:
            rank[y]+=1
def kruskal(nn,edges):
    selected_edge=list()#[]
    mst_weight=0
    for node in nn:
        make_set(node)
    sorted_edges=sorted(edges,key=lambda x:x[2])
    for edge in sorted_edges:
        u,v,w=edge[0],edge[1],edge[2]
        parent_u=find_set(u)
        parent_v=find_set(v)
        if parent_u!=parent_v:
            selected_edge.append(edge)
            mst_weight+=w
            union_set(parent_u,parent_v)
        return(selected_edge,mst_weight)
nn=input("Enter nodes name: ").split()
e=int(input("Enter how many edges:"))
edges=[]
parent={ }
rank={ }
print("Enter edges(u,v,w):")
for i in range(e):
    u,v,w=input("edge %d: "%(i+1)).split()
    edges.append([u,v,w])
    result=kruskal(nn,edges)
print(result)
