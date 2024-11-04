import collections


def is_subtree(big, small):
    flag = False
    queue = collections.deque()
    queue.append(big)
    while queue:
        node = queue.popleft()
        if node.val == small.val:
            flag = comp(node, small)
            break
        else:
            queue.append(node.left)
            queue.append(node.right)
    return flag


def comp(p, q):
    if p is None and q is None:
        return True
    if p is not None and q is not None:
        return p.val == q.val and comp(p.left,q.left) and comp(p.right, q.right)
    return False
