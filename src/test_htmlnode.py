import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        expected = "Hello, world!"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_nesting_parents(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        grandparent = ParentNode("section", [parent])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        child1 = LeafNode("span", "one")
        child2 = LeafNode("b", "two")
        child3 = LeafNode(None, "three")
        parent = ParentNode("div", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<div><span>one</span><b>two</b>three</div>",
        )

    def test_to_html_no_children(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_no_tag(self):
        child = LeafNode("b", "child")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

if __name__ == "__main__":
    unittest.main()
