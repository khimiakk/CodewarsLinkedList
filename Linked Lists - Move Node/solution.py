"""
simple: task5
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError()

    head, head_next = source, source.next
    head.next = dest

    return Context(head_next, head)
