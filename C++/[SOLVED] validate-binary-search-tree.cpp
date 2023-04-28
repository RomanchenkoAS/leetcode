/*Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.*/


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
    vector<int> nodes; // Store nodes values

    void validate(TreeNode *root) {

        if (root->left) {
            validate(root->left);
        }

        nodes.push_back(root->val);

        if (root->right) {
            validate(root->right);
        }
    }

    bool isValidBST(TreeNode *root)
    {
        if (!root) return true;

        validate(root);

        for (int i = 0; i < nodes.size() - 1; i++) {
            if (nodes[i] >= nodes[i + 1]) {
                return false;
            }
        }

        return true;
    }
};

int main(void) {
    TreeNode a, b, c, d, e, f;

    b.val = 4;
    c.val = 7;
    a.val = 5;
    d.val = 3;
    e.val = 9;
    f.val = 6;

    a.left = &b;
    a.right = &c;
    b.left = &d;
    c.right = &e;
    c.left = &f;

    // TreeNode a,b,c;

    // a.val = 5;
    // b.val = 1;
    // c.val = 7;
    // a.left = &b;
    // a.right = &c;


    Solution sol;

    auto result = sol.isValidBST(&a);

    cout << result << endl;
}