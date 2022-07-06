"""
Author: Derek Gauger
Date: 07/06/2022

Purpose:
I wanted to start adding a few basic data structure implementations to my GitHub. Most likely this implementation
will never be used, but it is a good exercise to do for practice.

Description:
This is a very simple queue Python implementation. I did not do a Stack data structure because it would have been
even simpler than this one.
"""


class Queue:
    
    # Constructor
    def __init__(self):
        self.array = []
        
    # Function that allows us to use len(queue)
    def __len__(self):
        return len(self.array)

    # Function that allows us to use str(queue) for printing
    def __str__(self):
        output = "Queue Order:\n"
        for i in range(len(self)):
            index = len(self) - i - 1
            output += "{}. {}\n".format(i + 1, self.array[index])

        return output

    # Function that adds an item to the queue
    def enqueue(self, item):
        self.array = [item] + self.array

    # Function that removes the item to the queue
    def dequeue(self):
        popped_element = self.array[len(self) - 1]
        del self.array[len(self) - 1]
        return popped_element

    # Function that peeks at the first item in the queue
    def front(self):
        return self.array[len(self) - 1]

    # Function that peeks at the last item in the queue
    def rear(self):
        return self.array[0]
