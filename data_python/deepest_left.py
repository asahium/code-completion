class DeepestLeft:
    def __init__(self):
        self.depth = 0
        self.Node = None


def find_deepest_left(root, is_left, depth, res):
    if not root:
        return
    if is_left and depth > res.depth:
        res.depth = depth
        res.Node = root
    find_deepest_left(root.left, True, depth + 1, res)
    find_deepest_left(root.right, False, depth + 1, res)
