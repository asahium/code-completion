import unittest
from bst import Node
from bst import bst

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


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

    def test_height(self):
        self.assertEqual(4, height(self.tree.root))

