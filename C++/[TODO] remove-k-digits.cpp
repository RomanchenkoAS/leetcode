/*Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.*/

#include <iostream>
#include <vector>

using namespace std;

void remove_digit(string num, int k_curr, int & k, vector<string> & possible_numbers)
{

    // Base case - lowest level
    if (k_curr == k)
    {
        for (int i = 0; i < num.size(); i++)
        {
            string result = "";
            for (int j = 0; j < num.size(); j++)
            {
                if (i != j)
                {
                    result += num[j];
                }
            }
            possible_numbers.push_back(result);
        }
    }
    else {
        for (int i = 0; i < num.size(); i++)
        {
            string result = "";
            for (int j = 0; j < num.size(); j++)
            {
                if (i != j)
                {
                    result += num[j];
                }
            }
            remove_digit(result, k_curr+1, k, possible_numbers);
        }
    }
}

class Solution
{
public:
    string removeKdigits(string num, int k)
    {
        vector<string> possible_numbers;

        if (k >= num.size()) {
            return "0";
        }

        remove_digit(num, 1, k, possible_numbers);

        int min = stoi(possible_numbers[0]);

        for (int i = 1; i < possible_numbers.size(); i++) {
            int current = stoi(possible_numbers[i]);
            if (current < min) {
                min = current;
            }
        }

        return to_string(min);

    }
};

int main(void)
{
    Solution sol;

    string num = "1432219";
    // string num = "10";
    // string num = "10200";
    int k = 1000;

    string result = sol.removeKdigits(num, k);

    cout << result << endl;

    return 0;
}