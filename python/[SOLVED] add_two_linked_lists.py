# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def read(l, result):
    """ Recursive function to read linked list int integer """
    if l.next == None:
        return str(l.val)
    return read(l.next, result) + str(l.val)

def write(l, input):
    l.val = input[0]
    
    if len(input) == 1:
        return
    else:     
        l.next = ListNode()
        write(l.next, input[1:])
    

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_num = read(l1, '')
        l2_num = read(l2, '')
        
        result_num = str(int(l1_num) + int(l2_num))
                
        result = ListNode(0, None)
        
        write(result, "".join(reversed(result_num)))
        
        return result
    

solution = Solution()

l1_3 = ListNode(2, None)
l1_2 = ListNode(4, l1_3)
l1_1 = ListNode(3, l1_2)

l2_3 = ListNode(5, None)
l2_2 = ListNode(6, l2_3)
l2_1 = ListNode(4, l2_2)

print(l1_1.val, l1_1.next.val, l1_1.next.next.val)
print(l2_1.val, l2_1.next.val, l2_1.next.next.val)


result = solution.addTwoNumbers(l1_1, l2_1)


print(result)
print(result.val, result.next.val, result.next.next.val)
