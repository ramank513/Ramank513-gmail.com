class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_largest(root):
    current = root
    while current.right:
        current = current.right
    return current

def find_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        raise ValueError("Tree must have at least two nodes")

    current = root
    while current:
        if current.left and current.right is None:
            return find_largest(current.left).val

        if current.right and current.right.left is None and current.right.right is None:
            return current.val

        current = current.right

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(40)

print(find_second_largest(root)) 