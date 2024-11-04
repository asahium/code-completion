def longest_consecutive(root):
    if root is None:
        return 0
    max_len = 0
    dfs(root, 0, root.val, max_len)
    return max_len


def dfs(root, cur, target, max_len):
    if root is None:
        return
    if root.val == target:
        cur += 1
    else:
        cur = 1
    max_len = max(cur, max_len)
    dfs(root.left, cur, root.val+1, max_len)
    dfs(root.right, cur, root.val+1, max_len)
