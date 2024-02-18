from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen_nodes = {}

        # Edge cases
        if head is None:
            return None
        if head.next is None:
            if head.random is None:
                return Node(x=head.val, next=None, random=None)
            else:
                new_head = Node(x=head.val, next=None, random=None)
                new_head.random = new_head
                return new_head


        # Iterate over initial list, make copy nodes and save relation "old_node:new_node" to the dict
        new_stable_head = new_moving_head = None
        while head is not None:
            new_node = Node(x=head.val, next=None, random=head.random)
            seen_nodes[head] = new_node

            if new_moving_head is None:
                # For a fist node just assign, keep stable_head at that point
                new_moving_head = new_node
                new_stable_head = new_node
            else:
                # For next nodes - connect prev. to current
                new_moving_head.next = new_node
                new_moving_head = new_moving_head.next

            # Move head a step forward
            head = head.next

        # For each node in a new list we need to fix "random" field according to dict
        new_moving_head = new_stable_head
        while new_moving_head is not None:
            if new_moving_head.random is not None:
                new_moving_head.random = seen_nodes[new_moving_head.random]
            new_moving_head = new_moving_head.next

        return new_stable_head
