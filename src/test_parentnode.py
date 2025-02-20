import unittest

from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("a", None, {"href":"https://www.boot.dev"})
        node2 = node
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = ParentNode("a", None, {"href":"https://www.boot.dev"})
        node2 = ParentNode("a", None, {"href":"https://www.boot.dev"})
        self.assertNotEqual(node,node2)

    def test_tag_not_none(self):
        node = ParentNode("a", None, {"href":"https://www.boot.dev"})
        self.assertIsNotNone(node.tag)

if __name__ == "__main__":
    unittest.main()