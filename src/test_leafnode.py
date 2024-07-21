import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_has_no_value(self):
        self.assertRaises(ValueError)

    def test_has_value(self):
        node = LeafNode("a", "https://www.boot.dev")
        self.assertEqual("https://www.boot.dev", node.value)
    
    def test_has_tag(self):
        node = LeafNode("a", "https://www.boot.dev")
        self.assertEqual("a", node.tag)
    
    def test_render_tag(self):
        node = LeafNode("a", "https://www.boot.dev")
        self.assertEqual("<a>https://www.boot.dev></a>", node.to_html())
    
    def test_render_props(self):
        node = LeafNode("a", "https://www.boot.dev", {"href": "https://www.boot.dev"})
        self.assertEqual('<a href="https://www.boot.dev">https://www.boot.dev</a>', node.to_html())