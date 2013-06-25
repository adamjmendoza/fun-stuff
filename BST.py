#!/usr/bin/env python

import sys
from collections import deque

class BSTNode(object):
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return self == self.parent.right

    def is_root(self):
        return not self.parent

    def inorder(self):
        s = ""
        if self.left:
            s += "{}".format(self.left.inorder())
        s += " {} ".format(self.key)
        if self.right:
            s += "{}".format(self.right.inorder())
        return s

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return '( {} <{}> {} )'.format(self.left or '*', self.key, self.right or '*')

class BST(object):
    def __init__(self, root=None):
        self.root = root
        self.depth = 1 if root else 0

    def search(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
            
    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key=key)
            return
        current_node = self.root
        depth = 1
        while current_node is not None:
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = BSTNode(key=key, parent=current_node)
                    current_node = None
                else:
                    current_node = current_node.left
                    depth += 1
            elif key > current_node.key:
                if current_node.right is None:
                    current_node.right = BSTNode(key=key, parent=current_node)
                    current_node = None
                else:
                    current_node = current_node.right
                    depth += 1
            else:
                current_node = None
        self.depth = max(depth, self.depth)

    def immediate_predecessor(self, node):
        node = node.left
        while node.right is not None:
            node = node.right
        return node

    def immediate_successor(self, node):
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        delete_node = self.search(key)
        if delete_node is None:
            return None

        if delete_node.left is None or delete_node.right is None:
            splice_node = delete_node
        else:
            splice_node = self.immediate_successor(delete_node)

        if splice_node.left is not None:
            splice_child = splice_node.left
        else:
            splice_child = splice_node.right

        if splice_child is not None:
            splice_child.parent = splice_node.parent

        if splice_node.is_root():
            self.root = splice_child
        else:
            if splice_node.is_left_child():
                splice_node.parent.left = splice_child
            else:
                splice_node.parent.right = splice_child

        if splice_node != delete_node:
            delete_node.key = splice_node.key

    def graph(self):
        current_height = 0
        pad = 80
        q = deque([(self.root, 1)])
        g = ""
        while len(q):
            node, height = q.popleft()
            if height > current_height:
                current_height = height
                pad /= 2
                g += "\n{}".format(" "*pad)
            if node:
                q.append((node.left, height+1))
                q.append((node.right, height+1))
                g += "{}{}".format(node.key, " "*pad*2)
            else:
                g += "{}".format(" "*(pad*2+2))
        return g
                

    def inorder(self):
        if self.root:
            return self.root.inorder()

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u'{}'.format(self.root)

def main(args):
    tree = BST()
    tree.insert(10)
    tree.insert(1)
    tree.insert(2)
    tree.insert(0)
    tree.insert(12)
    tree.insert(11)
    tree.insert(20)
    tree.insert(23)
    print tree
    print tree.inorder()
    print tree.graph()
    

if (__name__ == '__main__'):
    main(sys.argv[1:])
