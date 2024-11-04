def is_same_tree(tree_p, tree_q):
    if tree_p is None and tree_q is None:
        return True
    if tree_p is not None and tree_q is not None and tree_p.val == tree_q.val:
        return is_same_tree(tree_p.left, tree_q.left) and is_same_tree(tree_p.right, tree_q.right)
    return False