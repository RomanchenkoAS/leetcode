/* You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
    }
};

int main(void)
{

    vector<int> input = {1, 7, 3, 6, 5, 6};
    // vector<int> input = {1,2,3};
    // vector<int> input = {2, 1, -1};
    // vector<int> input = {};

    Solution sol;

    int result = sol.maxProfit(input);

    cout << result << endl;

    return 0;
}