import matplotlib.pyplot as plt
from graphviz import Digraph
# Define the TreeNode class and the BFS and DFS functions

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

@time_it
def BFS_contains(root, target):
    queue = [root]  # Create a queue for BFS
    while queue:
        node = queue.pop(0) #dequeue the vertex from queue
        if node:
            if node.val == target:
                return True
            # Add the child nodes to the queue
            queue.append(node.left)
            queue.append(node.right)
    return False

@time_it
def DFS_contains(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return DFS_contains(root.left, target) or DFS_contains(root.right, target)

def print_tree(node):
    dot = Digraph()

    def add_node(node):
        if node:
            dot.node(str(node.val))
            if node.left:
                dot.edge(str(node.val), str(node.left.val))
                add_node(node.left)
            if node.right:
                dot.edge(str(node.val), str(node.right.val))
                add_node(node.right)

    add_node(node)
    dot.render('binary_trees.gv', view=True)

root = list_to_bt([i for i in range(30)])
print_tree(root)# Plot the time taken by both BFS and DFS algorithms to search for each node in the tree
fig, ax = plt.subplots(figsize=(20, 6))

bfs_times = []
dfs_times = []

for i in range(31):
    bfs_times.append(BFS_contains(root, i)[0])
    dfs_times.append(DFS_contains(root, i)[0])

ax.bar(range(31), bfs_times, label="BFS")
ax.bar(range(31), dfs_times, bottom=bfs_times, label="DFS")
ax.set_title("BFS vs DFS")
ax.legend()
plt.xticks(range(31))
plt.show()