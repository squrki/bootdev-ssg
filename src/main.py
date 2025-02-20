from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode

print("hello world")

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return HTMLNode("i", text_node.text)
        case TextType.CODE:
            return HTMLNode("code", text_node.text)
        case TextType.LINKS:
            return HTMLNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGES:
            return HTMLNode("img", value = "", props = {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for o in old_nodes:
        start = o.text.find(delimiter)
        end = o.text[start+1:].find(delimiter)
        nodes.append(TextNode(o.text[:start]), TextType.TEXT)
        nodes.append(TextNode(o.text[start+1:end]), text_type)
        nodes.append(TextNode(o.text[end+1:]), TextType.TEXT)
    return nodes

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()