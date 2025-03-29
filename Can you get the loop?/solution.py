"""
hard: task3
"""

def loop_size(node):
    if node is None:
        return None

    slow = node
    fast = node.next

    while fast and fast.next:
        if slow == fast:
            loop = 1
            probe = slow.next
            while probe != slow:
                loop += 1
                probe = probe.next
            return loop
        slow = slow.next
        fast = fast.next.next

    return 0
