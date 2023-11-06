# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from lib.linked_list import ListNode

class Solution:
    def find_middle_node(self, head: ListNode):
        mid = 0
        slow, fast = head, head

        def has_next_next(node: ListNode):
            if node.next:
                if node.next.next:
                    return True
            return False

        while has_next_next(fast):
            mid += 1
            slow = slow.next
            fast = fast.next.next

        return slow, mid

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # FIND THE MIDDLE BY USING FAST/SLOW ITERATORS
        # CUT OUT RIGHT PART AND REORDER IT
        # COMPOSE IN RESULTING LIST


s = Solution()

head = ListNode()
head.take_input(list(range(5)))
head.print_list()

s.find_middle_node(head)