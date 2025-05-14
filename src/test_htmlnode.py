from htmlnode import HTMLNode

def test_tag_and_value_only():
    node = HTMLNode(tag="p", value="Hello world")
    assert node.props_to_html() == ""

def test_props():
    node = HTMLNode(tag="a", value="google.com", props={"href": "https://boot.dev", "target": "_blank"})
    assert node.props_to_html() == ' href="https://boot.dev" target="_blank"'

def test_child():
    child1 = HTMLNode(tag="p", value="child one")
    child2 = HTMLNode(tag="p", value="child two")
    parent = HTMLNode(tag="div", children=[child1, child2])

    assert parent.props_to_html() == ""
    assert len(parent.children) == 2
    assert isinstance(parent.children[0], HTMLNode)

if __name__ == "__main__":
    test_tag_and_value_only()
    test_props()
    test_child()