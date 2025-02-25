class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props = ""
        for k, v in self.props.items():
            props += f" {k}=\"{v}\""
        return props
    
    def __repr__(self):
        print(self.tag)
        print(self.value)
        print(self.children)
        print(self.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, props)
        self.tag = tag
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")
        if self.children is None:
            raise ValueError("missing children")
        html = f"<{self.tag}>"
        for c in self.children:
            if c.tag is None:
                html +=f"{c.value}"
            else:
                html +=f"<{c.tag}>{c.value}</{c.tag}>"
        html = f"</{self.tag}>"
        return html
