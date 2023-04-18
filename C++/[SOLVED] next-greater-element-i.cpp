/*The next greater element of some element x in an array is the first greater element that is to the
right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is i0 subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<int> & nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        // Length of the vector nums2
        size_t l = nums2.size();

        // Substitution
        int subs = 0;

        for (short i = 0; i < nums1.size(); i++)
        {
            // Recieve iterator pointing at the element i
            auto ind = std::find(nums2.begin(), nums2.end(), nums1[i]);

            // Find position of i, calculating distance between 0 and i
            short i0 = std::distance(nums2.begin(), ind);

            // Initialize substitution with actual value of i'th element
            subs = nums1[i];

            for (short j = i0 + 1; j < l; j++)
            {
                if (nums2[j] > nums1[i])
                {
                    // If the number to the right is bigger than i'th, make a substitution
                    subs = nums2[j];
                    break;
                }
            }

            // If the substitution was not made, make it equal to -1
            if (subs == nums1[i])
            {
                subs = -1;
            }

            // Substitute
            nums1[i] = subs;
        }

        return nums1;
    }
};

int main(void)
{

    Solution sol;

    vector<int> nums1 = {4, 1, 2}, nums2 = {1, 3, 4, 2};

    vector<int> result = sol.nextGreaterElement(nums1, nums2);

    cout << "Result: " << endl;

    for (int i : result)
    {
        cout << i << " ";
    }

    cout << endl;

    return 0;
}