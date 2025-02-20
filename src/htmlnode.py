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