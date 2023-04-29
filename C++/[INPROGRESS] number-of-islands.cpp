/*Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void dynamic_fill(vector<vector<int>> &image, int sr, int sc, int color, int initial_color, int n, int m)
    {
        image[sr][sc] = color;

        if (sr - 1 >= 0 && image[sr - 1][sc] == initial_color)
        {
            dynamic_fill(image, sr - 1, sc, color, initial_color, n, m);
        }
        if (sr + 1 < n && image[sr + 1][sc] == initial_color)
        {
            dynamic_fill(image, sr + 1, sc, color, initial_color, n, m);
        }
        if (sc - 1 >= 0 && image[sr][sc - 1] == initial_color)
        {
            dynamic_fill(image, sr, sc - 1, color, initial_color, n, m);
        }
        if (sc + 1 < m && image[sr][sc + 1] == initial_color)
        {
            dynamic_fill(image, sr, sc + 1, color, initial_color, n, m);
        }
    }

    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
    {
        size_t n = image.size(), m = image[0].size();
        if (image[sr][sc] == color) {
            return image;
        }
        dynamic_fill(image, sr, sc, color, image[sr][sc], n, m);
        return image;
    }
};

int main(void)
{

    // vector<vector<int>> image = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
    // int sr = 1, sc = 1, color = 2;
    vector<vector<int>> image = {{0, 0, 0}, {0, 0, 0}};
    int sr = 1, sc = 0, color = 2;

    Solution sol;

    // cout << "size1 : " << image[0].size() << endl; // horizontal || number of columns
    // cout << "size2 : " << image.size() << endl;    // vertical || number of rows

    auto result = sol.floodFill(image, sr, sc, color);

    for (auto i : result)
    {
        for (auto j : i)
        {
            cout << j << " ";
        }
        cout << endl;
    }

    return 0;
}