/*Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.*/

#include <iostream>
#include <vector>

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

int calculate_depth(ListNode *list, int iterator)
{
    if (list->next == nullptr)
    {
        return ++iterator;
    }
    else
    {
        iterator = calculate_depth(list->next, iterator);
        return ++iterator;
    }
}

class Solution
{
public:
    ListNode *middleNode(ListNode *head)
    {

        if (head == nullptr)
        {
            return nullptr;
        }

        short middle_index = calculate_depth(head, 0) / 2;

        for (short i = 0; i < middle_index; i++)
        {
            head = head->next;
        }

        return head;
    }
};

int main(void)
{
    Solution sol;

    ListNode a4, a3, a2, a1;
    a4.val = 7;
    a4.next = nullptr;
    a3.val = 4;
    a3.next = &a4;
    a2.val = 2;
    a2.next = &a3;
    a1.val = 1;
    a1.next = &a2;

    cout << "Initial: ";
    dispay_list(&a1);

    ListNode *result = sol.middleNode(&a1);

    cout << result->val << endl;

    return 0;
}
