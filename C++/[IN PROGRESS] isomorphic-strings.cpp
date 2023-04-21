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
    bool isIsomorphic(string s, string t) {
        if (s == t) {
            return true;
        }
        // int index = 0;
        // for (int i = 0; i < s.size(); i++) {
        //     // Look for s[i] in t (index .. size)
        //     // Record index
        //     // If not found return false

        //     for (int j = index; j < t.size(); j++) {
        //         index ++;
        //         if (s[i] == t[j]) {
        //             break;
        //         }
        //     }

        //     if (index > t.size()) {
        //         return false;
        //     }
        // }

        int index = 0;

        while (t[index]) {
            cout << t[index];
            index ++;
        }

        return true;
    }
};

int main(void)
{
    Solution sol;

    string s = "ace";
    string t = "abcb";

    bool result = sol.isIsomorphic(s, t);

    cout << endl << "reult = " << result << endl;

    return 0;
}