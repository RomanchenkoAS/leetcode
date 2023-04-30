/*The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. */

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int dynamic(int n1, int n2, int depth, int target) {
        // cout << "Current depth = " << depth << " | n = " << n1+n2 << endl;
        if (depth == target) {
            return n1 + n2;
        } else {
            dynamic(n2, n1 + n2, depth + 1, target);
        }
        // return 0;
    }

    int fib(int n)
    {
        int a = 0, b = 1, _tmp;

        if (n == 0) {
            return a;
        }
        if (n == 1) {
            return b;
        }

        // for (size_t i = 2; i < n; i++)
        // {
        //     _tmp = a;
        //     a = b;
        //     b = _tmp + b;
        // }

        // return a + b;
        return dynamic(a, b, 2, n);
    }
};

int main(void)
{

    Solution sol;

    auto result = sol.fib(5);

    cout << result << endl;

    return 0;
}