/*Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void dynamic_fill(vector<vector<char>> &image, int sr, int sc, int n, int m)
    {
        image[sr][sc] = '0';

        if (sr - 1 >= 0 && image[sr - 1][sc] == '1')
        {
            dynamic_fill(image, sr - 1, sc, n, m);
        }
        if (sr + 1 < n && image[sr + 1][sc] == '1')
        {
            dynamic_fill(image, sr + 1, sc, n, m);
        }
        if (sc - 1 >= 0 && image[sr][sc - 1] == '1')
        {
            dynamic_fill(image, sr, sc - 1, n, m);
        }
        if (sc + 1 < m && image[sr][sc + 1] == '1')
        {
            dynamic_fill(image, sr, sc + 1, n, m);
        }
    }

    int numIslands(vector<vector<char>> &grid)
    {
        size_t n = grid.size(), m = grid[0].size();
        int number = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    number++;
                    dynamic_fill(grid, i, j, n, m);
                }
            }
        }

        return number;
    }
};

int main(void)
{

    vector<vector<char>> grid = {{'1', '1', '1'}, {'1', '1', '0'}, {'1', '0', '1'}};
    // int sr = 1, sc = 1, color = 2;
    // vector<vector<int>> grid = {{0, 0, 0}, {0, 0, 0}};
    // int sr = 1, sc = 0, color = 2;

    Solution sol;

    // cout << "size1 : " << image[0].size() << endl; // horizontal || number of columns
    // cout << "size2 : " << image.size() << endl;    // vertical || number of rows

    auto result = sol.numIslands(grid);

    cout << result << endl;

    return 0;
}