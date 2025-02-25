import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_urlNotNone(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertIsNotNone(node.url)
    
    def test_text_type_not_same(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node.text_type, node2.text_type)
    
    def test_url_same(self):
        node = TextNode("This is the first text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is the second text node", TextType.BOLD, "https://www.google.com")
        self.assertEqual(node.url, node2.url)
    

if __name__ == "__main__":
    unittest.main()