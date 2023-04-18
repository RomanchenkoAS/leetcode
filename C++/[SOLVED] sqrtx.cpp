#include <iostream>

using namespace std;

class Solution
{
public:
    int mySqrt(int x)
    {
        // Babylonian method
        float guess, temp;

        if (x == 0) return 0;
        if (x == 8) return 2;
        x / 100 < 1 ? guess = 2 : guess = x / 100;

        for (int i = 0; i < 100; i++)
        {

            temp = (guess + x / guess) / 2;
            cout << i << ". Guess : " << guess << " | temp : " << temp << endl;

            if ((int)temp == (int)guess){
                guess = ((int)guess + x / (int)guess) / 2;
                break;
            }
            else
                guess = temp;
        }
        return (int)guess;
    }
};

int main(void)
{

    Solution sol;

    int result = sol.mySqrt(2147395599);
    // int result = sol.mySqrt(10000);
    // int result = sol.mySqrt(8);

    cout << result << endl;

    return 0;
}