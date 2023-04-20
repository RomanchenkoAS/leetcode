/* Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is 
equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1. */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        size_t s = nums.size();

        for (int i = 0; i < s; i++) {
            int leftsum = 0, rightsum = 0;

            for (int j = 0; j < i; j++) {
                leftsum += nums[j];
            }

            for (int j = i + 1; j < s; j++) {
                rightsum += nums[j];
            }

            if (leftsum == rightsum) {
                return i;
            }
        }

        return -1;
    }
};

int main(void) {

    vector<int> input = {1,7,3,6,5,6};

    Solution sol;

    int result = sol.pivotIndex(input);

    cout << result << endl;

    return 0;
}