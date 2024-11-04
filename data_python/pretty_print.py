from __future__ import print_function


def tree_print(tree):
    for key in tree:
        print(key, end=' ')
        tree_element = tree[key] 
        for subElem in tree_element:
            print(" -> ", subElem, end=' ')
            if type(subElem) != str:
                print("\n ")
        print()
