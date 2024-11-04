def is_balanced(root):
    return __is_balanced_recursive(root)


def __is_balanced_recursive(root):
    return -1 != __get_depth(root)


def __get_depth(root):
    if root is None:
        return 0
    left = __get_depth(root.left)
    right = __get_depth(root.right)
    if abs(left-right) > 1 or -1 in [left, right]:
        return -1
    return 1 + max(left, right)