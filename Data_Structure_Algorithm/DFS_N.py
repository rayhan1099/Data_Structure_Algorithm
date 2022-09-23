def dfs(u,color,adj):
    color[u]='gray'
    for element in adj[u]:
        if color[element]=='white':
            dfs(element,color,adj)
    color[u]='black'
    print(u,end=' ')


def main():
    n=input("Enter Nodes Name:").split()
    e=int(input("Number of Edges: "))
    adj={}
    color={}
    for element in n:
        adj[element]=[]
        color[element]='white'
    for i in range(e):
        u,v=input("Edge %d: "%(i+1)).split()
        adj[u].append(v)
        #adj[v].append(v)

    print("DFS: ")
    for member in n:
        if color[member]=='white':
            dfs(member,color,adj)
          
main()


