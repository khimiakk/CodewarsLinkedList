"""
simple: task4
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if not node:
        raise IndexError()
    probe = node
    count = 0
    while probe:
        if count == index:
            return probe
        if probe.next is None:
            raise IndexError()
        count +=1
        probe = probe.next
