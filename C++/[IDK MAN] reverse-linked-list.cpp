/*Given the head of a singly linked list, reverse the list, and return the reversed list.*/

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

void get_list(vector<ListNode*> *vec, ListNode *list) {
    vec->push_back(new ListNode(*list));

    if (list->next==nullptr) {
        return;
    } else {
        get_list(vec, list->next);
    }
}

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        int depth = calculate_depth(head, 0);
        vector<ListNode*> vec;
        get_list(&vec, head);

        // for (ListNode ln : vec) {
        //     cout << ln.val << " ";
        // }

        for (int i = depth; i >= 0; i --) {
            vec[i]->next = vec[i - 1];
            // cout << vec[i].val << " ";
        }
        vec[0]->next = nullptr;

        head = vec[vec.size() - 1];

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

    cout << "Initial: " ;
    dispay_list(&a1);

    cout << "Depth: " << calculate_depth(&a1, 0) << endl << "Result: ";
    ListNode *result = sol.reverseList(&a1);
    dispay_list(result);

    return 0;
}
