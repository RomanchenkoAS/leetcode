/*Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character, but a character may map to itself.*/

#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        // Different length
        if (s.length() != t.length())
        {
            return false;
        }
        // Empty input
        if (s.length() == t.length() && s.length() == 0)
        {
            return true;
        }

        unordered_map<char, char> subs, subs_back;

        for (int i = 0; i < s.length(); i++)
        {
            if (subs.count(s[i]) == 0)
            {
                subs[s[i]] = t[i];
            }
            if (subs_back.count(t[i]) == 0)
            {
                subs_back[t[i]] = s[i];
            }
        }

        return subs.size() == subs_back.size();
    }
};

int main(void)
{
    Solution sol;

    string s = "paper";
    string t = "title";
    // string s = "foo";
    // string t = "bar";

    bool result = sol.isIsomorphic(s, t);

    cout << endl
         << "result = " << result << endl;

    return 0;
}