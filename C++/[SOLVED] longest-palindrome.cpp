/* Given a string s which consists of lowercase or uppercase letters, return the length of the 
longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here. */

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> seen;
        int size = 0;
        bool has_single = false;
        
        for (char c : s) {
            seen[c]++;

            // has a pair
            if (seen[c] % 2 == 0) {
                size += 2;
                seen[c] -= 2;
            }
        }

        return (s.length() == size) ? size : size + 1;
        
    }
};

int main(void)
{

    string input = "abccccdd";

    Solution sol;

    int result = sol.longestPalindrome(input);

    cout << result << endl;

    return 0;
}