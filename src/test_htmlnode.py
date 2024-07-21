import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a text node")
        node2 = HTMLNode("p", "This is a text node")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("p", "This is a text node")
        node2 = HTMLNode("p", "This is a text node2")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode("p", "This is a text node")
        node2 = HTMLNode("p", "This is a text node", "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "This is a text node")
        self.assertEqual("HTMLNode(p, This is a text node, None, None)", repr(node))


if __name__ == "__main__":
    unittest.main()
