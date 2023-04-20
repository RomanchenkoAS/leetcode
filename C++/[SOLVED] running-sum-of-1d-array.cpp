// Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

// Return the running sum of nums.

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        short size = nums.size();
        for (short i = 1; i < size; i++)
        {
            nums[i] += nums[i - 1];
        }

        return nums;
    }
};

int main(void)
{
    Solution sol;

    vector<int> input = {1, 2, 3, 4};

    cout << "Input: ";
    for (int i : input)
    {
        cout << i << " ";
    }

    cout << "; \n";

    vector<int> result = sol.runningSum(input);

    for (int i : result)
    {
        cout << i << endl;
    }
}