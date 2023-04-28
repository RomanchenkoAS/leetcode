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

int calculate_depth(ListNode *list, int iterator) // Count list depth
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

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};