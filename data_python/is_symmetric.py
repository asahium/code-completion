def is_symmetric(root):
    if root is None:
        return True
    return helper(root.left, root.right)


def helper(p, q):
    if p is None and q is None:
        return True
    if p is not None or q is not None or q.val != p.val:
        return False
    return helper(p.left, q.right) and helper(p.right, q.left)


def is_symmetric_iterative(root):
    if root is None:
        return True
    stack = [[root.left, root.right]]
    while stack:
        left, right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
        else:
            return False
    return True
