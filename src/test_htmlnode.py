import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node = HTMLNode('tag', 'value', 'children', {'prop1': 'value1', 'prop2': 'value2'})

    def test_props_to_html(self):
        self.assertEqual(self.node.props_to_html(), ' prop1="value1" prop2="value2"')

    def test_repr(self):
        self.assertEqual(self.node.__repr__(), "HTMLNode(tag, value, children, {'prop1': 'value1', 'prop2': 'value2'})")


class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.tag, "p")
        self.assertEqual(node1.value, "This is a paragraph of text.")
        self.assertIsNone(node1.props, None)
        self.assertEqual(node2.tag, "a")
        self.assertEqual(node2.value, "Click me!")
        self.assertEqual(node2.props, {"href": "https://www.google.com"})

    def test_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode(tag='p', props={'class': 'greeting'})


class TestParentNode(unittest.TestCase):
    def test_init(self):
        child1 = LeafNode(tag='p', value='Hello, world!', props={'class': 'greeting'})
        child2 = LeafNode(tag='p', value='Goodbye, world!', props={'class': 'farewell'})
        node = ParentNode(tag='div', children=[child1, child2], props={'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.children, [child1, child2])
        self.assertEqual(node.props, {'class': 'container'})

    def test_to_html(self):
        child1 = LeafNode(tag='p', value='Hello, world!', props={'class': 'greeting'})
        child2 = LeafNode(tag='p', value='Goodbye, world!', props={'class': 'farewell'})
        node = ParentNode(tag='div', children=[child1, child2], props={'class': 'container'})
        self.assertEqual(node.to_html(),
                         '<div class="container"><p class="greeting">Hello, world!</p><p class="farewell">Goodbye, '
                         'world!</p></div>')

    def test_tag_required(self):
        with self.assertRaises(ValueError):
            ParentNode(children=[LeafNode(tag='p', value='Hello, world!', props={'class': 'greeting'})])

    def test_children_required(self):
        with self.assertRaises(ValueError):
            ParentNode(tag='div', props={'class': 'container'})


if __name__ == '__main__':
    unittest.main()
