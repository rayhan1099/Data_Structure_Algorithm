import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    

def minimaxTree(isMax, tree):
    # print(tree)
    if tree.right == None and tree.left == None:
        return tree.value
    
    if isMax:
        v = max(
            minimaxTree(False, tree.left) if tree.left is not None else float('-inf'),
            minimaxTree(False, tree.right) if tree.right is not None  else float('-inf')
        )
        # print(f'max {v}')
        return v
    else:
        v = min(
            minimaxTree(True,tree.left) if tree.left is not None else float('inf'),
            minimaxTree(True, tree.right) if tree.right is not None else float('inf')
        )
        # print(f'min {v}')
        return v



def minimax(cur_depth, nodeIndex, isMax, nodes, maxDepth):
    if cur_depth == maxDepth:
        return nodes[nodeIndex]
    if isMax:
        v = max(
            minimax(cur_depth+1, nodeIndex*2, False, nodes, maxDepth),
            minimax(cur_depth+1, nodeIndex*2+1, False, nodes, maxDepth)
        )
        # print(f'max {v}')
        return v
    else:
        v = min(
            minimax(cur_depth+1, nodeIndex*2, True, nodes, maxDepth),
            minimax(cur_depth+1, nodeIndex*2+1, True, nodes, maxDepth)
        )
        return v

tree = [3,5,2,9,12,5,23,23]
tree = [-8,7,15,14,8,-5,1,0]
treeDepth = math.log(len(tree), 2)

#print('the optimal value is: {}'.format(minimax(0,0,True,tree,treeDepth)))

t_1 = Node(3)
t_2 = Node(5)
t_3 = Node(2)
t_4 = Node(9)
t_5 = Node(12)
t_6 = Node(5)
t_7 = Node(23)
t_8 = Node(23)

root = Node(float('inf'))

l_1_1 = Node(float('inf'))
l_1_2 = Node(float('inf'))

l_2_1 = Node(float('-inf'))
l_2_2 = Node(float('-inf'))
l_2_3 = Node(float('-inf'))
l_2_4 = Node(float('-inf'))

l_1_1.left = l_2_1
l_1_1.right = l_2_2
l_1_2.left = l_2_3
l_1_2.right = l_2_4


l_2_1.left = t_1
l_2_1.right = t_2
l_2_2.left = t_3
l_2_2.right = t_4
l_2_3.left = t_5
l_2_3.right = t_6
l_2_4.left = t_7
l_2_4.right = t_8

root.left = l_1_1
root.right = l_1_2

print('the optimal value is: {}'.format(minimaxTree(True, root)))
