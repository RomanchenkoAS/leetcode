/*You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.*/

#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void dispay_list(ListNode *list)
{
    cout << list->val << " ";
    if (list->next == nullptr)
    {
        cout << endl;
        return;
    }
    else
    {
        dispay_list(list->next);
    }
}

ListNode *interweave(ListNode * a, ListNode * b)
{
    if (a->val >= b->val)
    {
        // If there is a b.next
        if (b->next != nullptr)
        {
            ListNode *_tmp = b->next;
            b->next = a;
            interweave(_tmp, a);
        }
        else
        {
            // If there isn't b.next, only a.next
            b->next = a;
            if (a->next != nullptr)
            {
                interweave(a, a->next);
            }
            else
            {
                return nullptr;
            }
        }
        return b;
    }
    else
    {
        // If there is an a.next
        if (a->next != nullptr)
        {
            ListNode *_tmp = a->next;
            a->next = b;
            interweave(_tmp, b);
        }
        else
        {
            // If there isn't b.next, only a.next
            a->next = b;
            if (b->next != nullptr)
            {
                interweave(b, b->next);
            }
            else
            {
                return nullptr;
            }
        }
        return a;
    }
}

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        if (list1 == nullptr && list2 == nullptr) {
            return nullptr;
        }
        if (list1 == nullptr) {
            return list2;
        }
        if (list2 == nullptr) {
            return list1;
        }

        return interweave(list1, list2);
    }
};

int main(void)
{
    Solution sol;

    ListNode a3, a2, a1;
    a3.val = 4;
    a3.next = nullptr;
    a2.val = 2;
    a2.next = &a3;
    a1.val = 1;
    a1.next = &a2;
    ListNode b3, b2, b1;
    b3.val = 4;
    b3.next = nullptr;
    b2.val = 3;
    b2.next = &b3;
    b1.val = 1;
    b1.next = &b2;

    dispay_list(&a1);
    dispay_list(&b1);

    ListNode *result = sol.mergeTwoLists(&a1, &b1);

    dispay_list(result);

    // cout << result.val << result->next << endl;

    return 0;
}
