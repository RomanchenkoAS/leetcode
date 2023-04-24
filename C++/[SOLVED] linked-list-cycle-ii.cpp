/*Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.*/

#include <iostream>
#include <unordered_set>
#include <unistd.h>

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

class Solution
{
public:
    // ListNode *detectCycle(ListNode *head)
    // {

    //     if (head == nullptr)
    //     {
    //         return nullptr;
    //     }

    //     unordered_set<ListNode *> checked;

    //     ListNode *current = head;

    //     checked.insert(head);

    //     while (current->next != nullptr)
    //     {
    //         current = current->next;
            
    //         if (checked.find(current) != checked.end())
    //             return current;
    //         checked.insert(current);
    //     }
    //     return nullptr;
    // }
    ListNode *detectCycle(ListNode *head) {
        // Floyd's algorythm (hare & tortoise)

        // Empty input scenario
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }

        if (head->next == head) {
            return head;
        }

        ListNode * fast = head;
        ListNode * slow = head;

        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next; // Hare moves two turns at once
            slow = slow->next;       // Tortoise moves one turn

            if (fast == slow) {
                break; // Found cycle
            }
        }

        // No cycle
        if (fast == nullptr || fast->next == nullptr) {
            return nullptr;
        }

        // When they meet, reset the slow one
        slow = head;

        // Move them one turn at the time
        while (slow != fast) {
            fast = fast->next;
            slow = slow->next;
        }
        // When they meet again it is the beginning of the cycle
        return slow;
    }
};

int main(void)
{
    Solution sol;

    ListNode a4, a3, a2, a1, a0;
    // a4.val = -4;
    // a4.next = &a2;
    // a3.val = 0;
    // a3.next = &a4;
    // a2.val = 2;
    // a2.next = &a3;
    // a1.val = 3;
    // a1.next = &a2;
    a1.val = 2;
    a1.next = &a0;
    a0.val = 1;
    a0.next = &a1;

    // cout << "Initial: ";
    // dispay_list(&a1);

    ListNode *result = sol.detectCycle(&a0);

    cout << "Result = " << result->val << endl;

    return 0;
}
