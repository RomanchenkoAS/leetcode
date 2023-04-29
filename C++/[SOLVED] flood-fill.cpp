/*An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from 
the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting 
pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to 
those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.*/

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void dynamic_fill(vector<vector<int>> &image, int sr, int sc, int color, int initial_color, int n, int m)
    {
        image[sr][sc] = color;
        // for (auto i : image)
        // {
        //     for (auto j : i)
        //     {
        //         cout << j << " ";
        //     }
        //     cout << endl;
        // }
        // cout << endl;
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