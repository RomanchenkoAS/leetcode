from typing import Optional

from ..lib import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next == head:
            return True
        if head.next is None:
            return False

        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
