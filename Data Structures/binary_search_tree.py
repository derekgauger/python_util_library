"""
Author: Derek Gauger
Date: 07/07/2022

Purpose:
I wanted to start adding a few basic data structure implementations to my GitHub. Most likely this implementation
will never be used, but it is a good exercise to do for practice.

Description:
This is a Binary Search Tree implementation. This might be useful to me because of the number of times I have
had to create binary search trees from scratch for classes. This was a good exercise to do to refresh up
on my data structure for a tree.
"""


# Class for a node
class Node:

    # Constructor
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    # Allows us to use the node as a string
    def __str__(self):
        return str(self.data)


# Class for Binary Search Tree
class BST:

    # Constructor
    def __init__(self):
        self.root = None

    # Method called for inserting into the tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_helper(self.root, value)

    # Main helper function for insertion where the recursion happens
    def _insert_helper(self, base, value):
        new_node = Node(value)
        if value > base.data:
            if base.right is None:
                base.right = new_node
            else:
                self._insert_helper(base.right, value)

        elif value < base.data:
            if base.left is None:
                base.left = new_node
            else:
                self._insert_helper(base.left, value)

        return new_node

    # Method called for searching the tree
    def search(self, value):
        if self.root == value:
            return self.root
        else:
            return self._search_helper(self.root, value)

    # Main helper method for searching the tree where the recursion happens.
    def _search_helper(self, base, value):

        if base is None:
            return None

        if value > base.data:
            return self._search_helper(base.right, value)
        elif value < base.data:
            return self._search_helper(base.left, value)
        else:
            return base

    # Puts the tree in order
    def inorder(self):
        sorted_list = []
        self._inorder_helper(self.root, sorted_list)
        return sorted_list

    # Does the work to put the tree in order
    def _inorder_helper(self, base, sorted_list):
        if base:
            self._inorder_helper(base.left, sorted_list)
            sorted_list.append(base)
            self._inorder_helper(base.right, sorted_list)

    # Reverses the order of the tree
    def reversed_order(self):
        sorted_list = []
        self._reversed_order_helper(self.root, sorted_list)
        return sorted_list

    # Does the work to reverse the order of the tree
    def _reversed_order_helper(self, base, sorted_list):
        if base:
            self._reversed_order_helper(base.right, sorted_list)
            sorted_list.append(base)
            self._reversed_order_helper(base.left, sorted_list)

    # Gets the parent node of the specific node value passed in
    def get_parent(self, value):
        if self.root.data == value:
            return -1

        return self._get_parent_helper(self.root, value)

    # Helps get the parent node of the value passed in
    def _get_parent_helper(self, base, value):
        if base is None:
            return None

        if value > base.data:
            if base.right.data == value:
                return base
            return self._get_parent_helper(base.right, value)
        else:
            if base.left.data == value:
                return base
            return self._get_parent_helper(base.left, value)

    # Finds the depth of a node
    def get_depth(self, value):
        root = self.search(value)
        return self._get_depth_helper(root)

    # Helps find the depth of a node
    def _get_depth_helper(self, base):

        if base is None:
            return 0

        return max(self._get_depth_helper(base.left), self._get_depth_helper(base.right)) + 1

    # Finds the minimum value of a branch of the tree
    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    # Deletes a node from the tree
    def delete(self, value):
        return self._delete_helper(self.root, value)

    # Helper method to delete a node from the tree.
    def _delete_helper(self, base, value):

        if base is None:
            return base

        if value > base.data:
            base.right = self._delete_helper(base.right, value)

        elif value < base.data:
            base.left = self._delete_helper(base.left, value)

        else:
            if base.left is None:
                temp = base.right
                base = None
                return temp

            elif base.right is None:
                temp = base.left
                base = None
                return temp

            temp = self.min_value_node(base.right)

            base.data = temp.data

            base.right = self._delete_helper(base.right, temp.data)

        return base
    
