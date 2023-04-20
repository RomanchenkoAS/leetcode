/* Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is
equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1. */

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {

        size_t s = nums.size();

        vector<int> rightsum = {0};
        int leftsum = 0;

        // Calculate rightsum array
        for (int i = (s - 1); i >= 0; i--)
        {
            rightsum.push_back(nums[i] + rightsum[s - i - 1]);
        }

        for (int i = 0; i < s; i++)
        {
            leftsum = leftsum + nums[i - 1];
            if (leftsum == rightsum[s - i - 1])
                return i;
        }

        return -1;
    }
};

int main(void)
{

    vector<int> input = {1, 7, 3, 6, 5, 6};
    // vector<int> input = {2, 1, -1};
    // vector<int> input = {};

    Solution sol;

    int result = sol.pivotIndex(input);

    cout << result << endl;

    return 0;
}