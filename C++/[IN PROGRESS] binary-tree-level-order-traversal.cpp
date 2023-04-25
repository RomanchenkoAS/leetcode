/*Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).*/

//  Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> traversal(TreeNode *root)
{
    if (root == nullptr)
    {
        return {{}};
    }

    vector<vector<int>> res;

    vector<int> current;
    if (root->left != nullptr)
    {
        current.push_back(root->left->val);
    }
    if (root->right != nullptr)
    {
        current.push_back(root->right->val);
    }

    if (!current.empty())
    {
        res.push_back(current);
    }

    vector<vector<int>> left_tree;
    vector<vector<int>> right_tree;

    if (root->left != nullptr)
    {
        left_tree = traversal(root->left);
        res.insert(res.end(), left_tree.begin(), left_tree.end());
    }

    if (root->right != nullptr)
    {
        right_tree = traversal(root->right);
        res.insert(res.end(), right_tree.begin(), right_tree.end());
    }

    return res;
}

class Solution
{
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        if (root == nullptr) {
            return {{}};
        }
        vector<vector<int>> result = {{root->val}};
        vector<vector<int>> traversed;

        traversed = traversal(root);

        result.insert(result.end(), traversed.begin(), traversed.end());

        return result;
    }
};

int main(void)
{

    TreeNode a, b, c, d, e;

    b.val = 1;
    c.val = 2;
    a.val = 3;
    d.val = 4;
    e.val = 5;
    

    a.left = &b;
    a.right = &c;
    b.left = &d;
    c.right = &e;

    Solution sol;

    auto result = sol.levelOrder(&a);

    for (auto i : result)
    {
        for (auto j : i)
        {
            cout << j << " ";
        }
        cout << "\n";
    }
}
