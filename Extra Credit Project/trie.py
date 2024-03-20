'''
Shreya Chetan Pawaskar
12041645
pawaskas@uci.edu
'''
from typing import List

class TrieNode:
    def __init__(self, label=""):
        self.children = {}
        self.is_end_word = False
        self.label = label

class Trie:
    def __init__(self, is_compressed):
        self.is_compressed = is_compressed
        self.root = TrieNode()
        self.is_trie = True

    def construct_trie_from_text(self, text):
        """Constructs a trie from the given list of words."""
        self.is_trie = True
        for key in text:
            node = self.root
            # Insert key into the trie
            for char in key:
                if char not in node.children:
                    node.children[char] = TrieNode(char)
                node = node.children[char]
            node.is_end_word = True

        if self.is_compressed:
            self.compress_trie(self.root)

    def compress_trie(self, node: TrieNode, parent=None, char=None):
        """Compresses the trie recursively."""
        while len(node.children) == 1 and not node.is_end_word:
            next_node = next(iter(node.children.values()))
            node.label += next_node.label  # Concatenate labels
            #Update children
            node.children = next_node.children
            node.is_end_word = next_node.is_end_word
            if parent:
                parent.children[char] = node
        for char, child in list(node.children.items()):
            #Recursively compress the child nodes
            self.compress_trie(child, node, char)

    def construct_suffix_tree_from_text(self, keys: List[str]):
        """Constructs a suffix tree from the given list of words."""
        for key in keys:
            for i in range(len(key)):
                key1=key[i:]
                node = self.root
                # Insert each suffix into the suffix tree
                for char in key1:
                    if char not in node.children:
                        node.children[char] = TrieNode(char)
                    node = node.children[char]
                node.is_end_word = True
            
        if self.is_compressed:
            self.compress_suffix(self.root)

    def compress_suffix(self, node: TrieNode, parent=None, char=None):
        """Constructs a suffix tree from the given list of words."""
        while len(node.children) == 1 and not node.is_end_word:
            next_node = next(iter(node.children.values()))
            node.label += next_node.label 
            # Update children and end of word flag
            node.children = next_node.children
            node.is_end_word = next_node.is_end_word
            if parent:
                parent.children[char] = node
        # Recursively compress child nodes
        for char, child in list(node.children.items()):
            self.compress_suffix(child, node, char)

    def insert_suffix_tree(self, suffix):
        """Inserts a suffix into the suffix tree."""
        node = self.root
        if self.is_compressed:
            common_prefix = ''
            for char in suffix:
                if char in node.children:
                    common_prefix += char
                    node = node.children[char]
                else:
                    break
            for char in suffix[len(common_prefix):]:
                if char not in node.children:
                    new_node = TrieNode()
                    node.children[char] = new_node
                node = node.children[char]
            node.is_end_word = True
        else:
            node = self.root
            for char in suffix:
                if char not in node.children:
                    new_node = TrieNode(char)
                    node.children[char] = new_node
                node = node.children[char]
            #Mark the last node True
            node.is_end_word = True

    def search_and_get_depth(self, key):
        """Searches for a key in the trie or suffix tree and returns its depth."""
        node = self.root
        #set a depth variable
        depth = 0
        #set i=0
        i = 0
        while i < len(key):
            flag = False
            for x, child in node.children.items():
                if key[i : i + len(child.label)] == child.label:
                    flag = True
                    depth = depth + 1
                    node = child
                    i = i+len(child.label)
                    break
            if flag==False:
                return -1
        return depth if node.is_end_word and node else -1
