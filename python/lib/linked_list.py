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
