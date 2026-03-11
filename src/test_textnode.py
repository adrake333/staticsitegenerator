import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("LOTR is the best", TextType.ITALIC, "https://www.lotrisbest.com")
        node2 = TextNode("LOTR is the best", TextType.ITALIC, "https://www.lotrisbest.com")
        self.assertEqual(node, node2)

    def test_noteq1(self):
        node = TextNode("LOTR is the best", TextType.BOLD, "https://www.lotrisbest.com")
        node2 = TextNode("Star Wars is the best", TextType.BOLD, "https://www.lotrisbest.com")
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = TextNode("LOTR is the best", TextType.BOLD, "https://www.lotrisbest.com")
        node2 = TextNode("LOTR is the best", TextType.ITALIC, "https://www.lotrisbest.com")
        self.assertNotEqual(node, node2)

    def test_noteq3(self):
        node = TextNode("LOTR is the best", TextType.ITALIC, "https://www.lotrisbest.com")
        node2 = TextNode("LOTR is the best", TextType.ITALIC, "https://www.starwarsisbest.com")
        self.assertNotEqual(node, node2)

    def test_noteq4(self):
        node = TextNode("LOTR is the best", TextType.BOLD, "https://www.lotrisbest.com")
        node2 = TextNode("LOTR is the best", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("Click Here", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click Here")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("fancy image", TextType.IMAGE, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.example.com/image.png", "alt": "fancy image"})


if __name__ == "__main__":
    unittest.main()
