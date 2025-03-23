import pytest
from balanced_binary_search_tree.avl_tree import AVLTree

def test_insert_and_search():
    avl = AVLTree()
    keys = [5, 3, 8, 1, 4]
    for key in keys:
        avl.insert_key(key)

    for key in keys:
        node = avl.search_key(key)
        assert node is not None, f"Key {key} not found"
        assert node.key == key
