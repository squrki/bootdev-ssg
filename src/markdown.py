import re

from textnode import TextType, TextNode

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
    alt_texts = re.findall(r"!\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)
    pairs = []
    for i in range(len(urls)):
        pairs.append((alt_texts[i], urls[i]))
    return pairs

def extract_markdown_links(text):
    alt_texts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)
    pairs = []
    for i in range(len(urls)):
        pairs.append((alt_texts[i], urls[i]))
    return pairs

def split_nodes_image(old_nodes):
    nodes = []
    for o in old_nodes:
        images = extract_markdown_images(o.text)
        for i in images:
            t = o.text.find(i[0])
            nodes.append(TextNode(o.text[:t], TextType.TEXT))



    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    
    return nodes