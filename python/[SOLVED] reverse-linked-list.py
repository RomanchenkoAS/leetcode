# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display_list(head):
    print(head.val, end=" ")
    if head.next == None:
        print()
        return
    else:
        display_list(head.next)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        node = head
        list = [node]
        while (node.next != None):
            list.append(node.next)
            node = node.next

        # print(list)
        # list.reverse()
        length = len(list) 
        for i in range(0, length):
            # print(i, list[i].val)

            if i == length - 1:
                list[i].next = None
            else:
                list[i].next = list[i + 1]

        return list[0]


l3 = ListNode(8, None)
l2 = ListNode(5, l3)
l1 = ListNode(1, l2)

sol = Solution()

print("Init: ")

display_list(l1)

print("Solution: ")

l1 = sol.reverseList(l1)

display_list(l1)
