from htmlnode import HTMLNode

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
