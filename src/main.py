from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
import re

print("hello world")


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()