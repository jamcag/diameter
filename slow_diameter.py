def max_depth(root):
    if not root:
        return 0
    depth = 0
    stack = []
    stack.append((root, 0))
    while stack:
        (node, current_depth) = stack.pop()
        depth = max(depth, current_depth)
        if node.left:
            stack.append((node.left, current_depth + 1))
        if node.right:
            stack.append((node.right, current_depth + 1))
    return depth + 1

def diameter(self):
    if not root:
        return 0
    return max(
        diameter(root.left),
        diameter(root.right),
        max_depth(root.left) + max_depth(root.right))
