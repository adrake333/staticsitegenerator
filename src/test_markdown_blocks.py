from markdown_blocks import markdown_to_blocks, block_to_block_type
import unittest

def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

def test_btbt_valid_heading(self):
    self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

def test_btbt_invalid_heading(self):
    self.assertEqual(block_to_block_type("###Heading"), BlockType.PARAGRAPH)

def test_btbt_valid_code(self):
    self.assertEqual(block_to_block_type("```\ncode\\n```"), BlockType.CODE)

def test_btbt_invalid_code(self):
    self.assertEqual(block_to_block_type("```code\\n```"), BlockType.PARAGRAPH)

def test_btbt_valid_quote(self):
    self.assertEqaul(block_to_block_type("> quote\n> still quote"), BlockType.QUOTE)

def test_btbt_invalid_quote(self):
    self.assertEqual(block_to_block_type("< quote\n > still quote"), BlockType.PARAGRAPH)

def test_btbt_valid_unordered_list(self):
    self.assertEqual(block_to_block_type("- one\n- two\n- three"), BlockType.UNORDERED_LIST)

def test_btbt_invalid_unordered_list(self):
    self.assertEqual(block_to_block_type("one \n two\n three"), BlockType.Paragraph)

def test_btbt_valid_ordered_list(self):
    self.assertEqual(block_to_block_type("1. one\n2. two\n3. three"), BlockType_ORDERED_LIST)

def test_btbt_invalid_ordered_list(self):
    self.assertEqual(block_to_block_type("1. one\n2.two\n3. three"), BlockType.PARAGRAPH)

def test_btbt_valid_paragraph(self):
    self.assertEqual(block_to_block_type("Just a paragraph."), BlockType.PARAGRAPH)
