#include <iostream>

using namespace std;

class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string result = "";

        short i = 0;

        short l1 = word1.length(), l2 = word2.length();

        do
        {
            if (i < l1)
            {
                result += word1[i];
            }
            if (i < l2)
            {
                result += word2[i];
            }

            i++;

        } while (i < l1 || i < l2);

        return result;
    }
};

int main(void)
{

    Solution sol;

    string input1 = "rlvrpyrhcxbceffrgiy";
    string input2 = "ktqi";

    // string input1 = "ab";
    // string input2 = "pqrs";

    string result = sol.mergeAlternately(input1, input2);

    cout << input1 << " || " << input2 << endl << result << endl;

    // for (int i = 0; i < result.length(); i ++ ) {
    //     int a = result[i];
    //     cout << result[i] << ": " << a <<  endl;

    // }

    return 0;
}