import unittest
from bst import Node
from bst import bst

def depth_sum(root, n):
    if root:
        return recur_depth_sum(root, 1)

def recur_depth_sum(root, n):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.data * n
    else:
        return n * root.data + recur_depth_sum(root.left, n+1) + recur_depth_sum(root.right, n+1)


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.tree = bst()
        self.tree.insert(9)
        self.tree.insert(6)
        self.tree.insert(12)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(10)
        self.tree.insert(15)
        self.tree.insert(7)
        self.tree.insert(18)

    def test_depth_sum(self):
        self.assertEqual(253, depth_sum(self.tree.root, 4))

if __name__ == '__main__':
    unittest.main()
