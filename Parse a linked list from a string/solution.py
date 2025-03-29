"""
simple: task2
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s is None or s == 'None':
        return None
    nodes = s.split(' -> ')

    head = Node(int(nodes[0]))
    probe = head

    for node in nodes[1:]:
        if node is not None and node != 'None':
            probe.next = Node(int(node))
            probe = probe.next

    return head
