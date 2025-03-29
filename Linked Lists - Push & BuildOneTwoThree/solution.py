"""
simple: task3
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    chain = None
    chain = push(chain, 3)
    chain = push(chain, 2)
    chain = push(chain, 1)
    return chain
