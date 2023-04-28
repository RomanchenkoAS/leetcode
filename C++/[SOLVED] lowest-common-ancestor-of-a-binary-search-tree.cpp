/*Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to
be a descendant of itself).”*/

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        if (!root)
        {
            return nullptr;
        }
        //     // If both p & q are less than root then the answer is lower to the right
        //     if (root->val < p->val && root->val < q->val) {
        //         return lowestCommonAncestor(root->right, p, q);
        //     }
        //     // If root is higher than both, answer is to the left
        //     if (root->val > p->val && root->val > q->val) {
        //         return lowestCommonAncestor(root->left, p, q);
        //     }
        //     // If root is between p and q it is the answer
        //     return root;

        bool less_than_both = (root->val < p->val && root->val < q->val);
        bool more_than_both = (root->val > p->val && root->val > q->val);
        while (less_than_both || more_than_both)
        {
            less_than_both = (root->val < p->val && root->val < q->val);
            more_than_both = (root->val > p->val && root->val > q->val);
            if (less_than_both) {
                root = root->right;
            } else {
                root = root->left;
            }
        }
        return root;
    }
};

int main(void)
{
    TreeNode a, b, c, d, e, f, g;

    a.val = 40;
    b.val = 30;
    c.val = 50;
    d.val = 25;
    e.val = 35;
    f.val = 45;
    g.val = 60;

    a.left = &b;
    a.right = &c;

    b.left = &d;
    b.right = &e;

    c.left = &f;
    c.right = &g;

    // TreeNode a,b,c;

    // a.val = 5;
    // b.val = 1;
    // c.val = 7;
    // a.left = &b;
    // a.right = &c;

    Solution sol;

    auto result = sol.lowestCommonAncestor(&a, &b, &c);

    cout << result->val << endl;
}