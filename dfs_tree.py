
# Assessment 3.6: DFS Method in Tree
# Name: JOSHUA COSINO
# Section: BSIT 1C

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the binary tree using JOSHUA COSINO
root = Node("J")

root.left = Node("O")
root.left.left = Node("H")
root.left.left.left = Node("O")
root.left.left.right = Node("S")

root.left.right = Node("U")
root.left.right.left = Node("I")
root.left.right.right = Node("N")

root.right = Node("S")
root.right.left = Node("A")
root.right.left.left = Node("O")
root.right.right = Node("C")


# DFS Preorder: Root -> Left -> Right
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# DFS Inorder: Left -> Root -> Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# DFS Postorder: Left -> Right -> Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Display program information
print("Assessment 3.6: DFS Method in Tree")
print("Name: JOSHUA COSINO")
print("Section: BSIT 1C")

print("\nDFS Preorder Traversal:")
preorder(root)

print("\n\nDFS Inorder Traversal:")
inorder(root)

print("\n\nDFS Postorder Traversal:")
postorder(root)

print()
