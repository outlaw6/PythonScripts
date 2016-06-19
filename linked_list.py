
# linked list
# in Pythonic way


#!/bin/env/python

class Node:

    def __init__(self, cargo=None, next=None):

        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def printCurrent(self):
        return self.cargo

    def printNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = None

    def insert(self, node):
        new_node = Node(node)
        new_node.setNext(self.head)
        self.head = new_node
        




if __name__ == '__main__':

    a = LinkedList()

    a.insert(1)
    a.insert(2)
