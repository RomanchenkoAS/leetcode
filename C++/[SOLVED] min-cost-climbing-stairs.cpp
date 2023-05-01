/*You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        size_t n = cost.size();
        int *total_cost = new int[n + 1];
        int sum = 0, position = n;

        total_cost[n] = 0;
        total_cost[n - 1] = cost[n - 1];

        for (int i = n - 2; i >= 0; i--)
        {
            total_cost[i] = min(total_cost[i + 1], total_cost[i + 2]) + cost[i];
        }

        int result = min(total_cost[0], total_cost[1]);

        delete[] total_cost;

        return result;
    }
};

int main(void)
{

    // vector<int> cost = {10, 15, 20};
    vector<int> cost = {1,100,1,1,1,100,1,1,100,1};
    // vector<int> cost = {0, 2, 2, 1};

    Solution sol;

    int output = sol.minCostClimbingStairs(cost);

    cout << output << endl;

    return 0;
}