"""
hard: task1
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    a = Node(0)
    a.next = head
    probe = a

    while probe.next is not None and probe.next.next is not None:
        first = probe.next
        second = first.next
        first.next, second.next, probe.next = second.next, first, second

        probe = first

    return a.next
