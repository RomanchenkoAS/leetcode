/*Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character, but a character may map to itself.*/

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {

        return true;
    }
};

int main(void)
{
    Solution sol;

    string s = "egg";
    string t = "add";

    bool result = sol.isIsomorphic(s, t);

    cout << endl
         << "reult = " << result << endl;

    return 0;
}