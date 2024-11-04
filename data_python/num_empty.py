import unittest
from bst import Node
from bst import bst

def num_empty(root):
    if root is None:
        return 1
    elif root.left is None and root.right:
        return 1 + num_empty(root.right)
    elif root.right is None and root.left:
        return 1 + num_empty(root.left)
    else:
        return num_empty(root.left) + num_empty(root.right)


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

    def test_num_empty(self):
        self.assertEqual(10, num_empty(self.tree.root))

if __name__ == '__main__':
    unittest.main()
