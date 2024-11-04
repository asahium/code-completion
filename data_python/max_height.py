from tree import TreeNode


def max_height(root):
    if root is None:
        return 0
    height = 0
    queue = [root]
    while queue:
        height += 1
        level = []
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                level.append(node.left)
            if node.right is not None:
                level.append(node.right)
        queue = level
    return height


def print_tree(root):
    if root is not None:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)
