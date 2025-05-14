import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("Some text", TextType.LINK, "https://www.google.com")
        node2 = TextNode("Some text", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none(self):
        node = TextNode("Some text", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Some text", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("Some text", TextType.LINK)
        node2 = TextNode("Some text", TextType.LINK)
        self.assertEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("Some text", TextType.BOLD, "https://example.com")
        node2 = TextNode("Some text", TextType.ITALIC, "https://example.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()