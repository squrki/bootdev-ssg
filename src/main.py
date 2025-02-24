from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
import re

print("hello world")

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
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
        if o.text_type != TextType.TEXT:
            nodes.append(o)
            continue
        text_list = o.text.split(delimiter)
        if len(text_list) < 3:
            raise Exception("invalid Markdown syntax")
        nodes.append(TextNode(text_list[0]), TextType.TEXT)
        nodes.append(TextNode(text_list[1]), text_type)
        nodes.append(TextNode(text_list[2]), TextType.TEXT)
    return nodes

def extract_markdown_images(text):
    alt_texts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)
    pairs = []
    for i in range(len(urls)):
        pairs.append((alt_texts[i], urls[i]))
    return pairs

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()