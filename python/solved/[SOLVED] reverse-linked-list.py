from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        node = self
        while node is not None:
            if node.next:
                print(node.val, end=" > ")
            else:
                print(node.val)

            node = node.next

    def take_input(self, list):
        node = self
        for i in range(len(list) - 1):
            node.next = ListNode()
            node = node.next
        node.next = None

        node = self
        for i in list:
            node.val = i
            node = node.next


class Solution:
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


s = Solution()
head = ListNode()
head.take_input([1, 2, 3, 4, 5])
head.print_list()

new_head = s.reverseList(head)
new_head.print_list()
