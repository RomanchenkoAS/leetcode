/*Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character, but a character may map to itself.*/

#include <iostream>
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

        short length = s.length();

        unordered_map<char, char> subs, subs_back;

        for (int i = 0; i < length; i++)
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

        string s_copy(length, ' '), t_copy(length, ' ');

        for (int i = 0; i < length; i++)
        {
            s_copy[i] = subs[s[i]];
        }
        for (int i = 0; i < length; i++)
        {
            t_copy[i] = subs_back[t[i]];
        }

        return s == t_copy && t == s_copy;
    }
};

int main(void)
{
    Solution sol;

    string s = "paper";
    string t = "title";
    // string s = "foo";
    // string t = "bar";
    // string s = "badc";
    // string t = "baba";

    bool result = sol.isIsomorphic(s, t);

    cout << endl
         << "result = " << result << endl;

    return 0;
}