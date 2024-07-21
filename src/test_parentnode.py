from parentnode import ParentNode
from leafnode import LeafNode

import unittest

class TestParentNode(unittest.TestCase):
    def test_has_no_tag(self):
        self.assertRaises(ValueError)
    
    def test_has_no_children(self):
        self.assertRaises(ValueError)
        
    def test_has_children(self):
        node = ParentNode("p", [LeafNode("p", "This is a text node")])
        self.assertEqual("<p>This is a child node</p>", node.children)
    
    def test_render_tag(self):
        node = ParentNode("p", [ParentNode("p", "This is a text node")])
        self.assertEqual("<p><p>This is a text node</p></p>", node.to_html())
    
    def test_render_props(self):
        node = ParentNode("p", [ParentNode("p", "This is a text node")], {"class": "text"})
        self.assertEqual('<p class="text"></p>', node.to_html())
