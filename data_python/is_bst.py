def is_bst(root):
    stack = []
    pre = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if pre and root.val <= pre.val:
            return False
        pre = root
        root = root.right

    return True
