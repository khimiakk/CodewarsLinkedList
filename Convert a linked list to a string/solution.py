"""
simple: task1
"""

def stringify(node):
    """
    Convert a linked list to a string
    """

    str_representation = ''
    if node is None:
        return 'None'
    else:
        while node is not None:
            if node.next is not None:
                str_representation += str(node.data)
                str_representation += ' -> '
            else:
                str_representation += str(node.data)
                str_representation += ' -> None'
            node = node.next

    return str_representation
