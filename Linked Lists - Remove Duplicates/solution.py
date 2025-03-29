"""
middle: task3
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    probe = head
    while probe.next is not None and probe.next != "None":
        if probe.data == probe.next.data:
            probe.next = probe.next.next
        else:
            probe = probe.next
    return head
