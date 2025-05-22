import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Node Value", None, {"href":"https://www.boot.dev"})
        # node2 = HTMLNode("a", "Node Value", None, {"href":"https://www.boot.dev"})
        node2 = node
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("a", "Node Value", None, {"href":"https://www.boot.dev"})
        node2 = HTMLNode("a", "Another Node Value", None, {"href":"https://www.boot.dev"})
        self.assertNotEqual(node,node2)

    def test_tag_not_none(self):
        node = HTMLNode("a", "Node Value", None, {"href":"https://www.boot.dev"})
        self.assertIsNotNone(node.tag)


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "Node Value", {"href":"https://www.boot.dev"})
        # node2 = HTMLNode("a", "Node Value", None, {"href":"https://www.boot.dev"})
        node2 = node
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("a", "Node Value", {"href":"https://www.boot.dev"})
        node2 = LeafNode("a", "Another Node Value", {"href":"https://www.boot.dev"})
        self.assertNotEqual(node,node2)

    def test_tag_not_none(self):
        node = LeafNode("a", "Node Value", {"href":"https://www.boot.dev"})
        self.assertIsNotNone(node.tag)


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