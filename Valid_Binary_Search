class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if not node:
        return True
    
    if not (min_value < node.value < max_value):
        return False
    
    return (is_valid_bst(node.left, min_value, node.value) and
            is_valid_bst(node.right, node.value, max_value))
