from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        node = head
        nodelist = []
        while node.next:
            nodelist.append(node)

        nodelist.reverse()
        for i in range(len(nodelist) - 1):
            node[i].next = nodelist[i + 1]

        print()


s = Solution()
head = [1, 2, 3, 4, 5]
print(s.reverseList(head))
