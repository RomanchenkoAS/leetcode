/*Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
*/

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {


        return true;
    }
};

int main(void)
{
    Solution sol;

    string s = "egg";
    string t = "add";

    bool result = sol.isSubsequence(s, t);

    cout << endl
         << "reult = " << result << endl;

    return 0;
}