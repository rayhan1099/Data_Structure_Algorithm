from math import inf
from queue import PriorityQueue


class Node:
    def __init__(self, node):
        self.name = node
        self.d = inf
        self.parent = None
        self.is_visited = False
        self.adj = []

    def __lt__(self, other):
        return self.d < other.d


def dijkstra(s, nodes):
    q = PriorityQueue()
    nodes[s].d = 0
    nodes[s].parent = s
    q.put(nodes[s])

    while not q.empty():
        u = q.get()
        u.is_visited = True

        for element in u.adj:
            v, w = element[0], element[1]
            if nodes[v].is_visited is False and nodes[v].d > (u.d+w):
                nodes[v].d = u.d+w
                nodes[v].parent = u.name
                q.put(nodes[v])


def path_print(x,nodes):
    if nodes[x].parent is x:
        print(x, end=' ')
    if nodes[x].parent is not x:
        path_print(nodes[x].parent, nodes)
        print(x, end=' ')


def main():
    n = int(input("How many nodes? "))
    node_name = input("Enter nodes' name: ").split()
    nodes = {}
    for element in node_name:
        nodes[element] = Node(element)
    e = int(input("How many edges? "))
    for i in range(e):
        u, v, w = input("Edge %d: " % (i+1)).split()
        nodes[u].adj.append([v, int(w)])
    s = input("Source = ")
    dijkstra(s, nodes)
    for element in node_name:
        print("vertex name: %s" % element)
        print("cost %d " % nodes[element].d)
        print("path: ", end=' ')
        path_print(element, nodes)
        print()


if __name__ == "__main__":
    main()