class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        
        if children == None:
            self.children = []
        else:
            self.children = children
        
        if props == None:
            self.props = {}
        else:
            self.props = props

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props_list = []
        for key, value in self.props.items():
            props_list.append(f' {key}="{value}"')
        
        return "".join(props_list)