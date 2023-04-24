/* You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0. */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    int lastStoneWeight(vector<int> &stones)
    {
        priority_queue<int> pr_q;

        for (int i : stones)
        {
            pr_q.push(i);
        }

        int x, y;

        while (pr_q.size() > 1)
        {
            x = pr_q.top();
            pr_q.pop();
            y = pr_q.top();
            pr_q.pop();

            // If stones are the same weight
            if (x == y)
            {
                if (pr_q.size() == 0)
                {
                    // Only two left, both are destroyed, result equals to 0
                    return 0;
                }
                else
                {
                    // Both are destroyed, go on
                    continue;
                }
            }

            // Make sure x > y
            if (y > x)
            {
                swap(x, y);
            }

            x -= y;

            pr_q.push(x);

        }

        return pr_q.top();
    }
};

int main(void)
{

    // vector<int> input = {1, 7, 3, 6, 5, 6};
    // vector<int> input = {1,2,3};
    // vector<int> input = {2, 1, -1};
    // vector<int> input = {};
    // vector<int> input = {1,3};
    vector<int> input = {2,2};

    Solution sol;

    int result = sol.lastStoneWeight(input);

    cout << result << endl;

    return 0;
}