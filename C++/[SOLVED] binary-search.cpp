/*Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.*/

#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {

        // Ascending order
        if (nums.empty())
        {
            return -1;
        }
        if (nums.size() == 1)
        {
            return (nums[0] == target) ? 0 : -1;
        }

        int begin = 0, end = nums.size() - 1;

        int cursor = (begin + end) / 2;

        while (begin < end - 1)
        {
            if (nums[cursor] == target)
            {
                // Found it
                return cursor;
            }
            else
            {
                if (target > nums[cursor])
                {
                    begin = cursor + 1;
                }
                else
                {
                    end = cursor - 1;
                }
                cursor = (begin + end) / 2;
            }

        }

        if (nums[end] == target)
        {
            return end;
        }
        if (nums[begin] == target)
        {
            return begin;
        }

        return -1;
    }
};

int main(void)
{
    Solution sol;

    vector<int> input = {-1, 0, 5};

    int result = sol.search(input, 2);

    cout << result << endl;
}