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
    def __init__(self, root=None, values=None):
        self.root = root
        self.depth = 1 if root else 0
        for v in values:
            self.insert(v)

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
        if node.left:
            node = node.left
            while node.right is not None:
                node = node.right
            return node
        else:
            p = node.parent
            while p is not None and node == p.left:
                node = p
                p = node.parent

    def immediate_successor(self, node):
        if node.right:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:
            p = node.parent
            while p is not None and node == p.right:
                node = p
                p = node.parent

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

    def rotate_left(self, x):
        if x.right is None: return
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        else:
            if x.is_left_child():
                y.parent.left = y
            else:
                y.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, y):
        if y.left is None: return
        x = y.left
        y.left = x.right
        if y.left is not None:
            y.left.parent = x
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y.is_left_child():
                x.parent.left = x
            else:
                x.parent.right = x
        x.right = y
        y.parent = x

    def graph(self):
        if not self.root: return ""
        pad = 128                        # powers of two work best
        q = deque([(self.root, 0, 1)])
        next_q = deque()
        prev_data = None
        g = ""
        while len(q):
            node, height, number = q.popleft()
            if node:
                if node.left:
                    next_q.append((node.left, height+1, 2*number))
                if node.right:
                    next_q.append((node.right, height+1, 2*number+1))
                if prev_data is None:
                    pad /= 2
                    g += " "*pad
                    g += "{}{}".format(" "*2*pad*(number-pow(2, height)), node.key)
                else:
                    g += "{}{}".format(" "*2*pad*(number-prev_data[2]), node.key)
                prev_data = (node, height, number)
            if not len(q):
                q.extend(next_q)
                next_q.clear()
                prev_data = None
                g += "\n"
        return g

    def inorder(self):
        if self.root:
            return self.root.inorder()

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u'{}'.format(self.root)

def main(args):
    tree = BST(values=(7, 4, 3, 2, 6, 11, 9, 18, 14, 12, 17, 19, 22, 20))
    print tree.graph()
    print '#'*128
    node = tree.search(11)
    tree.rotate_left(node)
    print tree.graph()
    print '#'*128
    tree.rotate_right(node)
    print tree.graph()
    print '#'*128
    tree.rotate_right(node)
    print tree.graph()
    print '#'*128
    tree.rotate_right(node)
    print tree.graph()
    print '#'*128
    tree.rotate_left(node)
    print tree.graph()

if (__name__ == '__main__'):
    main(sys.argv[1:])
