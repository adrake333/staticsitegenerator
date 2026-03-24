import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_title(self):
        markdown = "# This is the title"
        expected = "This is the title"
        self.assertEqual(extract_title(markdown), expected)

    def test_no_h1(self):
        markdown = "This line has no markdown"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_title_not_first_line(self):
        markdown = "This is the first line.\n# This is the title\nThis is the next line"
        expected = "This is the title"
        self.assertEqual(extract_title(markdown), expected)
