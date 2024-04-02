import unittest

from src.htmlnode import LeafNode
from src.textnode import TextNode, text_type_text, text_node_to_html_node, text_type_bold, text_type_italic, \
    text_type_code, text_type_link, text_type_image


class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.node = TextNode('text', 'text_type', 'url')

    def test_eq(self):
        other_node = TextNode('text', 'text_type', 'url')
        self.assertTrue(self.node.__eq__(other_node))

    def test_repr(self):
        self.assertEqual(self.node.__repr__(), "TextNode(text, text_type, url)")


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", text_type_text, None)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, "Hello, world!"))

        text_node = TextNode("Hello, world!", text_type_bold, None)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("b", "Hello, world!"))

        text_node = TextNode("Hello, world!", text_type_italic, None)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("i", "Hello, world!"))

        text_node = TextNode("Hello, world!", text_type_code, None)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode("code", "Hello, world!"))

        text_node = TextNode("Hello, world!", text_type_link, "https://www.google.com")
        self.assertEqual(text_node_to_html_node(text_node),
                         LeafNode("a", "Hello, world!", {"href": "https://www.google.com"}))

        text_node = TextNode("Hello, world!", text_type_image, "https://www.google.com/image.png")
        self.assertEqual(text_node_to_html_node(text_node),
                         LeafNode("img", "", {"src": "https://www.google.com/image.png", "alt": "Hello, world!"}))

    def test_invalid_text_type(self):
        text_node = TextNode("Hello, world!", "invalid_type", None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)


if __name__ == '__main__':
    unittest.main()
