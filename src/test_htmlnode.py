import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"class": "greeting", "id": "main"})
        expected = ' class="greeting" id="main"'
        self.assertEqual(node.props_to_html(), expected)

    def test_none_props(self):
        node = HTMLNode("div", "Hello", [], None)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_tag(self):
        node = HTMLNode("div", "Hello", [], None)
        expected = "div"
        self.assertEqual(node.tag, expected)

    def test_value(self):
        node = HTMLNode("div", "Hello", [], None)
        expected = "Hello"
        self.assertEqual(node.value, expected)

    def test_children(self):
        node = HTMLNode("div", "Hello", [], None)
        expected = []
        self.assertEqual(node.children, expected)

if __name__ == "__main__":
    unittest.main()
