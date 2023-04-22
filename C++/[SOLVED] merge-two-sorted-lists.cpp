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

ListNode *interweave(ListNode *a, ListNode *b)
{
    // If both are the same node
    if (a == b) {
        return a;
    }

    // If both elements are last in line
    // Connect least -> greater and return the least
    if (a->next == nullptr && b->next == nullptr)
    {
        if (a->val <= b->val)
        {
            a->next = b;
            return a;
        }
        else
        {
            b->next = a;
            return b;
        }
    }

    // If one of them is least and last in line
    if (a->val <= b->val && a->next == nullptr)
    {
        a->next = interweave(b, b->next);

        return a;
    }
    if (b->val < a->val && b->next == nullptr)
    {
        b->next = interweave(a, a->next);
        return b;
    }

    // If one of them is larger and last in line
    // if (a->val <= b->val && )

    // If both are not last in line
    if (a->val <= b->val)
    {
        ListNode *a_next = a->next ;
        // connect the least one to the greater one
        a->next = interweave(a_next, b);
        // call interweave on the least->next and the greater

        // return the least
        return a;
    }
    else
    {
        ListNode *b_next = b->next;
        b->next = interweave(b_next, a);

        return b;
    }

}

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        if (list1 == nullptr && list2 == nullptr)
        {
            return nullptr;
        }
        if (list1 == nullptr)
        {
            return list2;
        }
        if (list2 == nullptr)
        {
            return list1;
        }

        return interweave(list1, list2);
    }
};

int main(void)
{
    Solution sol;

    ListNode a2, a1;
    a2.val = 3;
    a2.next = nullptr;
    a1.val = -9;
    a1.next = &a2;
    ListNode b2, b1;
    b2.val = 7;
    b2.next = nullptr;
    b1.val = 5;
    b1.next = &b2;

    // ListNode a3, a2, a1;
    // a3.val = 4;
    // a3.next = nullptr;
    // a2.val = 2;
    // a2.next = &a3;
    // a1.val = 1;
    // a1.next = &a2;
    // ListNode b3, b2, b1;
    // b3.val = 4;
    // b3.next = nullptr;
    // b2.val = 3;
    // b2.next = &b3;
    // b1.val = 1;
    // b1.next = &b2;

    dispay_list(&a1);
    dispay_list(&b1);

    ListNode *result = sol.mergeTwoLists(&a1, &b1);

    dispay_list(result);

    // cout << result.val << result->next << endl;

    return 0;
}
