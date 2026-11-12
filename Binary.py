from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = TreeNode(root_val)

    def bfs(self):
        result = []
        if not self.root:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs_preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.val)
            self.dfs_preorder(node.left, result)
            self.dfs_preorder(node.right, result)
        return result

if __name__ == "__main__":
    print("--- BINARY TREE (COSINO) ---")
    # Tree Structure for COSINO: Root 'C', Left 'O', Right 'S', Left-Left 'I', Left-Right 'N'
    tree = BinaryTree('C')
    tree.root.left = TreeNode('O')
    tree.root.right = TreeNode('S')
    tree.root.left.left = TreeNode('I')
    tree.root.left.right = TreeNode('N')

    print("BFS Traversal:", " -> ".join(tree.bfs()))
    print("DFS Traversal:", " -> ".join(tree.dfs_preorder(tree.root)))