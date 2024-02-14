from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val: int = val
        self.next: ListNode = next

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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return None

        reversed_list_head = self.reverseList(head)
        current_node = reversed_list_head
        previous_node = None

        if n == 1:
            return self.reverseList(current_node.next)

        for i in range(n - 1):
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            previous_node.next = None
        else:
            previous_node.next = current_node.next

        return self.reverseList(reversed_list_head)

s = Solution()
head = ListNode()
head.take_input(list(range(12)))
head.print_list()
n = 3
res = s.removeNthFromEnd(head, n)
res.print_list()
