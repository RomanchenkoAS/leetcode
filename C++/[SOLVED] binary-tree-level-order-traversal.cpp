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
#include <queue>

using namespace std;

class Solution
{
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        if (!root) {
            return {};
        }

        vector<vector<int>> result;
        vector<int> output;
        queue<TreeNode *> q;

        q.push(root);
        q.push(NULL); // Separator

        while (!q.empty())
        {
            // Remove the first item of queue and save it
            TreeNode *temp = q.front();
            q.pop();

            if (temp == NULL)
            {
                // We have reached end of the level
                result.push_back(output);
                output.clear();

                // If queue is not empty, there are still children to be checked
                // So we add a separator
                if (!q.empty()) {
                    q.push(NULL);
                }
            }
            else // temp is not NULL
            {
                output.push_back(temp->val);

                // Check the children
                if (temp->left) {
                    q.push(temp->left);
                }
                if (temp->right) {
                    q.push(temp->right);
                }
            }
        }

        return result;
    }
};

int main(void)
{

    TreeNode a, b, c, d, e, f;

    b.val = 1;
    c.val = 2;
    a.val = 3;
    d.val = 4;
    e.val = 5;
    f.val = 6;

    a.left = &b;
    a.right = &c;
    b.left = &d;
    c.right = &e;
    c.left = &f;

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