/*You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?*/

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map <int, int> pathes;

    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }

        if (n == 2) {
            return 2;
        }

        if (!pathes.count(n)) {
            pathes[n] = climbStairs(n-1) + climbStairs(n-2);
        } 

        return pathes[n];
    }
};

int main(void) {

    Solution sol;

    auto result = sol.climbStairs(16);

    cout << result << endl;
    
    return 0;
}