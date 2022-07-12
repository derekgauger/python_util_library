"""
Author: Derek Gauger
Date: 07/06/2022

Purpose:
I wanted to start adding a few basic data structure implementations to my GitHub. Most likely this implementation
will never be used, but it is a good exercise to do for practice.

Description:
This is a very basic implementation of a LinkedList. I only wanted to do creation of, adding to, and removing from
the LinkedList.
"""


# Class that represents a Node/Element within the LinkedList
class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


# LinkedList implementation
class LinkedList:

    # Constructor
    def __init__(self):
        self.root = None
        self.size = 0

    # Function for allowing us to use len(linked_list)
    def __len__(self):
        return self.size

    # Function for turning the LinkedList into a string for printing purposes
    def __str__(self):
        current = self.root
        output = str(current.data)

        while type(current.next) is Node:
            current = current.next
            output += " -> " + str(current.data)

        return output

    # Function for adding an element to the LinkedList
    def add(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.root = new_node
        else:
            current = self.root
            while type(current.next) is Node:
                current = current.next
            current.next = new_node

        self.size += 1

    # Function for adding more than one element to the LinkedList
    # 'element_list' can contain Node objects or just values
    def add_many(self, element_list):

        for element in element_list:
            if type(element) is Node:
                self.add(element.data)
            else:
                self.add(element)

    # Function for getting a Node at an index
    def get_index(self, index):
        current = self.root
        for i in range(index):
            if type(current.next) is Node:
                current = current.next
            else:
                return -1

        return current

    # Function for getting the index of the first instance of a value in the LinkedList
    def get_value(self, value):
        current = self.root
        index = 0
        while type(current) is Node:
            if current.data == value:
                return index
            else:
                current = current.next
            index += 1

        if index == self.size:
            return -1
        else:
            return index

    # Function for removing an index from the LinkedList
    def remove_index(self, index):

        if index == 0:
            original_root = self.root
            self.root = self.root.next
            return original_root

        last = None
        current = self.root
        for i in range(index):
            if type(current.next) is Node:
                last = current
                current = current.next
            else:
                raise IndexError("List index out-of-bounds")

        last.next = current.next

        return current

    # Function for removing the first instance of a value in the LinkedList
    def remove_value(self, value):

        current = self.root
        if current.data == value:
            original_root = self.root
            self.root = self.root.next
            return original_root

        while type(current.next) is Node:
            last = current
            current = current.next
            if current.data == value:
                last.next = current.next
                return current

        raise ValueError("Value '{}' Not Found In List".format(value))
