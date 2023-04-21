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
    bool isSubsequence(string s, string t)
    {
        if (s == t)
        {
            return true;
        }

        for (int i = 0; i < t.size(); i++)
        {
            if (t[i] == s[0])
            {
                s.erase(0, 1);
            }
            if (!s[0])
            {
                return true;
            }
        }
        return s[0] ? false : true;
    }
};

int main(void)
{
    Solution sol;

    string s = "ace";
    string t = "abcbedfdwefevd";

    bool result = sol.isIsomorphic(s, t);

    cout << endl
         << "reult = " << result << endl;

    return 0;
}