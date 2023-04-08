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
        
        # print(result_num)
        
        # result = ListNode(int(result_num.pop()), None)
        # print(result.val)
        
        result = ListNode(0, None)
        
        # print(result_num[0:])
        # print(result_num[1:])
        
        for char in reversed(result_num):
            # print(char)
            pass
        
        return result
        

        # order_inc = False

        # a1 = l1.val + l2.val

        # if a1 >= 10:
        #     a1 -= 10
        #     order_inc = True

        # result = ListNode(a1, None)

        # l1 = l1.next
        # l2 = l2.next

        # a2 = l1.val + l2.val + 1 if order_inc else l1.val + l2.val
        # order_inc = False

        # if a2 >= 10:
        #     a2 -= 10
        #     order_inc = True

        # result.next = ListNode(a2, None)

        # l1 = l1.next
        # l2 = l2.next

        # a3 = l1.val + l2.val + 1 if order_inc else l1.val + l2.val
        # order_inc = False

        # result.next.next = ListNode(a3, None)

        # return result


solution = Solution()

l1_3 = ListNode(2, None)
l1_2 = ListNode(4, l1_3)
l1_1 = ListNode(3, l1_2)

l2_3 = ListNode(5, None)
l2_2 = ListNode(6, l2_3)
l2_1 = ListNode(4, l2_2)

# print(l1_1.val, l1_1.next.val, l1_1.next.next.val)
# print(l2_1.val, l2_1.next.val, l2_1.next.next.val)

string = ''

# print(read(l1_1, string))
# print(read(l2_1, string))

result = solution.addTwoNumbers(l1_1, l2_1)

l3 = ListNode()

write(l3, '5509')
read(l3)



# print(result)
# print(result.val, result.next.val, result.next.next.val)
