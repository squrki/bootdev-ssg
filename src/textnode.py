from enum import Enum

class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINKS = "Links"
    IMAGES = "Images"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text:
            if self.text_type == other.text_type:
                if self.url == other.url:
                    return True
        return False

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")
            
