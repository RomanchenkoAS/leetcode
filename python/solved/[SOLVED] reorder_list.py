from typing import Optional

from lib.linked_list import ListNode


class Solution:
    def find_middle_node(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        def has_next_next(node: ListNode):
            if node.next:
                if node.next.next:
                    return True
            return False

        while has_next_next(fast):
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        new_list = None
        while head:
            new_node = head.next
            head.next = new_list
            new_list = head
            head = new_node
        return new_list

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Does not return anything, modifies head in-place instead.
        """
        if head is None or head.next is None:
            return

        # FIND THE MIDDLE BY USING FAST/SLOW ITERATORS
        center_node = self.find_middle_node(head)

        # CUT OUT RIGHT PART AND REORDER IT
        right = center_node.next
        center_node.next = None

        right = self.reverseList(right)

        left = head
        # COMPOSE IN RESULTING LIST
        while (left is not None and right is not None):
            tmp = right.next
            right.next = left.next
            left.next = right
            right = tmp
            left = left.next.next


s = Solution()

head = ListNode()
head.take_input(list(range(6)))

s.reorderList(head=head)
